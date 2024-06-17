# pylint: disable=missing-module-docstring
import duckdb
import streamlit as st
import pandas as pd

con = duckdb.connect(database="data/exercice_sql.duckdb", read_only=False)


st.write("Exercice de révision SQL")

with st.sidebar:
    theme = st.selectbox(
        "Choissisez la thématique que vous souhaitez réviser",
        ["Joins", "Group By", "Windows Functions"],
        placeholder="Choisie une thématique",
    )
    st.write("Your selection : ", theme)

    exercice_df = con.execute(
        f"SELECT * FROM exercice_data WHERE theme ='{theme}'"
    ).df()


tab_question, tab_solution = st.tabs(["Question", "Solution"])

ANSWER = exercice_df.answer_file[0]
with open(f"answers/{ANSWER}") as f:
    answer = f.read()
    solution_df = con.execute(f"{answer}").df()

with tab_question:
    for table in list(exercice_df.tables[0]):
        display_table = con.execute(f"SELECT * FROM {table}").df()
        st.write(f"Table {table} :", display_table)
    query = st.text_area(
        label="Renseignez la requête SQL qui permet de joindre la table des commandes à la table des clients"
    )
    if query:
        result_df = con.execute(query).df()
        st.write(result_df)
        # comparing with result table
        try:
            result_df = result_df[solution_df.columns]
            st.write("La comparaion avec les solutions", result_df.compare(solution_df))
        except KeyError as e:
            st.write("Erreur : Certaines colonnes ou lignes sont manquantes")


with tab_solution:
    st.write("la requête utilisée :", answer)
    st.write("la table solution :", solution_df)
