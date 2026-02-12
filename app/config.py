import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "..", "data")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_GENERATE_ENDPOINT = f"{OLLAMA_BASE_URL}/api/generate"

LLM_MODEL = os.getenv("LLM_MODEL", "phi3:mini")

TOP_K = int(os.getenv("TOP_K", 2))
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 250))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))

MAX_TOKENS = int(os.getenv("MAX_TOKENS", 150))
TEMPERATURE = float(os.getenv("TEMPERATURE", 0))
