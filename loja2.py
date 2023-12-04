import streamlit as st
nome = st.text_input("entre com login")
senha = st.text_input("entre com a senha")
if senha=="1234":
   st.write(nome+"  clique no botao para acessar o site")
   st.link_button("Memorando agora", "https://comunicasanear-avcnrpqesbpzeg2ecsmuun.streamlit.app/")
