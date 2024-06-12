import streamlit as st
import pandas as pd
import duckdb

st.write("Exercice de révision SQL")
options = st.selectbox("Choissisez la thématique que vous souhaitez réviser",
                       ['Joins','Group By', 'Windows Functions'],
                       placeholder = "Choisie une thématique")


data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

st.write("Table utilisé :")
st.dataframe(df)
input_text = st.text_area(label="Renseignez la requête SQL")
if input_text :
    result_df = duckdb.sql(input_text).df()
    st.write(result_df)

