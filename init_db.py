import duckdb
import pandas as pd

con = duckdb.connect(database="data/exercice_sql.duckdb", read_only=False)

# ---------------
# LIST OF EXERCICES
# --------------

exercice_data = pd.DataFrame(
    {
        "theme": ["Joins", "Joins", "Windows Functions"],
        "exercise_name": [
            "Join customers and orders",
            "Join orders with customers, products and warehouses",
            "Rank customer by order",
        ],
        "tables": [
            ["customer_data", "order_data"],
            ["customer_data", "product_data", "order_data", "inventory_data"],
            ["customer_data", "order_data"],
        ],
        "answer_file": [
            "join_customers_orders.sql",
            "join_customers_orders_products_inventory.sql",
            "",
        ],
        "last_reviewed": ["2020-01-01", "2024-04-01", "2023-04-01"],
    }
)

# Load the DataFrame into DuckDB as a temporary table
con.register("exercice_data", exercice_data)
# Create or replace the table in DuckDB
con.execute("CREATE OR REPLACE TABLE exercice_data AS SELECT * FROM exercice_data")

# ---------------
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

# Load the DataFrame into DuckDB as a temporary table
con.register("customer_data", customer_data)
# Create or replace the table in DuckDB
con.execute("CREATE OR REPLACE TABLE customer_data AS SELECT * FROM customer_data")

product_data = pd.DataFrame(
    {
        "ProductID": [1, 2, 3, 4, 5, 6, 7],
        "ProductName": [
            "Laptop",
            "Phone",
            "Tablet",
            "Monitor",
            "Keyboard",
            "Mouse",
            "Printer",
        ],
        "Price": [1200, 800, 300, 200, 100, 50, 150],
        "Stock": [10, 15, 12, 8, 20, 25, 13],
    }
)

# Load the DataFrame into DuckDB as a temporary table
con.register("product_data", product_data)
# Create or replace the table in DuckDB
con.execute("CREATE OR REPLACE TABLE product_data AS SELECT * FROM product_data")


order_data = pd.DataFrame(
    {
        "OrderID": [101, 102, 103, 104, 105, 106, 107],
        "CustomerID": [1, 2, 1, 4, 3, 5, 2],  # Ensure some CustomerIDs match
        "ProductID": [1, 2, 3, 4, 5, 6, 2],  # Ensure some ProductIDs match
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

# Load the DataFrame into DuckDB as a temporary table
con.register("order_data", order_data)
# Create or replace the table in DuckDB
con.execute("CREATE OR REPLACE TABLE order_data AS SELECT * FROM order_data")

inventory_data = pd.DataFrame(
    {
        "WarehouseID": [1, 2, 3],
        "WarehouseLocation": ["New York", "Los Angeles", "Chicago"],
        "ProductID": [1, 2, 3],
        "Stock": [100, 150, 120],
    }
)


con.register("inventory_data", inventory_data)
# Create or replace the table in DuckDB
con.execute("CREATE OR REPLACE TABLE inventory_data AS SELECT * FROM inventory_data")

# Close the connection
con.close()
