import streamlit as st
import pandas as pd
import duckdb

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

st.write("Dataframe used :")
st.dataframe(df)
input_text = st.text_area(label="Please enter the query")
try :
    result_df = duckdb.sql(input_text).df()
    st.write(result_df)
except :
    st.error("No query selected")

