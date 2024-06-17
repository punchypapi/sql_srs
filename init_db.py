import duckdb
import pandas as pd

con = duckdb.connect(database = "data/exercice_sql.duckdb",read_only=False)

#---------------
# LIST OF EXERCICES
# --------------

exercice_data = pd.DataFrame(
    {"theme": ["Joins","Windows Functions"],
    "exercise_name": ["Join customers and orders", "Rank customer by order"],
    "tables": [["customer_data", "order_data"],["customer_data", "order_data"]],
    "last_reviewed": ["2020-01-01","2024-04-01"]
     }
)

con.execute("CREATE OR REPLACE TABLE exercice_data AS SELECT * FROM exercice_data")


#---------------
# CROSS JOIN EXERCICES
# --------------
customer_data = pd.DataFrame(
    {
        "CustomerID": [1, 2, 3, 4, 5],
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Email": [
            "alice@example.com",
            "bob@example.com",
            "charlie@example.com",
            "david@example.com",
            "eva@example.com",
        ],
        "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    }
)

con.execute("CREATE OR REPLACE TABLE customer_data AS SELECT * FROM customer_data")

order_data = pd.DataFrame(
    {
        "OrderID": [101, 102, 103, 104, 105, 106, 107],
        "CustomerID": [1, 2, 1, 4, 3, 5, 2],  # Ensure some CustomerIDs match
        "Product": [
            "Laptop",
            "Phone",
            "Tablet",
            "Monitor",
            "Keyboard",
            "Mouse",
            "Printer",
        ],
        "Quantity": [1, 2, 1, 2, 1, 1, 3],
        "OrderDate": [
            "2024-01-15",
            "2024-02-17",
            "2024-03-23",
            "2024-04-12",
            "2024-05-29",
            "2024-06-05",
            "2024-06-11",
        ],
    }
)

con.execute("CREATE OR REPLACE TABLE order_data AS SELECT * FROM order_data")

