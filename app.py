from chatbot import create_chat_chain

chat_chain = create_chat_chain()

print("Enterprise GenAI Assistant Ready")
print("Type 'exit' to quit\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    try:
        result = chat_chain.invoke(
            {"question": query}
        )

        print("\nBot:")
        print(result["answer"])

        print("\nSources:")
        for doc in result["source_documents"]:
            print(doc.metadata.get("source"))

        print("\n" + "-" * 50)

    except Exception as e:
        print(f"Error: {e}")