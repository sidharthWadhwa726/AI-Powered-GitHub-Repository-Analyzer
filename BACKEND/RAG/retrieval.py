from RAG.chroma_database import collection
from RAG.creating_embeddings import embedding_model

def retrieve_chunks(query : str, repo_id : str):
    query_vector = embedding_model.encode(query,normalize_embeddings=True ).tolist()
    results = collection.query(query_embeddings = [query_vector],n_results = 10 , where= {"repo" : repo_id})
    return results 
