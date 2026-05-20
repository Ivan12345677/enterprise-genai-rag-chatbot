from fastapi import FastAPI
from pydantic import BaseModel

from chatbot import create_chat_chain

# Initialize FastAPI app
app = FastAPI()

# Load chatbot chain once during startup
chat_chain = create_chat_chain()

# Request body schema
class ChatRequest(BaseModel):
    question: str

# Health check endpoint
@app.get("/")
def home():
    return {"message": "Enterprise GenAI API Running"}

# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):

    try:
        response = chat_chain.invoke({
            "question": request.question
        })

        answer = response["answer"]

        sources = []

        for doc in response["source_documents"]:
            sources.append(doc.metadata.get("source", "Unknown"))

        return {
            "question": request.question,
            "answer": answer,
            "sources": list(set(sources))
        }

    except Exception as e:
        return {
            "error": str(e)
        }