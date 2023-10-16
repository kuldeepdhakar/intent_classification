# Intent_Classification
This repository contains code designed for classifying user queries into specific intents, and it employs a retrieval-reranker approach. The primary steps involved in this approach are as follows:

### Data Indexing: 
Initially, we have indexed a comprehensive set of example queries corresponding to various intents into an open-source vector database (qdrant). Each of these indexed queries is represented by embeddings generated using the "sentence-transformers/all-MiniLM-L6-v2" model. This model is responsible for converting the textual queries into numerical representations.

### Reranker Model: 
For the reranking process, we utilize the "cross-encoder/ms-marco-MiniLM-L-6-v2" model. This model evaluates and ranks the similarity between the user query and the indexed queries, ultimately improving the accuracy of the intent classification.

When a user submits a query, the following steps are carried out:

### Query Embedding: 
The user's query is first converted into an embedding using the same "sentence-transformers/all-MiniLM-L6-v2" model employed during the indexing stage. This results in a numerical representation of the user's query.

### Semantic Similarity Calculation: 
The next step involves computing the semantic similarity, typically using cosine similarity, between the user's query embedding and the embeddings stored in the database for all the indexed queries. This process identifies the top 10 most similar queries from the database.

### Reranking: 
These top 10 retrieved queries are then reranked by the "cross-encoder/ms-marco-MiniLM-L-6-v2" model, which assesses their relevance to the user's query. The query with the highest reranked score is considered the most relevant.

### Intent Classification: 
The intent related to the query that achieved the highest reranked score is determined and returned as the intent of the user's query.

## How to Run and Test
Here's a more structured and coherent explanation of the provided information:

1. **Python Version**: The code is written in Python version 3.8, and it is important to note this requirement as it ensures compatibility with the codebase.

2. **Requirements.txt File**: The "requirements.txt" file contains a list of all the necessary dependencies and packages required to run the code successfully. To install these dependencies, you can use the following command:
   
   ```bash
   pip install -r requirements.txt
   ```

   This command simplifies the installation process by automatically fetching and installing all the required packages listed in the "requirements.txt" file.

3. **Flask_api.py**: The "flask_api.py" file is the core of the application and contains all the endpoints for the Flask API. To start the server and make the API accessible, you can execute this file. It serves as the entry point for running the application and handling API requests.

4. **add_delete_match_intent.py**: The "add_delete_match_intent.py" file includes essential functions for adding intents, deleting intents, and matching intents. These functions play a critical role in the intent management and classification processes.

5. **Configure.py**: The "configure.py" file is responsible for initializing the database (DB) and the retriever and reranker components. Proper configuration is pivotal for the correct functioning of the system, and this file handles those initializations.

6. **test_api.py**: The "test_api.py" file provides predefined functions that are designed for testing all the available endpoints in the API. These testing functions are valuable for assessing the functionality and reliability of the API as they allow for systematic and automated testing procedures.



