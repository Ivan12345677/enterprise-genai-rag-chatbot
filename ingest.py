import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

DOCS_PATH = "docs"
VECTORSTORE_PATH = "vectorstore"

def load_documents():
    documents = []

    for file in os.listdir(DOCS_PATH):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(DOCS_PATH, file)

            loader = PyPDFLoader(pdf_path)
            docs = loader.load()

            documents.extend(docs)

            print(f"Loaded: {file}")

    return documents

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks

def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local(VECTORSTORE_PATH)

    print("Vector DB saved successfully")

if __name__ == "__main__":
    print("Starting ingestion process...")

    docs = load_documents()

    chunks = split_documents(docs)

    create_vectorstore(chunks)

    print("Ingestion completed")