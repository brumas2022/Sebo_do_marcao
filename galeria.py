import pandas as pd
from sqlalchemy import create_engine, text
import streamlit as st

st.set_page_config(layout="wide")

st.header("Animais abrigados na chacara mantida por voluntários da ARPAA")
st.write("Eles recebem agua, alimentação, medicação e abrigo contra sol e chuva...tudo na medida do possível")
st.write("As ajudas podem ser feitas através do PIX 66992097580")

engine = create_engine('postgresql://postgres.ibhcxtnwnonsnycfgjay:Hoje#estamos#firmes#como#geleia@aws-0-sa-east-1.pooler.supabase.com:5432/postgres')
#engine = create_engine('postgresql://postgres:Lula#2022@localhost:5432/postgres')
sql = "SELECT * FROM caninos"
df = pd.read_sql_query(sql, con=engine)

df_filtro = df[df["foto"]!=""]
df_filtro = df_filtro.set_index('id')
#st.dataframe(df_filtro)
col1, col2, col3, col4 = st.columns((1,1,1,1))
col1.image(df_filtro['foto'][54], caption=df_filtro['nome'][54], use_column_width="always")
col2.image(df_filtro['foto'][32], caption=df_filtro['nome'][32], use_column_width="always")
col3.image(df_filtro['foto'][51], caption=df_filtro['nome'][51], use_column_width="always")
col4.image(df_filtro['foto'][41], caption=df_filtro['nome'][41], use_column_width="always")

col1.image(df_filtro['foto'][18], caption=df_filtro['nome'][18], use_column_width="always")
col2.image(df_filtro['foto'][10], caption=df_filtro['nome'][10], use_column_width="always")
col3.image(df_filtro['foto'][38], caption=df_filtro['nome'][38], use_column_width="always")
col4.image(df_filtro['foto'][57], caption=df_filtro['nome'][57], use_column_width="always")

col1.image(df_filtro['foto'][49], caption=df_filtro['nome'][49], use_column_width="always")
col2.image(df_filtro['foto'][35], caption=df_filtro['nome'][35], use_column_width="always")
col3.image(df_filtro['foto'][39], caption=df_filtro['nome'][39], use_column_width="always")
col4.image(df_filtro['foto'][14], caption=df_filtro['nome'][14], use_column_width="always")

col1.image(df_filtro['foto'][34], caption=df_filtro['nome'][34], use_column_width="always")
col2.image(df_filtro['foto'][7], caption=df_filtro['nome'][7], use_column_width="always")
col3.image(df_filtro['foto'][23], caption=df_filtro['nome'][23], use_column_width="always")
col4.image(df_filtro['foto'][29], caption=df_filtro['nome'][29], use_column_width="always")
  
col1.image(df_filtro['foto'][16], caption=df_filtro['nome'][16], use_column_width="always")
col2.image(df_filtro['foto'][26], caption=df_filtro['nome'][26], use_column_width="always")
col3.image(df_filtro['foto'][17], caption=df_filtro['nome'][17], use_column_width="always")
col4.image(df_filtro['foto'][8], caption=df_filtro['nome'][8], use_column_width="always")

col1.image(df_filtro['foto'][13], caption=df_filtro['nome'][13], use_column_width="always")
col2.image(df_filtro['foto'][55], caption=df_filtro['nome'][55], use_column_width="always")
col3.image(df_filtro['foto'][58], caption=df_filtro['nome'][58], use_column_width="always")
col4.image(df_filtro['foto'][42], caption=df_filtro['nome'][42], use_column_width="always")

col1.image(df_filtro['foto'][26], caption=df_filtro['nome'][26], use_column_width="always")
col2.image(df_filtro['foto'][16], caption=df_filtro['nome'][16], use_column_width="always")
col3.image(df_filtro['foto'][23], caption=df_filtro['nome'][23], use_column_width="always")
col4.image(df_filtro['foto'][19], caption=df_filtro['nome'][19], use_column_width="always")

col1.image(df_filtro['foto'][33], caption=df_filtro['nome'][33], use_column_width="always")
col2.image(df_filtro['foto'][44], caption=df_filtro['nome'][44], use_column_width="always")
col3.image(df_filtro['foto'][46], caption=df_filtro['nome'][46], use_column_width="always")
col4.image(df_filtro['foto'][47], caption=df_filtro['nome'][47], use_column_width="always")

col1.image(df_filtro['foto'][4], caption=df_filtro['nome'][4], use_column_width="always")
col2.image(df_filtro['foto'][27], caption=df_filtro['nome'][27], use_column_width="always")
col3.image(df_filtro['foto'][63], caption=df_filtro['nome'][63], use_column_width="always")
col4.image(df_filtro['foto'][37], caption=df_filtro['nome'][37], use_column_width="always")

col1.image(df_filtro['foto'][40], caption=df_filtro['nome'][40], use_column_width="always")
col2.image(df_filtro['foto'][6], caption=df_filtro['nome'][6], use_column_width="always")
col3.image(df_filtro['foto'][28], caption=df_filtro['nome'][28], use_column_width="always")
col4.image(df_filtro['foto'][9], caption=df_filtro['nome'][9], use_column_width="always")



