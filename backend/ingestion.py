import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader

# Choose embedding model
embeddings = HuggingFaceEmbeddings()

# Load documents (PDF, TXT, or an entire directory)
loaders = [
    DirectoryLoader("docs/", glob="*.txt", loader_cls=TextLoader),
    DirectoryLoader("docs/", glob="*.pdf", loader_cls=PyPDFLoader),
]
documents = []
for loader in loaders:
    documents.extend(loader.load())

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs_split = splitter.split_documents(documents)

# Create vector store
vectorstore = FAISS.from_documents(docs_split, embeddings)

# Save FAISS index
vectorstore.save_local("vectorstore")
print("✅ Vectorstore created and saved in /backend/vectorstore/")
