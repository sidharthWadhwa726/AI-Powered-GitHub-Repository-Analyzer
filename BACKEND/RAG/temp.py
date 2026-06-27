import chromadb
client = chromadb.PersistentClient(path="./chroma_db")
client.delete_collection("repo_chunks")
print("Deleted repo_chunks")