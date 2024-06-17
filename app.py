# pylint: disable=missing-module-docstring
import duckdb
import streamlit as st
import pandas as pd

con = duckdb.connect(database = "data/exercice_sql.duckdb",read_only=False)


st.write("Exercice de révision SQL")

with st.sidebar:
    theme = st.selectbox(
        "Choissisez la thématique que vous souhaitez réviser",
        ["Joins", "Group By", "Windows Functions"],
        placeholder="Choisie une thématique",
    )
    st.write("Your selection : ", theme)

    exercice_df = con.execute(f"SELECT * FROM exercice_data WHERE theme ='{theme}'").df()
    st.write(exercice_df.tables[0])


tab_question, tab_solution = st.tabs(["Question", "Solution"])


# ANSWER = """
# SELECT *
# FROM customer_data
# RIGHT JOIN order_data
# USING(CustomerID)
# """
# solution_df = duckdb.sql(ANSWER).df()
#
# with tab_question:
#     st.write("Tables des clients customer_data :", customer_data)
#     st.write("Tables des commandes order_data :", order_data)
#     query = st.text_area(
#         label="Renseignez la requête SQL qui permet de joindre la table des commandes à la table des clients"
#     )
#     if query:
#         result_df = duckdb.sql(query).df()
#         st.write(result_df)
#         # comparing with result table
#         try:
#             result_df = result_df[solution_df.columns]
#             st.write("La comparaion avec les solutions", result_df.compare(solution_df))
#         except KeyError as e:
#             st.write("Erreur : Certaines colonnes ou lignes sont manquantes")

#
# with tab_solution:
#     st.write("la requête utilisée :", ANSWER)
#     st.write("la table solution :", solution_df)
