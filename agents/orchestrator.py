from agents.retrieval_agent import RetrievalAgent
from agents.validation_agent import ValidationAgent
from agents.planner_agent import PlannerAgent
from agents.sql_agent import SQLAgent

from memory.chat_memory import ChatMemory
from monitoring.mlflow_tracking import MLflowTracker


class AgentOrchestrator:

    def __init__(self):

        # ---------------------------------
        # Initialize AI Agents
        # ---------------------------------
        self.retriever = RetrievalAgent()
        self.validator = ValidationAgent()
        self.planner = PlannerAgent()
        self.sql_agent = SQLAgent()

        # ---------------------------------
        # Conversational Memory
        # ---------------------------------
        self.memory = ChatMemory()

        # ---------------------------------
        # MLflow Tracking
        # ---------------------------------
        self.tracker = MLflowTracker()

    def execute(self, query):

        # ---------------------------------
        # Store User Query
        # ---------------------------------
        self.memory.add_message(
            "user",
            query
        )

        # ---------------------------------
        # Decide Workflow Route
        # ---------------------------------
        route = self.planner.decide(query)

        # =================================
        # Retrieval / RAG Workflow
        # =================================
        if route == "retrieval":

            # Run Retrieval Agent
            result = self.retriever.run(query)

            # Validate AI Response
            validation = self.validator.validate(
                result["response"]
            )

            # Store Assistant Response
            self.memory.add_message(
                "assistant",
                result["response"]
            )

            # Track Interaction
            self.tracker.log_interaction(
                query=query,
                response=result["response"],
                route=route
            )

            return {
                "route": route,
                "agent": result["agent"],
                "result": result,
                "validation": validation,
                "memory": self.memory.get_history()
            }

        # =================================
        # SQL Analytics Workflow
        # =================================
        elif route == "sql":

            # Run SQL Agent
            result = self.sql_agent.run(query)

            # Validate AI Response
            validation = self.validator.validate(
                result["response"]
            )

            # Store Assistant Response
            self.memory.add_message(
                "assistant",
                result["response"]
            )

            # Track Interaction
            self.tracker.log_interaction(
                query=query,
                response=result["response"],
                route=route
            )

            return {
                "route": route,
                "agent": result["agent"],
                "result": result,
                "validation": validation,
                "memory": self.memory.get_history()
            }

        # =================================
        # Fallback Workflow
        # =================================
        return {
            "route": "fallback",
            "message": "No matching workflow found"
        }