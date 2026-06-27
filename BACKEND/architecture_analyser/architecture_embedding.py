from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
def architecture_to_documents(repo_id, architecture):
    """
    Convert architecture JSON into searchable documents.
    """
    documents = []
    for section, value in architecture.items():
        if value is None:
            continue
        # Convert any object into text
        if isinstance(value, str):
            text = value
        else:
            import json
            text = json.dumps(value, indent=2)
        # Small sections
        if len(text) <= 1000:
            documents.append({
                "repo_id": repo_id,
                "document_type": "architecture",
                "section": section,
                "chunk_index": 0,
                "content": text
            })
        # Large sections
        else:
            chunks = splitter.split_text(text)
            for i, chunk in enumerate(chunks):
                documents.append({
                    "repo_id": repo_id,
                    "document_type": "architecture",
                    "section": section,
                    "chunk_index": i,
                    "content": chunk
                })
    return documents