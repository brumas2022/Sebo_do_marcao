import streamlit as st
nome = st.text_input("Qual é o seu nome?")
senha = st.text_input("E você sabe qual é a senha?")
if senha=="1234":
   st.write(nome+"  clique no botao para acessar o site")
   st.link_button("Memorando agora", "https://comunicasanear-avcnrpqesbpzeg2ecsmuun.streamlit.app/")
