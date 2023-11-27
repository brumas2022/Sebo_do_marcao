import streamlit as st
st.header("Sebo do Marcão", divider="orange")
st.markdown("Aqui será possivel encontrar coisas com nexo e também totalmente sem nexo :sunglasses:")
st.write("---")
st.markdown("Pensamento do dia: TUDO QUE VIER NA CABEÇA EU VOU CANTAR :sunglasses:")
st.markdown(":sunglasses:   :sunglasses:")
st.write("---")
st.write("---")
st.image("IMG_20220616_220024.jpg")

cols = st.columns((1,1))
cols[0].link_button("Loja paque menos", "https://mais.app/1Nm5y9", use_container_width=True)
cols[0].link_button("Memorando SANEAR", "https://comunicasanear-avcnrpqesbpzeg2ecsmuun.streamlit.app/", use_container_width=True)
cols[0].link_button("Cadastro de animais", "https://causanimal.streamlit.app", use_container_width=True)
cols[1].link_button("Video do Youtube", "https://www.youtube.com/watch?v=JnxCIRxt3kQ&t=19s", use_container_width=True)
cols[1].link_button("Faça sua doação", "https://www.mercadopago.com.br/integrations/v1/web-payment-checkout.js", use_container_width=True)

cols1 = st.columns((1,1,1))
cols1[0].image("https://www.google.com/imgres?imgurl=https://img.freepik.com/vetores-gratis/pilha-de-livros-de-design-plano-desenhado-a-mao_23-2149334862.jpg?w%3D2000&imgrefurl=https://br.freepik.com/fotos-vetores-gratis/livros&h=2000&w=2000&tbnid=nlMZ85YVaNd4YM&tbnh=225&tbnw=225&usg=AI4_-kRCyHWxDuAt2tA2LAjcTO-AwFcZ-g&vet=1&docid=0fILTN0CAh0EoM")
cols1[1].image("IMG_20220616_220024.jpg")
cols1[2].image("IMG_20220616_220024.jpg")

a = st.selectbox("Escolha a opção desejada",("Mensagem para o Marcao", "Desejar bom dia ao Marcao", "Desejar boa noite ao Marcao"))
if a == "Mensagem para o Marcao":
  nome = st.text_input("Digite seu nome")
  prompt = st.chat_input("Say something")
  if prompt:
      st.write(f"{nome} enviou a seguinte mensagem : {prompt}")
elif a == "Desejar bom dia ao Marcao":
  st.markdown("BOM DIA, MARCAO")
  st.markdown("Com fé, chegamos la")
  st.balloons()
elif a ==  "Desejar boa noite ao Marcao":
  st.markdown("BOA NOITE, MARCAO")
  st.markdown("Durma com os anjos")
  st.snow()
  st.write("---")
  
  
