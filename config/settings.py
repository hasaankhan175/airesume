"""
Application Configuration

This module contains all configurable settings for the AI Resume Analyzer.
Changing values here updates them throughout the application.
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Project Paths
# ==========================================================

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Data Directory
DATA_DIR = BASE_DIR / "data"

# Resume Dataset
RESUME_DATA_DIR = DATA_DIR / "resumes" / "data"

# Resume CSV Dataset
RESUME_CSV_PATH = DATA_DIR / "resumecsv" / "Resume.csv"

# User Uploads
UPLOAD_DIR = BASE_DIR / "uploads"

# Vector Store
VECTOR_STORE_DIR = BASE_DIR / "vector_store"

# FAISS Files
FAISS_INDEX_PATH = VECTOR_STORE_DIR / "faiss.index"
METADATA_PATH = VECTOR_STORE_DIR / "metadata.pkl"
CHUNKS_PATH = VECTOR_STORE_DIR / "chunks.pkl"

# Assets
ASSETS_DIR = BASE_DIR / "assets"

# Logs
LOG_DIR = BASE_DIR / "logs"

# ==========================================================
# AI Models
# ==========================================================

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Hugging Face Model
LLM_MODEL = "meta-llama/Llama-3.1-8B-Instruct"

# ==========================================================
# Hugging Face API
# ==========================================================

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# ==========================================================
# Text Processing
# ==========================================================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# ==========================================================
# Retrieval
# ==========================================================

TOP_K_RESULTS = 5

# ==========================================================
# Supported File Types
# ==========================================================

SUPPORTED_FILE_TYPES = [
    ".pdf"
]

# ==========================================================
# Streamlit
# ==========================================================

APP_TITLE = "AI Resume Analyzer"

PAGE_ICON = "📄"

# ==========================================================
# Create Required Directories
# ==========================================================

DIRECTORIES = [
    UPLOAD_DIR,
    VECTOR_STORE_DIR,
    LOG_DIR
]

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)