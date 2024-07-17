import streamlit as st
import pandas as pd
import supabase as supa
st.set_page_config(layout="wide")
st.sidebar.title("Grupos")
g1=st.sidebar.button("GRUPO 01")
g2=st.sidebar.button("GRUPO 02")
g3=st.sidebar.button("GRUPO 03")
g4=st.sidebar.button("GRUPO 04")
g5=st.sidebar.button("GRUPO 05")
g6=st.sidebar.button("INSERIR AÇÃO")
g7=st.sidebar.button("OUTROS")

if g1:
  st.title("Este é GRUPO 01 formado por este membros e suas ações estão ao lado")
  
  df=pd.read_excel("PLANEJAMENTO ESTRATÉGICO 2024 GRUPO 01.xlsx", sheet_name=2) 
  df_descr=df.iloc[0,1]
  df_term=df.iloc[0,6]
  colunas=list(df.columns)
  st.sidebar.write(df_descr)
  st.sidebar.write(df_term)
  st.sidebar.write(colunas)
  col1 = st.columns((1,1,1))
  col1[0].image("zeroum.jpg")
  col1[1].dataframe(df.head(1))

  
    
if g2:
  st.title("Este é GRUPO 02 formado por este membros e suas ações estão ao lado")

if g3:
  st.title("Este é GRUPO 03 formado por este membros e suas ações estão ao lado")
  
if g4:
  st.title("Este é GRUPO 04 formado por este membros e suas ações estão ao lado")
  
if g5:
  st.title("Este é GRUPO 05 formado por este membros e suas ações estão ao lado")

if g6:
  st.title("Este é o modulo de inserção de ações")
  


#lista = ["Acoes", "Responsavel", "Atrasados", "Em dia"]
#escolha = st.selectbox("Escolha uma opcao : ", lista)
#if escolha == "Acoes":
#  st.write("Estas são as XX ações do planejamento estratégico 2024")
#  st.selectbox("Es
#if escolha == "Responsavel":
#   list_resp = ["João Couto", "Denize"]
#   resp = st.radio("Escolha o responsavel para listar todaas as suas ações", list_resp)
#   if resp == "João Couto":
#      st.write("Este é o João Couto")
#      #st.image()
#   if resp == "Denize":
#      st.write("Esta é a Denize")
#      #st.image()
#   #fazer o filtro no supabse com o resp
#if escolha == "Atrasados":
#   st.write("Estas ações estão com os seguinte atrasos")
#if escolha == "Em dia"
#   st.write("Estas ações estão em dia")"""


  
