import os
from haystack import Document
from haystack.pipelines import Pipeline
from configure import document_store, dense_retriever, rerank

os.environ['TOKENIZERS_PARALLELISM'] = 'False'


def create_document(intent_name, examples):
    docs_final = []
    for i, example in enumerate(examples):
        document = Document(id=f"{i}_{intent_name}",
                            content=example, meta={"intent_name": intent_name})

        docs_final.append(document)

    return docs_final


def add_intent(intent_name, examples):
    all_add_list = create_document(intent_name, examples)

    if all_add_list:
        document_store.write_documents(all_add_list)
        document_store.update_embeddings(dense_retriever)


def delete_intent(intent_name):
    filter_query = {
        "intent_name": [intent_name]
    }

    document_store.delete_documents(filters=filter_query)



def create_response(answer):
    response_dict = dict()
    response_dict['IntentName'] = answer.meta['intent_name']
    response_dict['Response'] = answer.meta['response_text']
    response_dict['Response_url'] = answer.meta['response_url']
    response_dict['Queries'] = answer.meta['questions']
    response_dict['OrgID'] = answer.meta['org_id']
    response_dict['Score'] = round(answer.score, 2)
    response_dict['content'] = answer.context

    return response_dict


def match_intent(query):
    """### Ask questions
    Initialize a Pipeline (this time without a reader) and ask questions
    """

    pipeline = Pipeline()

    pipeline.add_node(component=dense_retriever, name="DenseRetriever", inputs=["Query"])
    pipeline.add_node(component=rerank, name="ReRanker", inputs=["DenseRetriever"])

    prediction = pipeline.run(
        query=query,
        params={
            "DenseRetriever": {"top_k": 10},
            "ReRanker": {"top_k": 1},
        },
    )


    if prediction['documents']:
        if prediction['documents'][0].score > 0.6:
            return prediction['documents'][0].meta['intent_name']
        else:
            return "No matching intent found"

    else:
        return "No matching intent found"




