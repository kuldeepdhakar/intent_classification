import logging
from haystack.nodes import EmbeddingRetriever
from haystack.nodes import SentenceTransformersRanker
from qdrant_haystack.document_stores import QdrantDocumentStore

logging.basicConfig(format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
logging.getLogger("haystack").setLevel(logging.INFO)

INDEX_NAME = "intent_data"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
RERANKER_MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"
EMB_DIM = 384

document_store = QdrantDocumentStore(
    url="https://5b34c796-bffa-41ea-8408-1d8655b48564.us-east4-0.gcp.cloud.qdrant.io",
    index=INDEX_NAME,
    api_key="2xnqaAOL8RC6hcRpT1TZ3QINII2p3KybYd1yudkM13e9w-maQWc7ag",
    # recreate_index=True,
    embedding_dim=EMB_DIM
)


dense_retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model=EMBEDDING_MODEL_NAME,
    use_gpu=True,
    scale_score=False
)

rerank = SentenceTransformersRanker(model_name_or_path=RERANKER_MODEL_NAME)

