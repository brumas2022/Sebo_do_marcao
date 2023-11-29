import streamlit as st
from st_pages import show_pages_from_config, Pages


show_pages_from_config(".streamlit/pages_sections.toml")


st.header(":green[Sebo do Marcão]", divider="orange")
st.markdown("Aqui será possivel encontrar coisas com nexo e também totalmente sem nexo :musical_note:")
st.write("---")
st.markdown("Pensamento do dia: :violet[QUANDO ACABAR O MALUCO SOU EU] :musical_note:")
st.markdown(":sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:")
st.write("---")
st.write("---")
st.image("IMG_20220616_220024.jpg")

cols1 = st.columns((1,1,1))
cols1[0].image("livros-stack-realistic_1284-4735.jpg")
cols1[1].image("livros-stack-realistic_1284-4735.jpg")
cols1[2].image("livros-stack-realistic_1284-4735.jpg")

cols2 = st.columns((1,1,1,1,1,1,1))
cols2[0].image("simbolos-musicais-ondulam-em-fundo-branco_1308-77408.jpg")
cols2[1].image("simbolos-musicais-ondulam-em-fundo-branco_1308-77408.jpg")
cols2[2].image("simbolos-musicais-ondulam-em-fundo-branco_1308-77408.jpg")
cols2[3].image("simbolos-musicais-ondulam-em-fundo-branco_1308-77408.jpg")
cols2[4].image("simbolos-musicais-ondulam-em-fundo-branco_1308-77408.jpg")
cols2[5].image("simbolos-musicais-ondulam-em-fundo-branco_1308-77408.jpg")
cols2[6].image("simbolos-musicais-ondulam-em-fundo-branco_1308-77408.jpg")


                   
                   




cols = st.columns((1,1))
cols[0].link_button("Loja paque menos", "https://mais.app/1Nm5y9", use_container_width=True)
cols[0].link_button("Memorando SANEAR", "https://comunicasanear-avcnrpqesbpzeg2ecsmuun.streamlit.app/", use_container_width=True)
cols[0].link_button("Cadastro de animais", "https://causanimal.streamlit.app", use_container_width=True)
cols[1].link_button("Video do Youtube", "https://www.youtube.com/watch?v=JnxCIRxt3kQ&t=19s", use_container_width=True)
cols[1].link_button("Faça sua doação", "https://www.mercadopago.com.br/integrations/v1/web-payment-checkout.js", use_container_width=True)



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
  
  
