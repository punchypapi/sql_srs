import streamlit as st
import pandas as pd
import duckdb

st.write("Exercice de révision SQL")

options = st.selectbox("Choissisez la thématique que vous souhaitez réviser",
                       ['Joins','Group By', 'Windows Functions'],
                       placeholder = "Choisie une thématique")

tab_question, tab_solution = st.tabs(["Question", "Solution"])


customer_data = pd.DataFrame(
    dict(CustomerID=[1, 2, 3, 4, 5], Name=['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
         Email=['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com',
                'eva@example.com'], City=['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'])
)

order_data = pd.DataFrame(
    {
        'OrderID': [101, 102, 103, 104, 105, 106, 107],
        'CustomerID': [1, 2, 1, 4, 3, 5, 2],  # Ensure some CustomerIDs match
        'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Printer'],
        'Quantity': [1, 2, 1, 2, 1, 1, 3],
        'OrderDate': ['2024-01-15', '2024-02-17', '2024-03-23', '2024-04-12', '2024-05-29', '2024-06-05', '2024-06-11']
    }
)

with tab_question:
    st.write("Tables des clients :",customer_data)
    st.write("Tables des commandes :",order_data)
    query = st.text_area(label="Renseignez la requête SQL qui permet de joindre la table des commandes à la table des clients")
    if query:
        result_df = duckdb.sql(query).df()
        st.write(result_df)

with tab_solution:
    answer = """
    SELECT * 
    FROM customer_data 
    RIGHT JOIN order_data
    USING(CustomerID)
    
    """
    st.write("la requête utilisée :",answer)
    st.write(duckdb.sql(answer).df())