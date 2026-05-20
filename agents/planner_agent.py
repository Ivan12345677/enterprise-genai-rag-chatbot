class PlannerAgent:

    def decide(self, query):

        query = query.lower()

        analytics_keywords = [
            "sales",
            "revenue",
            "trend",
            "forecast",
            "analytics",
            "kpi"
        ]

        retrieval_keywords = [
            "summary",
            "document",
            "policy",
            "explain"
        ]

        for word in analytics_keywords:

            if word in query:
                return "sql"

        for word in retrieval_keywords:

            if word in query:
                return "retrieval"

        return "retrieval"