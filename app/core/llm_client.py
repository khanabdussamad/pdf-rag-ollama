import json

import requests

from app.config import (
    OLLAMA_GENERATE_ENDPOINT,
    LLM_MODEL,
    MAX_TOKENS,
    TEMPERATURE
)


def stream_answer(context_docs, question):
    context = "\n\n".join(
        [f"[{doc['file_name']}] {doc['text']}" for doc in context_docs]
    )

    prompt = f"""
Answer strictly using the context below.
Cite sources in [file_name] format.

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        OLLAMA_GENERATE_ENDPOINT,
        json={
            "model": LLM_MODEL,
            "prompt": prompt,
            "stream": True,
            "options": {
                "num_predict": MAX_TOKENS,
                "temperature": TEMPERATURE
            }
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            if "response" in data:
                yield data["response"]
