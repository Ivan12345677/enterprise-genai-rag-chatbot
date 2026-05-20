import sqlite3
import pandas as pd


data = {
    "month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr"
    ],
    "sales": [
        10000,
        15000,
        12000,
        18000
    ]
}

df = pd.DataFrame(data)

connection = sqlite3.connect(
    "data/sales.db"
)

df.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index=False
)

print("Sales data loaded successfully")