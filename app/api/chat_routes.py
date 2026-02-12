import time

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.core.llm_client import stream_answer
from app.core.retriever import retriever

router = APIRouter()

@router.post("/ask")
async def ask(question: str):

    start_time = time.time()

    docs = retriever.search(question)
    sources = list({doc["file_name"] for doc in docs})

    full_answer = ""
    for chunk in stream_answer(docs, question):
        full_answer += chunk

    end_time = round(time.time() - start_time, 2)

    return JSONResponse({
        "answer": full_answer,
        "sources": sources,
        "response_time": end_time
    })