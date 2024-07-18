import streamlit as st
import pandas as pd
import supabase as supa
st.set_page_config(layout="wide")
st.sidebar.title("Grupos")

def cliq_5():
      
      df5.columns = ['Item', 'Descrição', 'Responsavel', 'Data Inicio', 'Data Fim', 'Proprio', 'União', 'Quem', 'N1', 'N2']
      df5.drop(['Responsavel', 'N1', 'N2'], inplace=True, axis=1)
      df5.set_index("Item", inplace=True)
      st.dataframe(df5.iloc[4:])
def cliq_6():
      df6.columns = ['Item', 'Descrição', 'Responsavel', 'Data Inicio', 'Data Fim', 'Proprio', 'União', 'Quem', 'N1', 'N2']
      df6.drop(['Responsavel', 'N1', 'N2'], inplace=True, axis=1)
      df6.set_index("Item", inplace=True)
      st.dataframe(df6.iloc[4:])
def cliq_7():
      df7.columns = ['Item', 'Descrição', 'Responsavel', 'Data Inicio', 'Data Fim', 'Proprio', 'União', 'Quem', 'N1', 'N2']
      df7.drop(['Responsavel', 'N1', 'N2'], inplace=True, axis=1)
      df7.set_index("Item", inplace=True)
      st.dataframe(df7.iloc[4:])


g1=st.sidebar.button("GRUPO 01")
g2=st.sidebar.button("GRUPO 02")
g3=st.sidebar.button("GRUPO 03")
g4=st.sidebar.button("GRUPO 04")
g5=st.sidebar.button("GRUPO 05")
g6=st.sidebar.button("INSERIR AÇÃO")
g7=st.sidebar.button("OUTROS")

if g1:
  #st.title("Este é GRUPO 01 formado por este membros e suas ações estão ao lado")
  
  df1=pd.read_excel("PLANEJAMENTO ESTRATÉGICO 2024 GRUPO 01.xlsx", sheet_name=1)
  df2=pd.read_excel("PLANEJAMENTO ESTRATÉGICO 2024 GRUPO 01.xlsx", sheet_name=2)
  df3=pd.read_excel("PLANEJAMENTO ESTRATÉGICO 2024 GRUPO 01.xlsx", sheet_name=3)
  df4=pd.read_excel("PLANEJAMENTO ESTRATÉGICO 2024 GRUPO 01.xlsx", sheet_name=4)
  df5=pd.read_excel("PLANEJAMENTO ESTRATÉGICO 2024 GRUPO 01.xlsx", sheet_name=5)
  df6=pd.read_excel("PLANEJAMENTO ESTRATÉGICO 2024 GRUPO 01.xlsx", sheet_name=6)
  df7=pd.read_excel("PLANEJAMENTO ESTRATÉGICO 2024 GRUPO 01.xlsx", sheet_name=7)
  
  df_descr=df1.iloc[0,1]
  df_term=df1.iloc[0,6]

  nome_acao1=df1.columns[1]
  acao1=df1.columns[0]
  
  nome_acao2=df2.columns[1]
  acao2=df2.columns[0]

  nome_acao3=df3.columns[1]
  acao3=df3.columns[0]

  nome_acao4=df4.columns[1]
  acao4=df4.columns[0]

  nome_acao5=df5.columns[1]
  acao5=df5.columns[0]

  nome_acao6=df6.columns[1]
  acao6=df6.columns[0]

  nome_acao7=df7.columns[1]
  acao7=df7.columns[0]
  
  st.sidebar.write(df_descr)
  st.sidebar.write(df_term)
  
  
  col1 = st.columns((1,1,1,1))
  col1[0].image("DALTON_VIRGILIO.png", width=200, use_column_width=True)
  col1[1].image("RENATA_MORENO.png", width=200, use_column_width=True)
  col1[2].image("WILMA_MUNDIM.png", width=200, use_column_width=True)
  col1[3].image("EDUARDO_RAMOS.png", width=200, use_column_width=True)
  col1[0].button(acao5+" - "+nome_acao5, on_click=cliq_5 ,use_container_width=True)
  col1[0].button(acao6+" - "+nome_acao6, on_click=cliq_6, use_container_width=True)
  col1[0].button(acao7+" - "+nome_acao7, on_click=cliq_7, use_container_width=True)
  col1[1].button(acao4+" - "+nome_acao4)
  col1[1].button(acao3+" - "+nome_acao3)
  col1[2].button(acao2+" - "+nome_acao2)
  col1[3].button(acao1+" - "+nome_acao1)
  
 
  
    
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
  




  
