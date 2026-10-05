# RAGDemo

A lightweight Retrieval-Augmented Generation (RAG) application that demonstrates how to build a document-grounded AI workflow using LangChain, vector embeddings, and a local Chroma vector store.

This project loads a knowledge base, splits it into chunks, converts the text into embeddings, stores those embeddings in a vector database, and then answers questions using a retrieval-enabled language model.

## Overview

RAG combines the strengths of external knowledge retrieval and large language models:

- The system searches a local knowledge base for the most relevant context
- It passes the retrieved content to an LLM as grounding information
- The model answers based on the retrieved context instead of relying solely on its base training data

This makes the application especially useful for domain-specific documentation, FAQ-style knowledge bases, and internal documentation search and Q&A.

## Features

- Document ingestion from a local Markdown knowledge base
- Text chunking with overlap for better retrieval performance
- Embedding generation using Hugging Face sentence-transformers
- Vector storage with ChromaDB
- Retrieval-based question answering using LangChain
- OpenAI chat model integration for answer generation
- Simple, beginner-friendly architecture suitable for learning and prototyping

## Tech Stack

- Python
- LangChain
- LangChain Classic
- LangChain OpenAI
- Hugging Face Embeddings
- ChromaDB
- OpenAI GPT-3.5 Turbo
- Markdown knowledge source

## Project Structure

```text
RAGDemo/
├── app.py                 # Main RAG pipeline and query flow
├── knowledge_base.md      # Source documentation used for retrieval
├── vectorstore/           # Local Chroma vector database files
├── .env                   # Environment variables (local-only)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Prerequisites

Before running the app, ensure you have:

- Python 3.10+
- An OpenAI API key
- Internet access for model and dependency downloads
- A local environment suitable for installing Python packages

## Installation

1. Clone the repository and navigate into the project directory:

```bash
cd RAGDemo
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root with your OpenAI API key:

```env
API_KEY=your_openai_api_key_here
```

You can also use a `.env.example` pattern if you want to keep local secrets out of version control.

## How It Works

The application performs the following steps:

1. Loads the content from `knowledge_base.md`
2. Splits the content into smaller text chunks
3. Creates embeddings for each chunk using a sentence-transformers model
4. Stores the embeddings in a Chroma vector database
5. Uses a similarity search to find the most relevant chunks for a user question
6. Sends the retrieved context to an LLM through a RetrievalQA chain
7. Returns a grounded answer based on the retrieved knowledge

## Running the Application

Execute the main script:

```bash
python app.py
```

The script currently includes a sample question and outputs the answer generated from the RAG pipeline.

## Example Use Case

This project is ideal for:

- Internal documentation search
- FAQ assistants
- Product knowledge Q&A
- Academic or research document retrieval
- Learning how RAG systems work in practice

## Notes

- The vector store is persisted locally in the `vectorstore/` directory.
- The embedding model and OpenAI model can be adjusted depending on your performance and cost requirements.
- This project is designed as a demonstration and prototype, not as production-ready infrastructure.

## Future Improvements

Potential enhancements include:

- A simple web interface using Streamlit or FastAPI
- Support for multiple knowledge sources
- Metadata filtering and document-level search
- Better prompt engineering and evaluation
- Source citation and answer traceability
- Deployment to a cloud environment

## License

This project is intended for educational and demonstration purposes. Please check the repository owner or organization for the specific licensing terms before using it in production or public-facing environments.

## Contributing

Contributions are welcome. If you are improving the retrieval logic, adding new features, or refining the knowledge base, consider opening a pull request with a clear explanation of the changes and expected impact.
