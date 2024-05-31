import pandas as pd
import streamlit as st
#from supabase import create_client, Client

st.set_page_config("Controle de Perdas", layout="wide")

st.header("Planilha de troca de hidrometros - GRUPO   01 02 03 04")

lista = ["PERDAS", "TESTE SUPABASE", "CALENDARIO"]

st.sidebar.write("COMBATE ÀS PERDAS")

escolha = st.sidebar.radio("Seleciona a opcao", lista)

if escolha=="CALENDARIO":
    from streamlit_calendar import calendar
    calendario=calendar()
    st.write(calendario)

if escolha=="PERDAS":
   grupo = pd.read_csv("grupo1-4.CSV", sep=";", encoding="latin-1")
   df = pd.DataFrame(grupo)
   st.dataframe(df)



   tab1, tab2 = st.tabs(["Grafico", "Tabela"])
   with tab1:

       resultado1 = df['Data instalação']
       st.bar_chart(resultado1.value_counts())
       #st.bar_chart()

   with tab2:
       colunas = ['HD', 'Data instalação', 'Categoria']
       resultado = df.loc[:, colunas]

       st.dataframe(resultado)


elif escolha=="TESTE SUPABASE":
    from supabase import create_client, Client
    #url: str = os.environ.get("https://ibhcxtnwnonsnycfgjay.supabase.co")
    #key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImliaGN4dG53bm9uc255Y2ZnamF5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxNTM5NjIsImV4cCI6MjAxMDcyOTk2Mn0.PYLOei6RiMbucEqUmTtnmkcjDfIptsiTcNrUCmrBH7c")
    supabase: Client = create_client('https://ibhcxtnwnonsnycfgjay.supabase.co',
                                     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImliaGN4dG53bm9uc255Y2ZnamF5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NTE1Mzk2MiwiZXhwIjoyMDEwNzI5OTYyfQ.W9t9sqi_odq3kV2WovKCVfMXcFGprFOgai9Us9_rTQA')

    resposta = supabase.table("caninos").select("nome").execute()
    st.write(resposta)

    res = supabase.storage.from_('Meninos').get_public_url('Femeas/Betina.jpg')
    st.image(str(res))
