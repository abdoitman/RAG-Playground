# RAG Playground

A simple Retrieval-Augmented Generation (RAG) system using **Ollama** for local LLM inference and **LangChain** for orchestration. Query your documents with an offline AI model.

## Features
- Load and process PDF documents
- Vector similarity search with ChromaDB
- Local LLM inference with Ollama
- LangChain for RAG pipeline
- Chunking with configurable overlap

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running locally
- A model pulled in Ollama (e.g., `ollama pull qwen3.5:9b`)

## Installation

1. Clone or download the project
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the environment:
   - **Windows:** `venv\Scripts\Activate.ps1`
   - **Linux/Mac:** `source venv/bin/activate`

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Build the Vector Database

Place your PDF in the `data/` directory, then run:

```bash
python create_db.py
```

This will:
- Load and split the PDF into chunks
- Generate embeddings
- Store them in ChromaDB (`chroma_db/`)

### 2. Query the RAG System

```bash
python main.py
```

Enter your query and the system will:
- Retrieve relevant document chunks
- Send them to the local Ollama model
- Return an answer based on your documents

## Project Structure

```
RAG-Playground/
├── create_db.py        # Build vector database from PDF
├── main.py             # Query interface
├── playground.ipynb    # Experimental notebook
├── data/               # Place your PDF here
├── chroma_db/          # Vector database (auto-created)
└── requirements.txt    # Dependencies
```

## Configuration

Edit these files to customize:
- **`create_db.py`**: Adjust `chunk_size` and `chunk_overlap` in `RecursiveCharacterTextSplitter`
- **`main.py`**: Change the Ollama model name in `ChatOllama(model="...")`

## Troubleshooting

**Ollama connection error**: Ensure Ollama is running (`ollama serve`)

**Out of memory**: Reduce `chunk_size` or use a smaller model

**Same chunks returned twice**: Reduce `chunk_overlap` value
