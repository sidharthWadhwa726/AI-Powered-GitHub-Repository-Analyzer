from .analyse_comp_repo import detect_language
from .import_graph import get_import_graph
# this is the main loop for the import graph of all the files 
def analyse_imports(repo_files):
    repo_imports = {}
    for repo_file in repo_files:
        path = repo_file["path"]
        content = repo_file["content"]
        lang = detect_language(path)
        if not lang:
            continue
        repo_imports[path] = get_import_graph(content,lang)
    return repo_imports


