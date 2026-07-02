# ARZOPA Z1FC AI Chatbot API

AI Chatbot sử dụng **FastAPI**, **Gemini 2.5 Flash** và **FAISS RAG** để tư vấn sản phẩm **ARZOPA Z1FC Portable Monitor**.

Chatbot được xây dựng để tích hợp vào Landing Page, giúp người dùng đặt câu hỏi về sản phẩm và nhận được câu trả lời dựa trên dữ liệu đã được embedding.

---

# ✨ Features

* 🤖 AI Chatbot với Gemini 2.5 Flash
* 📚 RAG (Retrieval Augmented Generation)
* 🔍 Vector Search bằng FAISS
* 📄 Knowledge Base dạng Markdown
* ⚡ FastAPI REST API
* 🌐 Hỗ trợ CORS cho Landing Page
* 🚀 Sẵn sàng deploy trên Render

---

# Tech Stack

* Python 3.11+
* FastAPI
* Google Gemini 2.5 Flash
* Google Gemini Embedding
* FAISS
* NumPy
* Pydantic

---

# Project Structure

```text
.
├── app/
│   ├── config.py
│   ├── main.py
│   ├── schemas.py
│   ├── data/
│   └── services/
│       ├── embedding_service.py
│       ├── gemini_service.py
│       └── rag_service.py
│
├── vector_store/
│   ├── arzopa.index
│   └── documents.json
│
├── build_index.py
├── requirements.txt
├── .env
└── README.md
```

---

# Installation

Clone project

```bash
git clone https://github.com/delvintrung/z1fc_chatbot.git

cd z1fc-rag
```

Create virtual environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY

FRONTEND_URL=http://localhost:5173
```

---

# Build Vector Database

Sau khi thêm các file Markdown vào thư mục:

```text
app/data/
```

Chạy:

```bash
python build_index.py
```

Lệnh trên sẽ sinh:

```text
vector_store/

arzopa.index

documents.json
```

---

# Run API

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

# API

## Health Check

GET

```
/
```

Response

```json
{
    "status":"ok"
}
```

---

## Chat

POST

```
/chat
```

Request

```json
{
    "message":"Màn hình này có phù hợp cho lập trình không?"
}
```

Response

```json
{
    "answer":"Có. ARZOPA Z1FC rất phù hợp..."
}
```

---

# Knowledge Base

Dữ liệu RAG được lưu trong

```text
app/data/
```

Bao gồm:

* overview.md
* specifications.md
* features.md
* compatibility.md
* connectivity.md
* package_contents.md
* use_cases.md
* advantages.md
* faq.md
* troubleshooting.md
* warranty.md
* buying_guide.md
* limitations.md
* conversation_rules.md
* company_policy.md

---

# RAG Workflow

```text
User Question

↓

Embedding

↓

FAISS Similarity Search

↓

Retrieve Top Documents

↓

Gemini 2.5 Flash

↓

Answer
```

---

# Deploy

Project có thể deploy trực tiếp lên

* Render
* Railway
* Google Cloud Run

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

# Notes

* Vector Database được build trước bằng `build_index.py`.
* Không nên build lại vector mỗi lần deploy.
* Chỉ cần commit thư mục `vector_store/` lên GitHub.

---

# Future Improvements

* Conversation History
* Streaming Response
* Multi-product RAG
* Hybrid Search (BM25 + Vector)
* Feedback System
* Admin Dashboard
* Citation nguồn trả lời
* Redis Cache
* PostgreSQL lưu lịch sử chat

---

# License

This project is developed for educational purposes and as part of a technical assessment.
