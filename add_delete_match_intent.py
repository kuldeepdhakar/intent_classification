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






if __name__ == '__main__':
    intent_data_1 = {
        "name": "book-a-ticket",
        "examples": [
            "I want to book a ticket from Hyderabad to Chennai",
            "I'd like to book a plane ticket for a flight on August 25th",
            "Can you help me reserve a seat on a flight from New York to Los Angeles?",
            "I'm interested in flying to Paris from London on the 10th of September.",
            "I want to travel to Tokyo and I need a ticket for a flight next week.",
            "Could you assist me in booking a flight from Chicago to Miami on the 15th of October?",
            "I'm looking for a round-trip ticket from San Francisco to Seattle for the weekend of November 5th.",
            "I need to get to Dubai from Mumbai, preferably on a direct flight.",
            "Can you check for available flights from Toronto to Vancouver for the 20th of December?",
            "I'm planning a trip to Rome, and I'd like to book a business class ticket with extra legroom.",
            "I want to fly to London, departing on the 8th of January and returning on the 20th."
        ]
    }

    intent_data_2 = {
        "name": "flight-cancellation",
        "examples": [
            "Cancel my booking for the flight.",
            "I want to cancel my reservation.",
            "Can you help me with canceling my flight?",
            "Cancel my booking for the flight from [source] to [destination].",
            "I need to cancel my flight on [date].",
            "How do I cancel my booking?",
            "I want to cancel my reservation with confirmation number [confirmation number].",
            "Can you assist me in canceling my flight?",
            "What's the process for canceling my flight?",
            "I'd like to cancel my booking for the flight on [date]."
        ]
    }
    intent_data_3 = {
        "name": "check-reservation",
        "examples": [
            "What's the reservation status for booking ID ABC123?",
            "Can you provide me with the current boarding status for my flight?",
            "I'd like to know if my reservation for flight XYZ456 is confirmed.",
            "What's the seat number allocated for my reservation with confirmation number DEF789?",
            "Has there been any seat upgrade for my booking on flight LMN567?",
            "Can you check the reservation status for the email address john.doe@email.com?",
            "I want to inquire about the boarding status of my flight with booking reference GHI234.",
            "Please tell me the current status of my reservation for flight JKL890.",
            "Has there been any change in the seat assignment for my booking on flight MNO123?",
            "What's the reservation status for my ticket on the flight with departure code PQR456?"
        ]
    }

    intent_data_4 = {
      "name": "check-booking-status",
      "examples": [
        "What's the booking status for reservation ID XYZ789?",
        "Can you provide me with the current seat assignment for my booking?",
        "I'd like to know if my booking for flight ABC123 is confirmed.",
        "What's the departure gate for my reservation with confirmation number LMN456?",
        "Has there been any cabin upgrade for my reservation on flight DEF789?",
        "Can you check the booking status for the email address jane.doe@email.com?",
        "I want to inquire about the gate information for my flight with booking reference QRS123.",
        "Please tell me the current status of my booking for flight WXY456.",
        "Has there been any change in the meal preference for my booking on flight TUV123?",
        "What's the booking status for my ticket on the flight with reference code STU456?"
      ]
    }

    # add_intent(intent_data_1)
    # add_intent(intent_data_2)
    # add_intent(intent_data_3)
    # add_intent(intent_data_4)
    # delete_intent("check-booking-status")

    print(match_intent(query="What's the booking status for reservation ID XYZ789?"))
