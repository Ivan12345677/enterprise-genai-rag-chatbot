from dotenv import load_dotenv

from transformers import pipeline

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface.llms import HuggingFacePipeline

from langchain_community.vectorstores import FAISS

from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory

load_dotenv()

VECTORSTORE_PATH = "vectorstore"

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore

def load_llm():
    pipe = pipeline(
        task="text2text-generation",
        model="google/flan-t5-small",
        max_new_tokens=128
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    return llm

def create_chat_chain():
    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    llm = load_llm()

    memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key="answer"
    )

    chat_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )

    return chat_chain