from langchain_core.messages import HumanMessage, AIMessage
chat_sessions = {}
def get_history(session_id):
    return chat_sessions.get(session_id, [])

def add_message(session_id, question, answer):
    if session_id not in chat_sessions:
        chat_sessions[session_id] = []
    chat_sessions[session_id].append(HumanMessage(content=question))
    chat_sessions[session_id].append(AIMessage(content=answer))

    