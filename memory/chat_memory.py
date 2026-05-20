from datetime import datetime


class ChatMemory:

    def __init__(self):

        # Stores complete conversation history
        self.history = []

    def add_message(self, role, content):

        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        self.history.append(message)

    def get_history(self):

        return self.history

    def clear_memory(self):

        self.history = []

    def get_last_message(self):

        if len(self.history) > 0:
            return self.history[-1]

        return None

    def get_conversation_context(self):

        context = ""

        for msg in self.history:

            context += (
                f"{msg['role'].upper()}: "
                f"{msg['content']}\n"
            )

        return context