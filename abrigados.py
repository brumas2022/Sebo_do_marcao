import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine, text
import streamlit as st

st.set_page_config(layout="wide")

st.header("Animais abrigados na ARPAA")

engine = create_engine('postgresql://postgres.ibhcxtnwnonsnycfgjay:Hoje#estamos#firmes#como#geleia@aws-0-sa-east-1.pooler.supabase.com:5432/postgres')
#engine = create_engine('postgresql://postgres:Lula#2022@localhost:5432/postgres')
sql = "SELECT * FROM caninos"
df = pd.read_sql_query(sql, con=engine)
st.dataframe(df)
st.dataframe(df['foto'])

col1, col2, col3, col4 = st.columns((1,1,1,1))
col1.image(df['foto'][33], caption=df['nome'][33], use_column_width="always")
col2.image(df['foto'][2], caption=df['nome'][2], use_column_width="always")
col3.image(df['foto'][12], caption=df['nome'][12], use_column_width="always")
col4.image(df['foto'][12], caption=df['nome'][12], use_column_width="always")

col1.image(df['foto'][50], caption=df['nome'][50], use_column_width="always")
col2.image(df['foto'][51], caption=df['nome'][51], use_column_width="always")
col3.image(df['foto'][52], caption=df['nome'][52], use_column_width="always")
col4.image(df['foto'][53], caption=df['nome'][53], use_column_width="always")

col1.image(df['foto'][54], caption=df['nome'][54], use_column_width="always")


