# Intent_Classification
This repository contains code designed for classifying user queries into specific intents, and it employs a retrieval-reranker approach. The primary steps involved in this approach are as follows:

## Data Indexing: 
Initially, we have indexed a comprehensive set of example queries corresponding to various intents into an open-source vector database (qdrant). Each of these indexed queries is represented by embeddings generated using the "sentence-transformers/all-MiniLM-L6-v2" model. This model is responsible for converting the textual queries into numerical representations.

## Reranker Model: 
For the reranking process, we utilize the "cross-encoder/ms-marco-MiniLM-L-6-v2" model. This model evaluates and ranks the similarity between the user query and the indexed queries, ultimately improving the accuracy of the intent classification.

When a user submits a query, the following steps are carried out:

## Query Embedding: 
The user's query is first converted into an embedding using the same "sentence-transformers/all-MiniLM-L6-v2" model employed during the indexing stage. This results in a numerical representation of the user's query.

## Semantic Similarity Calculation: 
The next step involves computing the semantic similarity, typically using cosine similarity, between the user's query embedding and the embeddings stored in the database for all the indexed queries. This process identifies the top 10 most similar queries from the database.

## Reranking: 
These top 10 retrieved queries are then reranked by the "cross-encoder/ms-marco-MiniLM-L-6-v2" model, which assesses their relevance to the user's query. The query with the highest reranked score is considered the most relevant.

## Intent Classification: 
The intent related to the query that achieved the highest reranked score is determined and returned as the intent of the user's query.
