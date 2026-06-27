from architecture_analyser.func import get_complete_graph
from pathlib import Path

EXTENSION_TO_LANGUAGE = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".java": "java",
    ".cpp": "cpp",
    ".c": "c",
    ".go": "go",
    ".rs": "rust"
} 

def detect_language(path):
    extension = Path(path).suffix
    # .get() is safer then []
    return EXTENSION_TO_LANGUAGE.get(extension)

# this is the main loop for the graph of all functions  of all the files 
def analyse_repo(repo_files):
    repo_graph = {}
    for repo_file in repo_files:
        path = repo_file["path"]
        content = repo_file["content"]

        lang = detect_language(path)
        if not lang:
            continue

        repo_graph[path] = get_complete_graph(content, lang)

    return repo_graph


