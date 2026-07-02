from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import FRONTEND_URL
from app.schemas import ChatRequest, ChatResponse
from app.services.gemini_service import ask_gemini

app = FastAPI(title="ARZOPA Z1FC RAG Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL, "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = ask_gemini(request.message)
    return ChatResponse(answer=answer)