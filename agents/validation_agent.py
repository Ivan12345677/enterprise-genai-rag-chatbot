class ValidationAgent:

    def validate(self, response):

        hallucination_keywords = [
            "might",
            "possibly",
            "unknown",
            "not sure"
        ]

        risk_score = 0

        for word in hallucination_keywords:

            if word in response.lower():
                risk_score += 1

        return {
            "validated": risk_score < 2,
            "risk_score": risk_score
        }