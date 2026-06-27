import chromadb

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="repo_chunks")

def store_chunks_in_chroma(embedded_chunks):
    if not embedded_chunks:
        return
    collection.upsert(
        ids=[chunk["id"] for chunk in embedded_chunks],
        documents=[chunk["content"] for chunk in embedded_chunks],
        embeddings=[chunk["embedding"] for chunk in embedded_chunks],
        metadatas=[chunk["metadata"] for chunk in embedded_chunks])
    print(collection.count())
    


