import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Enterprise GenAI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 Enterprise GenAI Assistant")

st.markdown("Ask questions from enterprise documents using RAG architecture.")

# User input
question = st.text_input("Enter your question:")

# Ask button
if st.button("Ask"):

    if question.strip() != "":

        try:
            # Call FastAPI backend
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"question": question}
            )

            data = response.json()

            # Display answer
            st.subheader("Answer")
            st.write(data["answer"])

            # Display sources
            st.subheader("Sources")

            for source in data["sources"]:
                st.write(source)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a question.")