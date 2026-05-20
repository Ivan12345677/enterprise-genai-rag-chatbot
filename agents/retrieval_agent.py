from chatbot import ask_rag


class RetrievalAgent:

    def run(self, query):

        response = ask_rag(query)

        return {
            "agent": "RetrievalAgent",
            "query": query,
            "response": response
        }