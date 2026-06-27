import os
import requests
from fastapi import FastAPI, HTTPException

ALLOWED_EXTENSIONS = {
    ".py",".js",".jsx",".ts",".tsx",
    ".java",".cpp",".c",".go",
    ".md",".json",".yml",".yaml",
    ".html",".css"
}

IGNORED_DIRS = {
    "node_modules",
    ".git",
    "dist",
    "build",
    "coverage",
    "__pycache__",
    ".next",
    ".venv"
}


def is_allowed(path):
    folders = path.split("/")
    for folder in folders:
        if folder in IGNORED_DIRS:
            return False
    ext = os.path.splitext(path)[1]
    return ext in ALLOWED_EXTENSIONS


def fetch_repo_tree(owner, repo):
    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/git/trees/HEAD?recursive=1"
    )
    headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github+json"
    }
    response = requests.get(url,headers=headers)
     # checking errors
    if response.status_code == 404:
        raise HTTPException(status_code=404,detail=f"Repository {owner}/{repo} not found")

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,detail="GitHub API Error")

    # all the contents of the repo are in the tree 
    tree = response.json()["tree"]
    
    files = []
    for item in tree:
        if(item["type"] == "blob" and is_allowed(item["path"])):
            files.append(item)
    return files