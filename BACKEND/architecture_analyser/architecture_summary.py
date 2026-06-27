from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)
# this is the main model for the generating the summary or tthe question realated to the architecture andd all 
def generate_architecture_summary(folder_tree,function_graph,import_graph):
    prompt = f"""
        You are a senior software architect.
        Analyze this repository.
        Folder Tree:
        {folder_tree}
        Function Graph:
        {function_graph}
        Import Graph:
        {import_graph}
        Generate:
        1. Repository Overview
        2. Folder Responsibilities
        3. Main Modules
        4. Entry Points
        Identify the most likely entry point(s).
        5. Function Dependency Flow
        Explain how functions call one another.
        6. Module Dependency Flow
        Explain how files depend on one another.
        7. Likely Execution Flow
        Infer the most probable execution sequence.
        Represent it like:
        main.py
            ↓
        process_repo()
            ↓
        chunk_file()
            ↓
        embed_chunks()
            ↓
        store_chunks_in_chroma()
        If multiple execution paths exist, describe each separately.
        If the execution flow cannot be determined with certainty, explain the assumptions made.
        8. Overall Architecture
        Describe whether the repository follows layered, modular, MVC, client-server, microservice, or another architecture.
        Only use the supplied repository information.
        Do not invent files or functions.
"""
    response = llm.invoke(prompt)
    return response.content