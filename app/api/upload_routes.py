import asyncio
import os
from typing import List

import aiofiles
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi import Body

from app.config import DATA_DIR
from app.core.document_processor import extract_text, chunk_text
from app.core.retriever import retriever

router = APIRouter()

@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):

    os.makedirs(DATA_DIR, exist_ok=True)
    results = []

    for file in files:

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files allowed")

        file_path = os.path.join(DATA_DIR, file.filename)

        async with aiofiles.open(file_path, "wb") as out_file:
            while content := await file.read(1024):
                await out_file.write(content)

        text = await asyncio.to_thread(extract_text, file_path)
        chunks = chunk_text(text)

        retriever.add_document(chunks, file.filename)

        results.append({
            "file_name": file.filename,
            "status": "Indexed"
        })

    return {"files": results}

@router.delete("/remove")
async def remove_document(file_name: str = Body(...)):
    retriever.remove_document(file_name)
    return {"message": f"{file_name} removed successfully"}
