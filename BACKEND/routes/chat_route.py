from fastapi import APIRouter
from models.chat_request import ChatRequest
from RAG.retrieval import (retrieve_chunks)
from services.gemini_service import (generate_answer)
from architecture_analyser.load_architecture import load_architecture
from services.chat_history import get_history, add_message
router = APIRouter()

@router.post("/chat")
def chat_repo(request : ChatRequest):
    results = retrieve_chunks(request.question , request.repo_id)
    # print(results)
    # print("QUESTION:", request.question)
    # print("FILES:")
    # print(results["metadatas"][0])

    # print("DOCUMENTS:")
    contexts = []
    for doc in results["documents"][0]:
        print(doc[:300])
        print("-"*50)
    # we want the ans to the single query  
        for doc, meta in zip(results["documents"][0],results["metadatas"][0]):
            contexts.append(f"""FILE: {meta['file_path']}TYPE: {meta['chunk_type']}{doc}""")
        
        history = get_history(request.session_id)
        architecture = load_architecture(request.repo_id)
        ans = generate_answer(request.question,contexts,architecture["summary"], history)
        add_message(request.session_id,request.question,ans)
    # ans = generate_answer(request.question,chunks)
    # sending the question to the model with the relvant chunks to avoid the hallucination 
    return {
        "answer": ans,
        "sources": [
            meta["file_path"]
            for meta in results["metadatas"][0]
        ]
    }

