# AI Development Knowledge Base
Version: 1.0
Purpose: Retrieval-Augmented Generation (RAG) knowledge source
Domain: AI Development, LLMs, Embeddings, Vector Databases, and RAG

---

## 1. Artificial Intelligence

Artificial Intelligence (AI) is the field of computer science focused on building systems that can perform tasks that normally require human intelligence.

Common AI capabilities include:
- Understanding natural language
- Recognizing images and speech
- Making predictions
- Reasoning over information
- Recommending actions
- Generating text, images, audio, and code

Machine learning is a subset of AI in which systems learn patterns from data rather than relying entirely on explicitly programmed rules.

Deep learning is a subset of machine learning that uses neural networks with multiple layers to learn complex patterns.

---

## 2. Generative AI

Generative AI refers to AI systems that can create new content based on patterns learned during training.

Examples include:
- Text
- Code
- Images
- Audio
- Video
- Structured data

Large Language Models (LLMs) are a major category of generative AI systems designed primarily for working with language.

A generative AI application normally consists of a model plus application logic, data sources, tools, prompts, and safety controls.

---

## 3. Large Language Models

A Large Language Model (LLM) is a neural-network model trained on large amounts of data to understand and generate language.

LLMs are commonly used for:
- Question answering
- Summarization
- Translation
- Code generation
- Classification
- Information extraction
- Conversational assistants
- Content generation

An LLM does not automatically know a company's private database or current internal information. Applications can provide that information through RAG, tools, APIs, or other external data sources.

---

## 4. Tokens

A token is a unit of text processed by an LLM.

A token may represent a complete word, part of a word, punctuation, a symbol, or a short sequence of characters.

LLMs have context windows that limit how much information can be processed in one request.

Token limits affect prompt size, retrieved document size, conversation history, output length, cost, and latency.

Good RAG systems retrieve only the most relevant information instead of sending an entire knowledge base to the model.

---

## 5. Transformer Architecture

The Transformer is a neural-network architecture introduced in the 2017 research paper "Attention Is All You Need."

Transformers became important because they use attention mechanisms to model relationships between tokens efficiently.

A simplified workflow is:

Input text -> Tokenization -> Embeddings -> Attention layers -> Feed-forward layers -> Output probabilities

Attention allows the model to determine which tokens are important in relation to other tokens.

---

## 6. Attention

Attention is a mechanism that allows a neural network to assign different importance to different parts of an input.

Self-attention allows each token to consider other tokens in the same sequence.

A simplified attention mechanism uses:
- Query
- Key
- Value

The simplified attention equation is:

Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V

Multi-head attention performs several attention operations in parallel so the model can learn different relationships.

---

## 7. Prompt Engineering

Prompt engineering is the practice of designing instructions and context that guide an AI model toward useful and reliable outputs.

A strong prompt can define:
- Role
- Task
- Context
- Constraints
- Expected output format
- Examples
- Evaluation criteria

Example:

"You are a technical instructor. Explain Retrieval-Augmented Generation to a beginner using a simple example. Use no more than 300 words."

In RAG, the prompt normally contains the user's question plus retrieved context.

---

## 8. Embeddings

An embedding is a numerical representation of data that captures semantic meaning.

Example:

"The customer wants to reset a password."

can be converted into a numerical vector such as:

[0.12, -0.44, 0.83, ...]

The actual vector normally contains many dimensions.

Semantically similar texts tend to have vectors that are close together according to an appropriate similarity metric.

Embeddings are commonly used for:
- Semantic search
- RAG
- Recommendation systems
- Document clustering
- Duplicate detection
- Classification

An embedding model is different from a generative LLM. An embedding model converts content into vectors, while a generative model produces content.

---

## 9. Vector Similarity

Vector similarity measures how closely two embeddings relate to each other.

Common similarity methods include:
- Cosine similarity
- Dot product
- Euclidean distance

Cosine similarity measures the angle between vectors.

Cosine similarity = (A · B) / (||A|| ||B||)

A higher cosine similarity generally means the vectors are more semantically similar when the embedding model is designed for cosine similarity.

---

## 10. Vector Databases

A vector database stores and searches numerical embeddings efficiently.

Examples include:
- FAISS
- Pinecone
- Qdrant
- Weaviate
- Milvus
- Chroma
- pgvector with PostgreSQL

A vector store typically contains:
- Vector embeddings
- Document text or references
- Metadata
- Identifiers

A search request converts the user's question into an embedding and searches for vectors that are semantically similar.

---

## 11. FAISS

FAISS stands for Facebook AI Similarity Search.

FAISS is a library for efficient similarity search and clustering of dense vectors.

FAISS can be used to build a local vector index for RAG applications.

A simplified workflow is:

1. Load documents.
2. Split documents into chunks.
3. Generate embeddings for chunks.
4. Store embeddings in a FAISS index.
5. Convert the user's question into an embedding.
6. Search the FAISS index.
7. Retrieve the most similar chunks.
8. Send retrieved context to an LLM.
9. Generate an answer based on the retrieved context.

FAISS is primarily a vector similarity-search library. It is not a complete hosted database service.

---

## 12. Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) is an architecture that combines information retrieval with generative AI.

The purpose of RAG is to allow an LLM to answer questions using external knowledge.

A basic RAG pipeline is:

Documents
-> Document loading
-> Text extraction
-> Chunking
-> Embedding generation
-> Vector storage
-> User question
-> Query embedding
-> Similarity search
-> Relevant chunks
-> Prompt construction
-> LLM
-> Answer

RAG is useful when information is:
- Private
- Domain-specific
- Frequently updated
- Too large to include directly in a prompt
- Not reliably known by the base model

---

## 13. RAG Ingestion Pipeline

The ingestion pipeline prepares documents before users ask questions.

### Step 1: Load documents

Documents can come from PDF files, Word documents, Markdown files, HTML pages, databases, APIs, or internal company systems.

### Step 2: Clean text

Remove unnecessary formatting, repeated headers, navigation text, and other noise.

### Step 3: Chunk text

Split long documents into smaller sections.

### Step 4: Generate embeddings

Convert each chunk into a vector using an embedding model.

### Step 5: Store vectors

Save vectors and metadata in a vector store.

The result is a searchable knowledge base.

---

## 14. Document Chunking

Chunking means dividing a large document into smaller pieces before embedding.

Chunking is important because extremely large chunks may contain multiple unrelated concepts, while extremely small chunks may lose important context.

Common strategies include:
- Fixed-size chunking
- Recursive character chunking
- Sentence-based chunking
- Paragraph-based chunking
- Semantic chunking
- Structure-aware chunking

A useful chunk should ideally represent one coherent topic.

Overlap can be used between chunks so information near boundaries is not lost.

---

## 15. Metadata

Metadata is information stored alongside a document chunk.

Useful metadata includes:
- Document ID
- File name
- Page number
- Section title
- Author
- Date
- Product
- Department
- Source URL
- Document type

Metadata enables filtering and access control.

For example, a system can combine semantic search with metadata filtering to find customer-support documents about refunds created after a particular date.

---

## 16. Retrieval

Retrieval is the process of finding relevant information from a knowledge base.

A basic retrieval process is:

User question
-> Query embedding
-> Vector similarity search
-> Top-K results
-> Retrieved context

Top-K means the system retrieves the K most relevant results.

Retrieving too few chunks can omit important information. Retrieving too many can introduce noise and increase prompt size.

---

## 17. Hybrid Search

Hybrid search combines multiple retrieval techniques.

A common approach combines:
- Keyword search
- Semantic vector search

Keyword search is useful for exact terms such as product IDs, error codes, names, and technical identifiers.

Vector search is useful for semantic concepts and paraphrases.

Hybrid retrieval can improve recall when either keyword or semantic search alone is insufficient.

---

## 18. Reranking

Reranking is a second-stage process used to improve the ordering of retrieved documents.

A typical pipeline is:

Query
-> Initial retrieval
-> Top 20 candidates
-> Reranker
-> Best 5 chunks
-> LLM

The initial retriever prioritizes speed and recall.

The reranker evaluates the relationship between the query and candidate documents more carefully.

Reranking can improve answer quality when the initial vector search returns several similar but differently relevant documents.

---

## 19. RAG Prompt

A RAG prompt usually contains:
1. System instructions
2. User question
3. Retrieved context
4. Rules for using the context

Example:

```text
You are an AI assistant.

Answer the user's question using only the provided context.

If the answer is not present in the context, say that the information is not available.

Context:
{retrieved_documents}

Question:
{user_question}
```

This approach can reduce unsupported answers.

---

## 20. Hallucination

A hallucination occurs when an AI model produces information that is incorrect, unsupported, or fabricated.

RAG can reduce hallucination by providing relevant source material, but RAG does not guarantee factual accuracy.

Ways to reduce hallucinations include:
- Better retrieval
- Better chunking
- Reranking
- Strong prompts
- Source citations
- Grounded generation
- Output validation
- Confidence thresholds
- Human review for high-risk tasks

A useful rule is:

"If the retrieved context does not contain enough evidence, do not invent an answer."

---

## 21. RAG Evaluation

RAG systems should be evaluated at both retrieval and generation levels.

Retrieval evaluation asks:
- Did the system retrieve the correct information?
- Were relevant documents included?
- Were irrelevant documents excluded?

Generation evaluation asks:
- Is the answer supported by the retrieved context?
- Is the answer relevant?
- Is the answer complete?
- Is the answer factually correct?

Important concepts include:
- Context precision
- Context recall
- Answer relevance
- Faithfulness
- Groundedness

A RAG system can fail even when the LLM is excellent if retrieval returns the wrong documents.

---

## 22. RAG Failure Modes

Common RAG problems include:

### Poor chunking
Important information is separated across chunks.

### Poor embeddings
The embedding model does not represent the domain well.

### Incorrect retrieval
The correct document is not retrieved.

### Too much context
The prompt contains irrelevant information.

### Too little context
The retrieved chunks do not contain enough evidence.

### Stale knowledge
The knowledge base has not been updated.

### Metadata errors
Incorrect metadata causes relevant documents to be filtered out.

### Hallucination
The model generates unsupported information.

### Prompt injection
Malicious content inside retrieved documents attempts to manipulate the model's instructions.

---

## 23. RAG Security

RAG systems should treat retrieved documents as untrusted data.

Important security controls include:
- Access control
- Tenant isolation
- Metadata-based authorization
- Document sanitization
- Prompt-injection detection
- Secrets protection
- Audit logging
- Encryption
- Rate limiting

A user should never retrieve documents simply because they are semantically similar if the user does not have permission to access those documents.

For multi-tenant SaaS applications, every retrieval operation should enforce tenant boundaries.

---

## 24. RAG and Fine-Tuning

RAG and fine-tuning solve different problems.

RAG is generally useful for giving a model access to external or changing information.

Fine-tuning is generally useful for changing model behavior, style, formatting, or task-specific patterns.

Example:

A company wants an AI assistant to answer questions using its latest HR policy.

RAG is appropriate because the policy may change and should remain external to the model.

A company wants the model to consistently produce outputs in a specific structured style.

Fine-tuning may be appropriate if prompting alone is insufficient.

RAG and fine-tuning can also be used together.

---

## 25. RAG Example: Customer Support

Suppose an e-commerce company has thousands of support documents.

A customer asks:

"Can I return a product after 20 days?"

The RAG system can:

1. Convert the question into an embedding.
2. Search the support knowledge base.
3. Retrieve the return-policy chunks.
4. Add those chunks to the prompt.
5. Ask the LLM to answer using the retrieved policy.
6. Return the answer with the relevant source.

This allows the assistant to answer using the company's actual policy instead of relying only on pretrained knowledge.

---

## 26. Simple Python RAG Architecture

A simplified implementation looks like this:

```python
documents = load_documents()

chunks = split_into_chunks(documents)

embeddings = embedding_model.embed(chunks)

vector_store.add(
    documents=chunks,
    embeddings=embeddings
)

question = "What is the company's refund policy?"

query_embedding = embedding_model.embed([question])

results = vector_store.search(
    query_embedding,
    top_k=5
)

context = "\n\n".join(results)

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}
"""

answer = llm.generate(prompt)

print(answer)
```

This is a conceptual example. Production systems require error handling, authentication, authorization, monitoring, evaluation, and data-quality controls.

---

## 27. Local RAG with Ollama

Ollama can be used to run supported AI models locally.

A local RAG architecture can use:
- Ollama for local LLM inference
- An embedding model for vector generation
- FAISS or another vector store for retrieval
- Python for application logic
- FastAPI for serving the RAG application

Example architecture:

User
-> FastAPI
-> Query embedding
-> FAISS
-> Retrieved chunks
-> Prompt
-> Ollama
-> Response

Running models locally can be useful for development, privacy-sensitive workloads, experimentation, and offline environments, depending on hardware and model requirements.

---

## 28. FastAPI in AI Applications

FastAPI is a Python web framework commonly used to build APIs.

A RAG API might expose an endpoint such as:

POST /ask

Request:

```json
{
  "question": "What is the refund policy?"
}
```

Response:

```json
{
  "answer": "Customers can request a refund...",
  "sources": [
    "refund-policy.pdf"
  ]
}
```

FastAPI can provide the API layer between a frontend application and the RAG pipeline.

---

## 29. AI Agent vs RAG

RAG retrieves information and uses that information to generate an answer.

An AI agent is a broader system that can reason through tasks and use tools.

An agent may have:
- LLM
- Memory
- Tools
- APIs
- RAG
- Planning
- Action execution
- Validation

RAG can therefore be one capability inside an AI agent.

Example customer-support agent:

1. Understand customer request.
2. Search company knowledge base using RAG.
3. Check order status through an API.
4. Decide what action is needed.
5. Respond to the customer.
6. Escalate to a human when necessary.

---

## 30. RAG Interview Questions

### What is RAG?

RAG stands for Retrieval-Augmented Generation. It combines information retrieval with a generative language model. Instead of relying only on pretrained knowledge, the system retrieves relevant external documents and provides them as context to the model before generating an answer.

### Why use RAG?

RAG is useful when an application needs private, domain-specific, frequently changing, or large amounts of external information.

### What is an embedding?

An embedding is a numerical vector representation of information that captures semantic relationships. Similar meanings tend to have similar vectors.

### What is a vector database?

A vector database stores embeddings and supports similarity search over those vectors. It is commonly used to retrieve relevant documents in RAG systems.

### What is FAISS?

FAISS is a library for efficient similarity search over dense vectors. It can be used as the retrieval component of a local RAG application.

### What is chunking?

Chunking is the process of dividing large documents into smaller, meaningful sections before generating embeddings.

### What happens when retrieval returns irrelevant documents?

Answer quality can decrease because the LLM receives poor context. Solutions include improving chunking, embeddings, metadata filtering, hybrid search, query rewriting, and reranking.

### Is RAG guaranteed to prevent hallucinations?

No. RAG can reduce hallucination by grounding the model in retrieved evidence, but the system still needs strong retrieval, prompting, validation, and evaluation.

### RAG versus fine-tuning?

RAG gives a model access to external knowledge at runtime. Fine-tuning changes model behavior through additional training. RAG is usually preferable when the main requirement is access to changing or private information.

---

## 31. End-to-End RAG Architecture

A production RAG application can be represented as:

DATA SOURCES
    |
    v
Document Loaders
    |
    v
Text Extraction
    |
    v
Cleaning
    |
    v
Chunking
    |
    v
Embedding Model
    |
    v
Vector Database
    |
    |
    +----------------------+
                           |
USER QUESTION              |
    |                      |
    v                      |
Query Processing           |
    |                      |
    v                      |
Query Embedding            |
    |                      |
    v                      |
Retriever -----------------+
    |
    v
Metadata Filtering
    |
    v
Reranking
    |
    v
Relevant Context
    |
    v
Prompt Construction
    |
    v
LLM
    |
    v
Grounded Answer
    |
    v
Sources / Citations

---

## 32. Best Practices for RAG

1. Use high-quality source documents.
2. Clean documents before indexing.
3. Choose chunk sizes based on document structure.
4. Preserve metadata.
5. Use an embedding model appropriate for the language and domain.
6. Start with vector retrieval and evaluate it before adding complexity.
7. Use metadata filtering for authorization and precision.
8. Consider hybrid search for exact identifiers.
9. Consider reranking when retrieval quality is insufficient.
10. Limit retrieved context to relevant information.
11. Require the model to ground answers in retrieved evidence.
12. Return source references when possible.
13. Evaluate retrieval separately from generation.
14. Continuously update stale documents.
15. Protect the system against prompt injection and unauthorized retrieval.
16. Log retrieval and generation behavior for debugging.
17. Build automated evaluation datasets from real user questions.
18. Monitor latency, cost, relevance, and answer quality.

---

## 33. Key Terms

AI: Artificial Intelligence.

Machine Learning: A subset of AI in which systems learn patterns from data.

Deep Learning: Machine learning based on multi-layer neural networks.

Generative AI: AI capable of generating new content.

LLM: Large Language Model.

Token: A unit of text processed by an AI model.

Transformer: Neural-network architecture based heavily on attention mechanisms.

Embedding: A numerical vector representation of information.

Vector Database: A system designed to store and search vector representations.

FAISS: A library for efficient vector similarity search.

Chunking: Splitting documents into smaller retrieval units.

Retriever: A component that finds relevant information.

Reranker: A component that improves the ranking of retrieved candidates.

RAG: Retrieval-Augmented Generation.

Hallucination: Unsupported or incorrect information generated by an AI system.

Fine-tuning: Additional model training used to adapt model behavior.

Agent: An AI system capable of using tools and taking actions toward a goal.

---

## 34. Summary

A reliable RAG system is not simply "LLM + vector database."

A complete RAG system includes:

High-quality data
+ Good document processing
+ Appropriate chunking
+ Strong embeddings
+ Effective retrieval
+ Metadata filtering
+ Optional reranking
+ Grounded prompting
+ LLM generation
+ Evaluation
+ Security
+ Monitoring

The quality of the final answer depends heavily on the quality of the retrieved context. Improving retrieval is therefore often as important as choosing the language model.
