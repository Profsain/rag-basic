from langchain_classic.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Retrieve the API key from environment variables
api_key = os.getenv("API_KEY")

llm = OpenAI(api_key=api_key)


# step 1: Load the documents
print("\nStep 1: Load the documents")
print("_" * 50)

# load the knowledge_base.md file
with open("knowledge_base.md", "r") as file:
    knowledge_base = file.read()
print("Knowledge base loaded successfully.")

# step 2: Split the documents into chunks
print("\nStep 2: Split the documents into chunks")
print("_" * 50)
# split the knowledge base into chunks of 200 characters with an overlap of 50 characters
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, 
    chunk_overlap=50,
    separators=["\n\n", "\n", " ", ""],
    length_function=len
    )
chunks = text_splitter.split_text(knowledge_base)
print(f"Number of chunks created: {len(chunks)}")
print("Chunks created successfully.")
# print the first 3 chunks
# for i, chunk in enumerate(chunks[:3]):
#     print(f"\nChunk {i+1}:\n{chunk}")

# step 3: Create embeddings for the chunks
print("\nStep 3: Create embeddings for the chunks")
print("_" * 50)
# create embeddings for the chunks using HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
print("Embeddings created successfully.")
# openai embeddings
# embeddings = OpenAIEmbeddings(api_key=api_key)
# print first 3 embeddings
for i, chunk in enumerate(chunks[:3]):
    embedding = embeddings.embed_query(chunk)
    print(f"\nEmbedding for chunk {i+1}:\n{embedding}")

# step 4: Create a vector store from the embeddings 
print("\nStep 4: Create a vector store from the embeddings")
print("_" * 50)
