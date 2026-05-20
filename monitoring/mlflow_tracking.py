import mlflow
import time


class MLflowTracker:

    def log_interaction(
        self,
        query,
        response,
        route
    ):

        with mlflow.start_run():

            mlflow.log_param(
                "query",
                query
            )

            mlflow.log_param(
                "route",
                route
            )

            mlflow.log_metric(
                "response_length",
                len(response)
            )

            mlflow.log_text(
                response,
                "response.txt"
            )