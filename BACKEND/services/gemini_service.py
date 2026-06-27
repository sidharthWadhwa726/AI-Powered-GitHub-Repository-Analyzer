from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os

load_dotenv()
# for the chat we have to use the chat model 
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite",google_api_key=os.getenv("GOOGLE_API_KEY"))

# by default the chat history is empty 
def generate_answer(question , chunks,architecture_summary, chat_history = []):
    context = "\n\n".join(chunks)
    # print("=" * 50)
    # print("QUESTION:", question)
    # print("CONTEXT:")
    # print(context[:3000])
    # print("=" * 50)
    chat_template = ChatPromptTemplate.from_messages([
        ('system' , """ You are a Github Repository Assistant 
        Answer Only using the repository context 
        if the answer is not present in the repository context , say :
        'I could not find that info in the repository'"""),
        MessagesPlaceholder(variable_name = "chat_history"),
        ('human' , """Repository Architecture:{architecture_summary}
            Relevant Repository Code:{context}
            Question:{question}"""),])
    messages = chat_template.invoke({
        "chat_history" : chat_history,
        "architecture_summary": architecture_summary,
        "context" : context,
        "question" : question }
    )
    response = llm.invoke(messages)
    return response.content 
