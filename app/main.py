from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

from app.api.upload_routes import router as upload_router
from app.api.chat_routes import router as chat_router

app = FastAPI(title="PDF Contextual RAG Assistant")

app.include_router(upload_router)
app.include_router(chat_router)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
