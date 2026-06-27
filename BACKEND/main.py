from fastapi import FastAPI
from routes.ingest import router as ingest_route
from routes.chat_route import router as chat_with_repo
app = FastAPI(title="Github RAG API")

app.include_router(ingest_route)
app.include_router(chat_with_repo)

@app.get("/")
def home():
    return {"message": "GitHub RAG Backend Running"}

