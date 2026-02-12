# PDF Contextual RAG Assistant

An enterprise-grade Multi-Document Retrieval-Augmented Generation (RAG)
Assistant built using FastAPI and Ollama.

This application enables contextual question answering across multiple
uploaded PDF documents with source attribution, response time tracking,
and a modern assistant-style interface.

------------------------------------------------------------------------

## 🚀 Features

-   Multi-file PDF upload
-   Secure PDF validation (frontend + backend)
-   Async file handling
-   Intelligent document chunking
-   TF-IDF retrieval engine
-   Citation-aware answer generation
-   Response time display
-   Document removal
-   Clear chat functionality
-   Modern enterprise UI
-   Modular production-grade backend
-   Config-driven architecture

------------------------------------------------------------------------

## 🏗 Architecture Overview

Frontend (Bootstrap UI) ↓ FastAPI API Layer ↓ Document Processing
Layer - PDF Parsing - Text Chunking

Retrieval Layer - TF-IDF Vectorization - Similarity Ranking

LLM Layer - Ollama Runtime - Context-Grounded Generation

------------------------------------------------------------------------

## 📂 Project Structure

app/ │ ├── main.py ├── config.py │ ├── api/ │ ├── upload_routes.py │ └──
chat_routes.py │ ├── core/ │ ├── document_processor.py │ ├──
retriever.py │ └── llm_client.py │ └── templates/ └── index.html

------------------------------------------------------------------------

## ⚙️ Technology Stack

Backend: FastAPI\
Retrieval: scikit-learn (TF-IDF)\
LLM Runtime: Ollama\
PDF Parsing: pypdf\
Async IO: aiofiles\
Frontend: Bootstrap 5

------------------------------------------------------------------------

## 📦 Installation

1.  Clone Repository

git clone
https://github.com/yourusername/pdf-contextual-rag-assistant.git\
cd pdf-contextual-rag-assistant

2.  Create Virtual Environment

python -m venv venv

Activate:

Windows\
venv`\Scripts`{=tex}`\activate  `{=tex}

Mac/Linux\
source venv/bin/activate

3.  Install Dependencies

pip install -r requirements.txt

4.  Install and Run Ollama

Download from: https://ollama.com

Pull model:

ollama pull phi3:mini

Start server:

ollama serve

5.  Run Application

uvicorn app.main:app --reload

Open in browser:

http://127.0.0.1:8000

------------------------------------------------------------------------

## 🔧 Configuration

Configured via config.py:

LLM_MODEL = "phi3:mini"\
TOP_K = 2\
CHUNK_SIZE = 300\
MAX_TOKENS = 150\
TEMPERATURE = 0

Environment variables can override defaults.

------------------------------------------------------------------------

## 🔒 Security Controls

-   PDF-only upload enforcement
-   MIME type validation
-   Asynchronous chunked file writing
-   Controlled prompt construction

------------------------------------------------------------------------

## 📈 Future Enhancements

-   Hybrid Retrieval (TF-IDF + Embeddings)
-   Persistent vector storage
-   Streaming token responses
-   Docker containerization
-   Cloud deployment

------------------------------------------------------------------------

## 🏷 License

MIT License

------------------------------------------------------------------------

PDF Contextual RAG Assistant\
Enterprise-ready contextual document intelligence.
