import streamlit as st
import pandas as pd
import supabase as supa

st.sidebar.write("Grupos")
st.sidebar.link_button("GRUPO 01")
st.sidebar.link_button("GRUPO 02")

lista = ["Acoes", "Responsavel", "Atrasados", "Em dia"]
escolha = st.selectbox("Escolha uma opcao : ", lista)
if escolha == "Acoes":
  st.write("Estas são as XX ações do planejamento estratégico 2024")
  st.selectbox("Es
if escolha == "Responsavel":
   list_resp = ["João Couto", "Denize"]
   resp = st.radio("Escolha o responsavel para listar todaas as suas ações", list_resp)
   if resp == "João Couto":
      st.write("Este é o João Couto")
      #st.image()
   if resp == "Denize":
      st.write("Esta é a Denize")
      #st.image()
   #fazer o filtro no supabse com o resp
if escolha == "Atrasados":
   st.write("Estas ações estão com os seguinte atrasos")
if escolha == "Em dia"
   st.write("Estas ações estão em dia")


  
