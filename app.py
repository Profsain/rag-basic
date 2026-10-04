from langchain_classic.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
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
# print the first 500 characters of the knowledge base
print(knowledge_base[:500])

# step 2: Split the documents into chunks
print("\nStep 2: Split the documents into chunks")
print("_" * 50)
# split the knowledge base into chunks of 1000 characters with an overlap of 200 characters
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_text(knowledge_base)
print(f"Number of chunks created: {len(chunks)}")
