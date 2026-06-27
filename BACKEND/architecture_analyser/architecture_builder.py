from .folder_tree import build_folder_tree
from .analyse_comp_repo import analyse_repo
from .analyse_imports import analyse_imports
from .architecture_summary import generate_architecture_summary
# this is the main file for the building the archotecture
def build_architecture(repo_files):
    folder_tree = build_folder_tree(repo_files)
    function_graph = analyse_repo(repo_files)
    import_graph = analyse_imports(repo_files)
    summary = generate_architecture_summary(folder_tree,function_graph,import_graph)
    return {
        "folder_tree": folder_tree,
        "function_graph": function_graph,
        "import_graph": import_graph,
        "summary": summary
    }