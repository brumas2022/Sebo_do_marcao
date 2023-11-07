import streamlit as st
st.header("Sebo do Marcão")
st.write("---")
st.markdown("Aqui será possivel encontrar coisas com nexo e também totalmente sem nexo")
st.image("IMG_20220616_220024.jpg")
st.link_button("Loja paque menos", "https://mais.app/1Nm5y9")
st.link_button("Memorando SANEAR", "https://www.sanearmt.com.br")
st.link_button("Cadastro de animais", "https://causanimal.streamlit.app")
a = st.selectbox("Escolha a opção desejada",("Mandar uma mensagem para o Marcao", "Desejar bom dia ao Marcao", "Desejar boa noite ao Marcao"))
if a == "Mandar uma mensagem para o Marcao":
  nome = st.text_input("Digite seu nome")
  prompt = st.chat_input("Say something")
  if prompt:
      st.write(f"{nome} enviou a seguinte mensagem : {prompt}")
elif a == "Desejar bom dia ao Marcao":
  st.markdown("BOM DIA, MARCAO")
  st.markdown("Com fé, chegamos la")
elif a ==  "Desejar boa noite ao Marcao":
  st.markdown("BOA NOITE, MARCAO")
  st.markdown("Durma com os anjos")
  st.write("---")
  
