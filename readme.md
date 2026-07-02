# 🤖 AI Resume Analyzer (RAG-Based ATS System)

An AI-powered Resume Analyzer that evaluates resumes against job descriptions using **Retrieval-Augmented Generation (RAG)**, **FAISS Vector Database**, **Sentence Transformers**, and **Large Language Models (LLMs)**. The application calculates an ATS (Applicant Tracking System) score, retrieves similar resumes from a knowledge base, and generates detailed AI-powered feedback to help candidates improve their resumes.

---

# 🚀 Features

- 📄 Upload Resume (PDF)
- 💼 Paste Job Description
- 🤖 AI-powered Resume Analysis
- 🎯 ATS Score Calculation
- 📊 Score Breakdown
- 🔍 Resume Retrieval using FAISS
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Knowledge Base built from 2,484 resumes
- 📈 Skill Matching
- ❌ Missing Skills Detection
- 💡 Resume Improvement Suggestions
- 📑 Download Analysis Report
- 🌐 Interactive Streamlit Web Application

---

# 🏗️ Project Architecture

```
                Resume PDF
                     │
                     ▼
              PDF Text Extraction
                     │
                     ▼
               Text Cleaning
                     │
                     ▼
              ATS Score Engine
                     │
                     ▼
              Resume Embedding
                     │
                     ▼
              FAISS Retrieval
                     │
                     ▼
         Similar Resume Chunks
                     │
                     ▼
          Prompt Construction
                     │
                     ▼
         Hugging Face LLM
                     │
                     ▼
      AI Resume Analysis Report
                     │
                     ▼
             Streamlit Dashboard
```

---

# 🛠 Tech Stack

## Programming Language

- Python 3.11+

## Frontend

- Streamlit

## AI / NLP

- Hugging Face Inference API
- Meta Llama 3.1 Instruct
- Sentence Transformers

## Retrieval

- FAISS Vector Database

## PDF Processing

- PyMuPDF (fitz)

## Data Processing

- Pandas
- NumPy

---

# 📂 Dataset

This project uses the Resume Dataset containing **2,484 resumes** across multiple professional domains.

Examples include:

- Accounting
- Engineering
- Information Technology
- HR
- Healthcare
- Banking
- Agriculture
- Aviation
- Construction
- Sales
- Business Development
- Teacher
- Designer
- Finance
- Consultant
- and many more.

---

# 📊 Dataset Statistics

| Item | Value |
|------|------:|
| Total Resumes | 2,484 |
| Categories | 24 |
| Total Chunks | 36,786 |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database | FAISS |

---

# ⚙️ Project Structure

```
AIResumeAnalyzer/

│
├── app.py
│
├── config/
│   └── settings.py
│
├── data/
│   ├── resumes/
│   └── resumecsv/
│
├── models/
│   ├── embedding_model.py
│   └── llm.py
│
├── prompts/
│   └── ats_prompt.py
│
├── services/
│   ├── analyzer.py
│   ├── ats_scorer.py
│   ├── chunker.py
│   ├── pdf_loader.py
│   ├── retriever.py
│   ├── text_cleaner.py
│   └── vector_store.py
│
├── vector_db/
│
├── build_index.py
│
├── requirements.txt
│
└── README.md
```

---

# 🔄 Workflow

## Step 1

Upload a Resume (PDF)

↓

## Step 2

Extract text using PyMuPDF

↓

## Step 3

Clean and preprocess the resume

↓

## Step 4

Calculate ATS score

↓

## Step 5

Generate embedding

↓

## Step 6

Retrieve similar resume chunks from FAISS

↓

## Step 7

Build RAG prompt

↓

## Step 8

Generate AI analysis using Hugging Face LLM

↓

## Step 9

Display results in Streamlit

---

# 🎯 ATS Scoring

The ATS Score is calculated using a weighted scoring approach.

| Component | Weight |
|-----------|--------:|
| Skills Match | 35% |
| Keyword Match | 20% |
| Experience | 20% |
| Education | 10% |
| Projects | 10% |
| Certifications | 5% |

Total Score = **100**

---

# 🧠 Retrieval-Augmented Generation (RAG)

Instead of asking the language model directly, the system first retrieves relevant resume examples from a FAISS vector database.

The retrieved context is then combined with:

- Candidate Resume
- Job Description

This enables the language model to generate more context-aware, relevant, and accurate resume feedback.

---

# 📋 AI Analysis Includes

- ATS Score
- Resume Summary
- Strengths
- Weaknesses
- Matched Skills
- Missing Skills
- Missing Keywords
- Experience Analysis
- Education Analysis
- Project Analysis
- Resume Improvement Suggestions
- Final Hiring Recommendation

---

# 🌐 Streamlit Dashboard

The web application provides:

- Resume Upload
- Job Description Input
- ATS Dashboard
- AI Resume Analysis
- Downloadable Report

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AIResumeAnalyzer.git

cd AIResumeAnalyzer
```

Create a Conda environment:

```bash
conda create -n resume-rag python=3.11

conda activate resume-rag
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Build the FAISS index:

```bash
python build_index.py
```

Launch the Streamlit app:

```bash
streamlit run app.py
```

---

# 📈 Future Improvements

- Resume Rewriter
- Cover Letter Generator
- Interview Question Generator
- Resume Ranking
- Recruiter Dashboard
- PDF Report Export
- Multi-Resume Comparison
- Job Recommendation Engine
- Docker Deployment
- Cloud Deployment

---

# 💡 Learning Outcomes

Through this project, I gained hands-on experience with:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases (FAISS)
- Sentence Embeddings
- Hugging Face Inference API
- Prompt Engineering
- Resume Parsing
- ATS Scoring Systems
- PDF Processing
- Streamlit Application Development
- End-to-End AI Application Development

---

# 📄 License

This project is intended for educational and portfolio purposes.

---

# 👨‍💻 Author

**Hasaan**

AI | Data Science | Machine Learning | NLP | Generative AI

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!