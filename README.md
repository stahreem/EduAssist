# 📚 EduAssist: A Multilingual AI Learning Assistant

## Overview

EduAssist is an AI-powered multilingual learning assistant designed to help students understand educational documents more efficiently. The application allows users to upload PDF documents and automatically generates concise summaries, important keywords, quizzes, flashcards, and multilingual translations using local Large Language Models (LLMs).

Unlike many cloud-based AI tools, EduAssist is designed to work with **local AI models through Ollama**, ensuring better privacy, offline capability, and zero API costs.

---

# Features

### 📄 PDF Processing

- Upload PDF documents
- Extract text using pdfplumber
- Automatic language detection
- Text preprocessing using spaCy

---

### 🤖 AI Summarization

- Chunk-based document summarization
- Intelligent summary merging
- Educational prompt engineering
- Local LLM inference using Qwen

---

### 🔑 Keyword Extraction

- KeyBERT-based keyword extraction
- Dynamic keyword count based on document length
- Duplicate keyword removal

---

### 📝 Quiz Generation

Automatically generates multiple-choice questions from the AI-generated summary.

Features:

- 5 educational MCQs
- Four options per question
- Automatic answer checking
- Translation support

---

### 🃏 Flashcards

Automatically creates study flashcards from the generated summary.

Features:

- Question–Answer format
- Educational prompt engineering
- Translation support

---

### 🌍 Multilingual Translation

Translate generated content into multiple languages.

Currently Supported:

- Hindi
- Telugu
- Urdu
- Tamil
- Kannada
- Malayalam
- French
- German
- Spanish
- Arabic
- Japanese

---

## Current Project Architecture

```
EduAssist
│
├── app/
├── config/
├── core/
├── preprocessing/
├── summarization/
├── keywords/
├── quiz/
├── flashcards/
├── translation/
├── models/
├── evaluation/
├── exports/
├── rag/
├── ui/
├── utils/
├── tests/
└── README.md
```

---

# Workflow

```
Upload PDF
      │
      ▼
Text Extraction
      │
      ▼
Language Detection
      │
      ▼
Text Cleaning
      │
      ▼
Document Chunking
      │
      ▼
Local LLM (Qwen via Ollama)
      │
      ▼
Summary Generation
      │
      ├───────────────┐
      ▼               ▼
Keyword         Flashcards
Extraction
      │               │
      ▼               ▼
Quiz          Translation
Generation
```

---

# Technologies Used

## Programming Language

- Python 3.13

---

## Frontend

- Streamlit

---

## NLP

- spaCy
- LangDetect
- KeyBERT

---

## Local AI

- Ollama
- Qwen 3 (1.7B)

---

## PDF Processing

- pdfplumber

---

## Machine Learning

- Sentence Transformers
- Scikit-Learn

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/EduAssist.git
```

Move into the project

```bash
cd EduAssist
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install spaCy model

```bash
python -m spacy download en_core_web_sm
```

Install Ollama

Download from:

https://ollama.com/

Pull the Qwen model

```bash
ollama pull qwen3:1.7b
```

Run the application

```bash
streamlit run app/app.py
```

---

# Current Features

- PDF Upload
- PDF Text Extraction
- Language Detection
- Text Cleaning
- Chunk-based Summarization
- Summary Merging
- Keyword Extraction
- Quiz Generation
- Flashcard Generation
- Translation
- Modular UI
- Session Management

---

# Future Work

The following features are planned:

- OCR support for scanned PDFs
- Mind Map generation
- Retrieval-Augmented Generation (RAG)
- AI Chat with uploaded documents
- PDF export
- DOCX export
- ROUGE Evaluation
- BERTScore Evaluation
- LLM-as-a-Judge Evaluation
- Semantic Search
- Citation Generation
- Multi-document summarization

---

# Evaluation Metrics (Planned)

- Compression Ratio
- Reading Time Reduction
- ROUGE Score
- BERTScore
- Keyword Precision
- LLM Evaluation
- Response Time

---

# Advantages

- Works completely offline
- No API costs
- Privacy-friendly
- Modular architecture
- Easy to extend
- Educational prompt engineering
- Supports multilingual learning

---

# License

This project is intended for educational and research purposes.

---

# Author

**Shifa Tahreem**

M.Tech Artificial Intelligence & Machine Learning

EduAssist – A Multilingual AI Learning Assistant
