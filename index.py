import streamlit as st
st.header("Sebo do Marcão")
st.write("---")
st.markdown("Aqui será possivel encontrar coisas com nexo e também totalmente sem nexo")
st.write("---")
st.write("Pensamento do dia: AINDA QUE EU FALASSE A LINGUA DOS HOMENS, SEM AMOR EU NADA SERIA")
st.image("IMG_20220616_220024.jpg")
st.link_button("Loja paque menos", "https://mais.app/1Nm5y9", use_container_width=True)
st.link_button("Memorando SANEAR", "https://comunicasanear-avcnrpqesbpzeg2ecsmuun.streamlit.app/")
st.link_button("Cadastro de animais", "https://causanimal.streamlit.app")
st.link_button("Video do Youtube", "https://www.youtube.com/watch?v=JnxCIRxt3kQ&t=19s")
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
  
