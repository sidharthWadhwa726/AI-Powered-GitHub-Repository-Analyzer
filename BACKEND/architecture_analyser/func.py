from tree_sitter_language_pack import get_parser

# dealing all diff things for all the languages 
FUNCTION_NODES = {
    "python": {"function_definition"},
    "javascript": {"function_declaration"},
    "typescript": {"function_declaration"},
    "java": {"method_declaration"},
    "cpp": {"function_definition"},
    "c": {"function_definition"},
    "go": {"function_declaration"},
    "rust": {"function_item"},
}

CALL_NODES = {
    "python": {"call"},
    "javascript": {"call_expression"},
    "typescript": {"call_expression"},
    "java": {"method_invocation"},
    "cpp": {"call_expression"},
    "c": {"call_expression"},
    "go": {"call_expression"},
    "rust": {"call_expression"},
}


# this is used to fetch the name for the functions 
def get_func_name(node , content):
    for i in range(node.child_count()):
        child = node.child(i)
        if child.kind() in {"identifier","property_identifier","field_identifier"}:
            return content[child.start_byte():child.end_byte()]
    return None

# if function node get inside that 
# this means the functions called inside the another functions 
def get_function_calls(function_node , content, calls,language):
    if(function_node.kind() in CALL_NODES[language]):
        calls.append(content[function_node.start_byte():function_node.end_byte()])
    
    for i in range(function_node.child_count()):
        get_function_calls(function_node.child(i) , content,calls,language)

# going to each node in the graph 
def build_graph(node, content , graph, language):
    if(node.kind() in FUNCTION_NODES[language]) :
        # checking if it contains the func 
        func_name = get_func_name(node,content)
        calls = []
        get_function_calls(node,content,calls,language)
        graph[func_name] = calls
    
    for i in range(node.child_count()):
        build_graph(node.child(i),content,graph, language)



# main func
def get_complete_graph(content , language):
    parser = get_parser(language)
    tree = parser.parse(content)
    graph = {}
    build_graph(tree.root_node() , content , graph, language)
    return graph 


# ALLOWED_EXTENSIONS = {
#     ".py",".js",".jsx",".ts",".tsx",
#     ".java",".cpp",".c",".go",
#     ".md",".json",".yml",".yaml",
#     ".html",".css"
# }


# language = "java"
# code = """

#     void processRepo() {
#         chunkFile();
#     }

# """
# def dfs(node, depth=0):
#     print("  " * depth + node.kind())

#     for i in range(node.child_count()):
#         dfs(node.child(i), depth + 1)



# parser = get_parser(language)
# tree = parser.parse(code)
# dfs(tree.root_node())
# # print(get_complete_graph(code,language))