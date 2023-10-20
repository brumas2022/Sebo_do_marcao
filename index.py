import streamlit as st
st.header("Esta é a pagina inicial do Sebo do Marcão")
st.write("---")
st.markdown("vamos comecar a trabalhar nisso aqui")
st.image("IMG_20220616_220024.jpg")
a = st.selectbox("Escolha a opção desejada",("Mandar uma mensagem para o Marcao", "Desejar bom dia ao Marcao", "Desejar boa noite ao Marcao"))
if a == "Mandar uma mensagem para o Marcao":
  nome = st.text_input("Digite seu nome")
  mensagem = st.text_input("Digite a sua mensagem")
elif a == "Desejar bom dia ao Marcao":
  st.markdown("BOM DIA, MARCAO")
elif a ==  "Desejar boa noite ao Marcao":
  st.markdown("BOA NOITE, MARCAO")
  
