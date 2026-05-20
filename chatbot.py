from dotenv import load_dotenv

from transformers import pipeline

from langchain_core.prompts import PromptTemplate

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface.llms import HuggingFacePipeline

from langchain_community.vectorstores import FAISS

from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()

# Path to saved FAISS vector database
VECTORSTORE_PATH = "vectorstore"

# -----------------------------
# Custom Prompt Engineering
# -----------------------------

custom_prompt = """
You are an enterprise AI assistant.

Use ONLY the provided context to answer.

Rules:
- Do not make up answers.
- If answer is not found, say:
  "I could not find relevant information."
- Keep responses professional.
- Do not generate inappropriate responses.
- Cite retrieved information when possible.

Context:
{context}

Question:
{question}

Answer:
"""

PROMPT = PromptTemplate(
    template=custom_prompt,
    input_variables=["context", "question"]
)

# -----------------------------
# Load Vector Database
# -----------------------------

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

# -----------------------------
# Load Local LLM
# -----------------------------

def load_llm():

    pipe = pipeline(
        task="text2text-generation",
        model="google/flan-t5-small",
        max_new_tokens=128
    )

    llm = HuggingFacePipeline(
        pipeline=pipe
    )

    return llm

# -----------------------------
# Create Conversational RAG Chain
# -----------------------------

def create_chat_chain():

    # Load FAISS vector database
    vectorstore = load_vectorstore()

    # Create retriever
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    # Load LLM
    llm = load_llm()

    # Add conversation memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    # Create conversational retrieval chain
    chat_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        combine_docs_chain_kwargs={
            "prompt": PROMPT
        }
    )

    return chat_chain

def ask_rag(query):

    chat_chain = create_chat_chain()

    result = chat_chain.invoke(
        {"question": query}
    )

    answer = result["answer"]

    sources = []

    for doc in result["source_documents"]:
        sources.append(
            doc.metadata.get("source")
        )

    final_response = f"{answer}\n\nSources:\n"

    for source in sources:
        final_response += f"- {source}\n"

    return final_response