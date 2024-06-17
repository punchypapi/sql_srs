# pylint: disable=missing-module-docstring
import os
import logging
import duckdb
import streamlit as st

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")
if "exercice_sql.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())
    # subprocess.run(["python","init_db.py"])


con = duckdb.connect(database="data/exercice_sql.duckdb", read_only=False)
# retrieve exercice table
exercice_df = con.execute("SELECT * FROM exercice_data").df()
st.write("Exercice de révision SQL")

with st.sidebar:
    theme_selection = st.selectbox(
        "Choissisez la thématique que vous souhaitez réviser",
        list(exercice_df.theme.unique()),
        placeholder="Choisie une thématique",
    )
    st.write("Your selection : ", theme_selection)

    exercice_selection = st.selectbox(
        "Choissisez l'exercice que vous souhaitez réviser",
        list(exercice_df[exercice_df.theme == theme_selection]["exercise_name"]),
        placeholder="Choisie une thématique",
    )
    st.write("Your selection : ", exercice_selection)

    exercices_df_sorted = exercice_df[exercice_df.exercise_name == exercice_selection]

    st.write("Last reviewed :", exercices_df_sorted.last_reviewed.values[0])


tab_question, tab_solution = st.tabs(["Question", "Solution"])

ANSWER = exercices_df_sorted.answer_file.values[0]
with open(f"answers/{ANSWER}") as f:
    answer = f.read()
    solution_df = con.execute(f"{answer}").df()
with tab_question:
    for table in list(exercices_df_sorted.tables.values[0]):
        display_table = con.execute(f"SELECT * FROM {table}").df()
        st.write(f"Table {table} :", display_table)
    query = st.text_area(
        label="Renseignez la requête SQL qui permet de joindre toutes les tables"
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
