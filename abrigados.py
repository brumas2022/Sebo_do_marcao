import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine, text
import streamlit as st

st.set_page_config(layout="wide")

st.header("Animais na ARPAA")

engine = create_engine('postgresql://postgres.ibhcxtnwnonsnycfgjay:Hoje#estamos#firmes#como#geleia@aws-0-sa-east-1.pooler.supabase.com:5432/postgres')
#engine = create_engine('postgresql://postgres:Lula#2022@localhost:5432/postgres')
sql = "SELECT * FROM caninos"
df = pd.read_sql_query(sql, con=engine)
lista = ["TABELA COMPLETA","TABELA COM FOTO", "MURAL DE FOTOS"]

escolha = st.sidebar.radio("ESCOLHA A OPCAO DESEJADA  :", lista)

if escolha=="TABELA COMPLETA":
   coluna = ['nome', 'foto']
   st.dataframe(df.loc[:, coluna])
if escolha=="TABELA COM FOTO":
   colunas = ['id','nome','foto']
   resultado = df.loc[:,colunas]
   st.data_editor(resultado,column_config={"foto": st.column_config.ImageColumn("Preview Image", help="Streamlit app preview screenshots")}, hide_index=True,)
   df_filtro = df[df["foto"]!=""]
   st.dataframe(df_filtro.set_index('id'))

   col1, col2, col3, col4 = st.columns((1,1,1,1))
   col1.image(df_filtro['foto'][54], caption=df_filtro['nome'][54], use_column_width="always")
   col2.image(df_filtro['foto'][32], caption=df_filtro['nome'][32], use_column_width="always")
   col3.image(df_filtro['foto'][51], caption=df_filtro['nome'][51], use_column_width="always")
   col4.image(df_filtro['foto'][41], caption=df_filtro['nome'][41], use_column_width="always")


if escolha=="MURAL DE FOTOS":

   from supabase import create_client, Client
   #url: str = os.environ.get("https://ibhcxtnwnonsnycfgjay.supabase.co")
   #key: str = os.environ.get("eyHHHJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImliaGN4dG53bm9uc255Y2ZnamF5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxNTM5NjIsImV4cCI6MjAxMDcyOTk2Mn0.PYLOei6RiMbucEqUmTtnmkcjDfIptsiTcNrUCmrBH7c")
   supabase: Client = create_client('https://ibhcxtnwnonsnycfgjay.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImliaGN4dG53bm9uc255Y2ZnamF5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NTE1Mzk2MiwiZXhwIjoyMDEwNzI5OTYyfQ.W9t9sqi_odq3kV2WovKCVfMXcFGprFOgai9Us9_rTQA')

   resposta = supabase.table("caninos").select("*").execute()

   
   c1, c2, c3, c4 = st.columns((1,1,1,1))
   c1.write(resposta.data[11]["nome"])
   c1.image(resposta.data[11]["foto"], use_column_width="always")
   c2.write(resposta.data[2]["nome"])
   c2.image(resposta.data[2]["foto"], use_column_width="always")
   c3.write(resposta.data[3]["nome"])
   c3.image(resposta.data[3]["foto"], use_column_width="always") # deu certo magrelo
   c4.write(resposta.data[57]["nome"])
   c4.image(resposta.data[57]["foto"], use_column_width="always") # deu certo magrelo

   c1.write(resposta.data[5]["nome"])
   c1.image(resposta.data[5]["foto"], use_column_width="always")
   c2.write(resposta.data[6]["nome"])
   c2.image(resposta.data[6]["foto"], use_column_width="always")
   c3.write(resposta.data[7]["nome"])
   c3.image(resposta.data[7]["foto"], use_column_width="always")
   c4.write(resposta.data[12]["nome"])
   c4.image(resposta.data[12]["foto"], use_column_width="always")

   c1.write(resposta.data[14]["nome"])
   c1.image(resposta.data[14]["foto"], use_column_width="always")
   c2.write(resposta.data[15]["nome"])
   c2.image(resposta.data[15]["foto"], use_column_width="always")
   c3.write(resposta.data[23]["nome"])
   c3.image(resposta.data[23]["foto"], use_column_width="always")
   c4.write(resposta.data[28]["nome"])
   c4.image(resposta.data[28]["foto"], use_column_width="always")


   c1.write(resposta.data[30]["nome"])
   c1.image(resposta.data[30]["foto"], use_column_width="always")
   c2.write(resposta.data[32]["nome"])
   c2.image(resposta.data[32]["foto"], use_column_width="always")
   c3.write(resposta.data[34]["nome"])
   c3.image(resposta.data[34]["foto"], use_column_width="always")
   c4.write(resposta.data[36]["nome"])
   c4.image(resposta.data[36]["foto"], use_column_width="always")

   c1.write(resposta.data[38]["nome"])
   c1.image(resposta.data[38]["foto"], use_column_width="always")
   c2.write(resposta.data[39]["nome"])
   c2.image(resposta.data[39]["foto"], use_column_width="always")
   c3.write(resposta.data[40]["nome"])
   c3.image(resposta.data[40]["foto"], use_column_width="always")
   c4.write(resposta.data[41]["nome"])
   c4.image(resposta.data[41]["foto"], use_column_width="always")


   #res = supabase.storage.list_buckets()
   #st.write(res.row)

   

  
   #col1, col2, col3, col4 = st.columns((1,1,1,1))
   #3col1.image(df['foto'][33], caption=df['nome'][33], use_column_width="always")
   #col2.image(df['foto'][2], caption=df['nome'][2], use_column_width="always")
   #col3.image(df['foto'][12], caption=df['nome'][12], use_column_width="always")
   #col4.image(df['foto'][6], caption=df['nome'][6], use_column_width="always")
    
   #col1.image(df['foto'][50], caption=df['nome'][50], use_column_width="always")
   #col2.image(df['foto'][51], caption=df['nome'][51], use_column_width="always")
   #col3.image(df['foto'][52], caption=df['nome'][52], use_column_width="always")
   #col4.image(df['foto'][53], caption=df['nome'][53], use_column_width="always")
    
   #col1.image(df['foto'][54], caption=df['nome'][54], use_column_width="always")
   #col2.image(df['foto'][3], caption=df['nome'][3], use_column_width="always")
   #col3.image(df['foto'][5], caption=df['nome'][5], use_column_width="always")
   #col4.image(df['foto'][7], caption=df['nome'][7], use_column_width="always")
