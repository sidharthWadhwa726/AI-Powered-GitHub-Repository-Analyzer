from fastapi import APIRouter
from models.repo_request import RepoRequest
from services.parse_repo import (parse_github_repo)
from services.fetch_repo_tree import (fetch_repo_tree)
from services.fetch_file_content import (fetch_file_content)
from RAG.creating_embeddings import (process_repo,process_architecture)
from RAG.chroma_database import (store_chunks_in_chroma)
from architecture_analyser.analyse_comp_repo import analyse_repo
from architecture_analyser.architecture_builder import build_architecture
from architecture_analyser.save_architecture import save_architecture
from architecture_analyser.load_architecture import load_architecture
from RAG.architecture_embedding import architecture_to_documents
router = APIRouter()

@router.post("/repo/index")
def ingest_repo(request : RepoRequest):
    owner , repo = parse_github_repo(request.repo_url)
    repo_id = f"{owner}/{repo}"
    files = fetch_repo_tree(owner , repo)
    repo_files = []
    for file in files:
        content = fetch_file_content(owner,repo,file["path"])
        if content:
            repo_files.append({"path": file["path"],"content": content})
    # chunking and  embedding
    embedded_chunks = process_repo(repo_files, repo_id)
    # storing them in the data base 
    store_chunks_in_chroma(embedded_chunks=embedded_chunks)
    # calling for the architecture repo 
    architecture = build_architecture(repo_files)
    save_architecture(repo_id,architecture)
    # this is for the architecture 
    architecture_docs = architecture_to_documents(repo_id,architecture)
    embedded_architecture = process_architecture(architecture_docs,repo_id)

    store_chunks_in_chroma(embedded_architecture)    
    return {
        "success" : True ,
        "repo" : repo_id,
        "chunks_stored" : len(embedded_chunks),
        "architecture_saved": True,
    }


@router.get("/repo/architecture/{owner}/{repo}")
def get_architecture (owner : str , repo : str):
    repo_id = f"{owner}/{repo}"
    architecture = load_architecture(repo_id)
    return architecture
