from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os 
from dotenv import load_dotenv
# importing the main function from the chunking.py 
from RAG.chunking import chunk_file
from sentence_transformers import SentenceTransformer
load_dotenv()
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def process_repo(repoFiles, repo_id : str):
    AllChunks = []
    for file in repoFiles:
        chunk = chunk_file(file['path'] , file['content'])
        AllChunks.extend(chunk)
    
    codes = [chunk ['content'] for chunk in AllChunks]
    vectors =  embedding_model.encode(codes,convert_to_numpy=True,normalize_embeddings=True)
    embedded_chunks = []

    for index, (chunk, vector) in enumerate(zip(AllChunks, vectors)):
        chunk_index = chunk.get("chunk_index", index)

        embedded_chunks.append({
            "id": f'{repo_id}::{chunk["file_path"]}::chunk_{chunk_index}',
            "content": chunk["content"],
            "embedding": vector.tolist(),
            "metadata": {
                "repo": repo_id,
                "file_path": chunk["file_path"],
                "chunk_type": chunk.get("chunk_type", "unknown"),
                "chunk_index": chunk_index,
                "start_line": chunk.get("start_line"),
                "end_line": chunk.get("end_line")
            }
        })

    return embedded_chunks

def process_architecture(documents, repo_id):
    texts = [doc["content"] for doc in documents]

    vectors = embedding_model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    embedded_documents = []

    for index, (doc, vector) in enumerate(zip(documents, vectors)):

        chunk_index = doc.get("chunk_index", index)

        embedded_documents.append({
            "id": f'{repo_id}::ARCH::{doc["section"]}::{chunk_index}',
            "content": doc["content"],
            "embedding": vector.tolist(),
            "metadata": {
                "repo": repo_id,
                "document_type": "architecture",
                "section": doc["section"],
                "chunk_index": chunk_index
            }
        })

    return embedded_documents