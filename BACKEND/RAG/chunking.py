import os
from tree_sitter_language_pack import get_parser
from langchain_text_splitters import RecursiveCharacterTextSplitter

CODE_LANGUAGES = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".java": "java",
    ".cpp": "cpp",
    ".c": "c",
    ".go": "go",
    ".rs": "rust"
}

# this helps when we are chunking the texts files like readme 
def recursive_chunk(file_path, content):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    chunks = splitter.split_text(content)
    result = []

    for index, chunk in enumerate(chunks):
        result.append({
            "file_path": file_path,
            "chunk_type": "text",
            "chunk_index": index,
            "content": chunk})
        
    return result


#  for code bases and all
# traversing the tree recursively 
def traverse_tree(node, content, file_path, chunks):
    semantic_nodes = {
        "class_definition",
        "function_definition"
    }

    if node.kind() in semantic_nodes:
        print(type(node.start_byte))
        print(type(node.end_byte))
        chunk_content = content[node.start_byte():node.end_byte()]

        chunks.append({
            "file_path": file_path,
            "chunk_type": node.kind(),
            "chunk_index": len(chunks),
            "content": chunk_content
        })

    for i in range(node.child_count()):
        child = node.child(i)
        traverse_tree(child, content, file_path, chunks)
# semantic chunking on the basis of the nodes : {"class_definition","function_definition","method_definition"}
def semantic_chunk(file_path, content, language):
    parser = get_parser(language)
    tree = parser.parse(content)
    # print(file_path)
    # print(tree.root_node.children[:20])
    chunks = []
    traverse_tree(tree.root_node(),content,file_path,chunks)
    print(file_path, "=>", len(chunks))
    return chunks


# chunking all the files 
def chunk_file(file_path, content):
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()
    try:
        if extension in CODE_LANGUAGES:
            language = CODE_LANGUAGES[extension]
            chunks = semantic_chunk(file_path,content,language)
            if len(chunks) > 0:
                return chunks
        return recursive_chunk(file_path,content)
    except Exception as e :
        print(f"TREE SITTER ERROR in {file_path}: {e}")
        return recursive_chunk(file_path,content)
    