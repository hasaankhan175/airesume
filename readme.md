# AI Resume Analyzer using RAG – Project Specification

## Project Overview

The goal of this project is to build a **production-ready AI Resume Analyzer** using **Retrieval-Augmented Generation (RAG)**. The application will allow users to upload their resumes and compare them against a job description using semantic search, embeddings, and a Large Language Model (LLM).

The project is designed to demonstrate practical skills in:

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Vector Databases
* Embeddings
* Prompt Engineering
* Streamlit Development
* Production-ready Python Architecture
* Document Processing
* AI Application Development

---

# Technology Stack

## Frontend

* Streamlit

## Backend

* Python 3.11

## LLM

* Hugging Face Inference API (Free Tier)

### Recommended Models

* Qwen/Qwen2.5-7B-Instruct (Primary)
* Mistral-7B-Instruct-v0.3 (Fallback)
* Phi-3 Mini (Optional)

---

## Embedding Model

sentence-transformers/all-MiniLM-L6-v2

---

## Vector Database

FAISS

---

## PDF Processing

PyMuPDF

---

## Framework

LangChain

---

# Data Source

Knowledge Base

Use the complete dataset of **2,484 resumes** stored as PDF files.

Dataset Location

D:\airesume\data\resumes\data

Each category contains multiple PDF resumes, for example:

ADVOCATE/
CHEF/
ENGINEERING/
ACCOUNTANT/
HR/
...

The CSV dataset located at:

D:\airesume\data\resumecsv

will be used only for validation, experimentation, or future model improvements.

---

# User Workflow

1. User uploads their own Resume (PDF).
2. User provides a Job Description using either:

   * Text input
   * PDF upload
3. The application extracts text from the uploaded resume.
4. Resume text is cleaned and split into semantic chunks.
5. Chunks are converted into embeddings.
6. Relevant chunks are stored and retrieved using FAISS.
7. The LLM analyzes the retrieved resume content against the job description.
8. Results are displayed in the Streamlit application.

---

# Features

## Resume Summary

Generate a concise professional summary of the candidate.

---

## ATS Score

Generate an ATS score between 0–100.

The ATS score should be based on:

* Keyword Match
* Skill Match
* Experience Match
* Education Match
* Semantic Similarity

A hybrid approach will be used:

* Rule-based scoring for transparency.
* LLM-generated analysis for qualitative feedback.

---

## Skill Match Analysis

Display:

Matching Skills

Missing Skills

Suggested Skills

---

## Resume Feedback

Analyze:

* Resume Structure
* Formatting
* Experience
* Projects
* Technical Skills
* Soft Skills

Provide improvement suggestions.

---

## Keyword Analysis

Highlight:

* Present Keywords
* Missing Keywords
* Important Recruiter Keywords

---

## Interview Question Generator

Generate personalized interview questions based on:

* Resume
* Job Description

---

## Cover Letter Generator (Bonus)

Generate a professional cover letter using:

* Resume
* Job Description

---

## Download Report

Allow users to download the analysis as:

* PDF
* DOCX

---

# RAG Pipeline

User Resume PDF

↓

Text Extraction

↓

Cleaning

↓

Chunking

↓

Embeddings

↓

FAISS Vector Database

↓

Retriever

↓

Relevant Resume Chunks

↓

Prompt Template

↓

Hugging Face LLM

↓

Analysis

↓

Results

---

# Project Architecture

The project will follow a production-ready modular architecture with separate modules for:

* Configuration
* Logging
* Exception Handling
* Data Loading
* PDF Parsing
* Text Preprocessing
* Embedding Generation
* Vector Store Management
* Retrieval
* Prompt Templates
* LLM Integration
* Resume Analysis
* ATS Scoring
* Utilities
* Streamlit UI

This structure will make the project scalable, maintainable, and suitable for a professional GitHub portfolio.

---

# Dataset Strategy

The application will use **all 2,484 PDF resumes** to build the FAISS vector index.

Each resume will:

* Be parsed from PDF.
* Be cleaned.
* Be split into chunks.
* Be embedded using sentence-transformers/all-MiniLM-L6-v2.
* Be indexed in FAISS.

The vector database will be created once and reused by the application for fast retrieval.

---

# Future Enhancements

* Multiple embedding model selection.
* Resume version comparison.
* Recruiter dashboard.
* Batch resume analysis.
* Resume ranking against multiple job descriptions.
* MLOps pipeline for automated indexing.
* Docker deployment.
* Cloud deployment on Hugging Face Spaces or Streamlit Community Cloud.

---

# Expected Learning Outcomes

By completing this project, the following skills will be demonstrated:

* Python Development
* Streamlit Application Development
* Retrieval-Augmented Generation (RAG)
* LangChain
* Hugging Face Inference API
* Embedding Models
* FAISS Vector Search
* Prompt Engineering
* PDF Processing
* NLP Preprocessing
* AI System Design
* Modular Software Architecture
* Production-ready Project Organization
* Git & GitHub Best Practices



# AI Resume Analyzer (RAG) - Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py                          # Main Streamlit application
├── build_index.py                  # Build FAISS index from all PDFs
├── requirements.txt                # Project dependencies
├── .env                            # Hugging Face API key
├── .gitignore
├── README.md
│
├── config/
│   ├── __init__.py
│   ├── settings.py                 # Paths, constants, model names
│   └── logging_config.py           # Logging configuration
│
├── data/
│   ├── resumecsv/
│   │   └── Resume.csv
│   │
│   └── resumes/
│       └── data/
│           ├── ACCOUNTANT/
│           ├── ADVOCATE/
│           ├── ...
│
├── uploads/                        # User uploaded resumes & JDs
│
├── vector_store/
│   ├── faiss.index
│   ├── metadata.pkl
│   └── chunks.pkl
│
├── models/
│   ├── __init__.py
│   ├── embedding_model.py          # Load embedding model
│   ├── llm.py                      # Hugging Face API wrapper
│   └── prompt_templates.py         # All prompts
│
├── services/
│   ├── __init__.py
│   ├── pdf_loader.py               # Read PDF files
│   ├── text_cleaner.py             # Clean extracted text
│   ├── chunker.py                  # Split text into chunks
│   ├── vector_store.py             # Save/load FAISS index
│   ├── retriever.py                # Retrieve relevant chunks
│   ├── ats_scorer.py               # Rule-based ATS scoring
│   ├── analyzer.py                 # Main resume analysis pipeline
│   ├── keyword_matcher.py          # Keyword extraction & matching
│   ├── skill_matcher.py            # Skill comparison
│   ├── report_generator.py         # PDF/DOCX report generation
│   └── job_description_parser.py   # Parse JD text/PDF
│
├── utils/
│   ├── __init__.py
│   ├── helpers.py                  # Common helper functions
│   ├── file_handler.py             # File saving/loading
│   ├── validators.py               # Input validation
│   └── logger.py                   # Logger utility
│
├── assets/
│   ├── logo.png
│   └── style.css
│
├── notebooks/
│   ├── data_exploration.ipynb
│   └── embedding_experiments.ipynb
│
└── tests/
    ├── test_pdf_loader.py
    ├── test_chunker.py
    ├── test_embeddings.py
    ├── test_vector_store.py
    └── test_analyzer.py
```

# File Responsibilities

### Root Files

* `app.py` → Streamlit user interface.
* `build_index.py` → Reads all 2,484 PDFs, creates embeddings, and saves the FAISS index.
* `requirements.txt` → Python dependencies.
* `.env` → Hugging Face API key.
* `README.md` → Project documentation.

---

### config/

Stores all configuration values.

* `settings.py`

  * Dataset paths
  * Upload folder
  * Model names
  * Chunk size
  * Chunk overlap
  * API settings
* `logging_config.py`

  * Configure application logging.

---

### models/

Contains AI model initialization.

* `embedding_model.py`

  * Loads the SentenceTransformer embedding model.
* `llm.py`

  * Connects to the Hugging Face Inference API.
* `prompt_templates.py`

  * Stores prompts for:

    * ATS analysis
    * Resume summary
    * Skill analysis
    * Interview questions
    * Cover letter

---

### services/

Core business logic.

* `pdf_loader.py`

  * Extract text from PDFs using PyMuPDF.
* `text_cleaner.py`

  * Remove unnecessary spaces, symbols, and formatting.
* `chunker.py`

  * Split text into overlapping chunks.
* `vector_store.py`

  * Create, save, and load the FAISS index.
* `retriever.py`

  * Retrieve the most relevant chunks.
* `ats_scorer.py`

  * Calculate rule-based ATS score.
* `keyword_matcher.py`

  * Compare keywords between resume and job description.
* `skill_matcher.py`

  * Match technical and soft skills.
* `job_description_parser.py`

  * Parse text or PDF job descriptions.
* `analyzer.py`

  * Orchestrates the entire RAG pipeline.
* `report_generator.py`

  * Export analysis as PDF or DOCX.

---

### utils/

Reusable helper functions.

* `helpers.py`
* `file_handler.py`
* `validators.py`
* `logger.py`

---

### vector_store/

Stores generated vector data.

* `faiss.index`
* `metadata.pkl`
* `chunks.pkl`

These files are generated automatically after running `build_index.py`.

---

### tests/

Contains unit tests for major modules to ensure reliability and maintainability.
