import streamlit as st
from st_pages import show_pages_from_config, add_page_title

#add_page_title()
#show_pages_from_config(".streamlit/pages.toml")

senha = st.sidebar.selectbox(
    "Escolha um autor para continuar",
    ("Sheets", "Programas", "Che", "Simon")
)
if senha == "Sheets":
  st.sidebar.link_button("Controle de Ponto","https://docs.google.com/spreadsheets/d/1CcE0dc60ezKeIVTOlXOoM42UBDve46HI4GTSxIs_qY0/edit#gid=69725999")

if senha=="Programas":
    st.sidebar.link_button("Memorando SANEAR", "https://comunicasanear-avcnrpqesbpzeg2ecsmuun.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Cadastro de animais", "https://causanimal.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Galeria de fotos", "https://galeria.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Plano de Saneamento Sanear", "https://drive.google.com/file/d/1yDofmyFtOFxvmvhrWFx-ql-Odxt5Mdho/view", use_container_width=True)
    st.sidebar.link_button("Video do Youtube", "https://www.youtube.com/watch?v=JnxCIRxt3kQ&t=19s", use_container_width=True)
    st.sidebar.link_button("Faça sua doação", "https://www.mercadopago.com.br/integrations/v1/web-payment-checkout.js", use_container_width=True)
    st.sidebar.link_button("Lojinha", "https://loja1dosebo.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Aciona Telegram", "https://sebodomarcao-g4cnpbtuc8aclncvnvzr4e.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Sobre museu Rosa Bororo - fonte: ATribunamt", "https://www.atribunamt.com.br/opiniao-do-leitor/2024/05/entre-o-passado-e-o-futuro-o-papel-do-museu-rosa-bororo-na-historia-em-rondonopolis/", use_container_width=True)
    st.sidebar.link_button("Condominio Brumatti", "http://inquilinos.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Projeto Modernizacao", "http://controle1.streamlit.app", use_container_width=True)

    #st.sidebar.markdown(":red[Trabalhadores de todo mundo, UNI-VOS]")
    #st.sidebar.markdown(":sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:")

if senha=="Che":
    st.sidebar.markdown(":red[Hasta la victoria siempre]")
    st.sidebar.markdown(":sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:")

if senha=="Simon":
    st.sidebar.markdown(":violet[Aquele que serve a uma revolução ara no mar]")
    st.sidebar.markdown(":musical_note:")


st.header(":green[Sebo do Marcão]", divider="orange")
st.markdown("Aqui será possivel encontrar coisas com nexo e também totalmente sem nexo :musical_note:")
st.write("---")
#st.image("IMG_20220616_220024.jpg")
st.image("crie_uma_imagem_de_um_violao_inteirona_diagonal_ladeado_por_livros_e_notas_musicais_png.png")



cols = st.columns((1,1,1,1,1))
cols[0].link_button("F1", "https://www.uol.com.br", use_container_width=True)
cols[1].link_button("F2", "https://www.sanearmt.com.br", use_container_width=True)
cols[2].link_button("F3", "http://www.rondonopolis.mt.gov.br", use_container_width=True)
cols[3].link_button("F4", "https://www.atribunamt.com.br", use_container_width=True)
cols[4].link_button("F5", "https://www.agoramt.com.br", use_container_width=True)


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
  st.markdown("Espero estar melhor no outro dia....boa noite")
  st.snow()
  st.write("---")
  
  
