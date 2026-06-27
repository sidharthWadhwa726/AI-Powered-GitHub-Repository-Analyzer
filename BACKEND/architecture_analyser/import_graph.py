# this is the file that will generate the import graph  for a single file 
from tree_sitter_language_pack import get_parser
IMPORT_NODES = {
    "python": {"import_statement", "import_from_statement"},
    "javascript": {"import_statement"},
    "typescript": {"import_statement"},
    "java": {"import_declaration"},
    "go": {"import_declaration"},
    "cpp": {"preproc_include"},
    "c": {"preproc_include"},
    "rust": {"use_declaration"},
}
def get_import_name(node, content):
    return content[node.start_byte():node.end_byte()]

def collect_imports(node, content, imports, language):
    if node.kind() in IMPORT_NODES.get(language, set()):
        imports.append(get_import_name(node, content))

    for i in range(node.child_count()):
        collect_imports(node.child(i),content,imports,language)

def get_import_graph(content, language):
    parser = get_parser(language)
    tree = parser.parse(content)
    imports = []
    collect_imports(tree.root_node(),content,imports, language)

    return imports