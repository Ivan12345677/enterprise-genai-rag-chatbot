from agents.orchestrator import AgentOrchestrator

orchestrator = AgentOrchestrator()

print("Enterprise Agentic AI Assistant Ready")
print("Type 'exit' to quit\n")

while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    try:

        response = orchestrator.execute(query)

        print("\nAgent Route:")
        print(response.get("route"))

        print("\nBot:")

        result = response.get("result", {})

        print(result.get("response"))

        print("\nValidation:")

        validation = response.get("validation", {})

        print(
            f"Validated: {validation.get('validated')}"
        )

        print(
            f"Risk Score: {validation.get('risk_score')}"
        )

        print("\n" + "-" * 50)

    except Exception as e:

        print(f"Error: {e}")