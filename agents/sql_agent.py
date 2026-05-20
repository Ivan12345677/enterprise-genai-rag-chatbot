import sqlite3
import pandas as pd


class SQLAgent:

    def __init__(self):

        self.connection = sqlite3.connect(
            "data/sales.db"
        )

    def run(self, query):

        query = query.lower()

        if "sales" in query:

            sql_query = """
            SELECT *
            FROM sales
            """

            df = pd.read_sql_query(
                sql_query,
                self.connection
            )

            summary = df.describe(
                include="all"
            ).to_string()

            return {
                "agent": "SQLAgent",
                "sql_query": sql_query,
                "response": summary
            }

        return {
            "agent": "SQLAgent",
            "response": "No SQL workflow triggered"
        }