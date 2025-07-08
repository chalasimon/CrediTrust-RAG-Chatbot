# CREDITRUST RAG CHATBOT
## Overview

A Retrieval-Augmented Generation (RAG) powered chatbot that transforms customer complaints into actionable insights for financial institutions. This tool helps product managers, support teams, and compliance officers quickly identify emerging issues across multiple financial products.

**Key Features**:
- Natural language querying of complaint databases
- Semantic search across unstructured complaint narratives
- AI-generated insights with source attribution
- Multi-product comparison capabilities
- Intuitive web interface for non-technical users

## Business Problem

CrediTrust Financial receives thousands of customer complaints monthly across:
- Credit Cards
- Personal Loans
- Buy Now, Pay Later (BNPL)
- Savings Accounts
- Money Transfers

This system addresses three critical needs:
1. Reduce complaint trend identification from days to minutes
2. Enable non-technical teams to self-serve insights
3. Shift from reactive to proactive issue resolution

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/chalasimon/CrediTrust-RAG-Chatbot.git
   cd CrediTrust-RAG-Chatbot
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   ### Repository Structure

```bash
.
├── data
│   ├── processed
│   └── raw
├── docs
│   ├── final_report.md
│   └── interim_report.md
├── notebooks
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_embedding_tests.ipynb
├── src
│   ├── embedding
│   │   ├── chunking.py
│   │   ├── embedder.py
│   │   └── vector_db.py
│   ├── preprocessing
│   │   ├── cleaner.py
│   │   └── filter.py
│   ├── retrieval
│   │   ├── generator.py
│   │   ├── prompts.py
│   │   └── retriever.py
│   └── ui
│       ├── app.py
│       └── components.py
└── vector_store
    ├── chroma_db
    └── faiss_index