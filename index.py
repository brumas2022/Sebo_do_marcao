import streamlit as st
import telebot
import psycopg2
import os
from dotenv import load_dotenv
from st_pages import show_pages_from_config, add_page_title

def bot_telegram():
    # Carregando as variáveis de ambiente do arquivo .env
    load_dotenv()
    # Acessando a variável de ambiente API_KEY
    CHAVE_API = os.getenv("CHAVE_API")
    st.info("Este site aciona o bot do telegram sobre os animais")
    a=st.text_input("Qual é a senha?")
    b=os.getenv("senha")
    if a==b:
       st.write("Vc acertou!!!")
   
    escolha=st.text_input("Digite sua mensagem")
    bot = telebot.TeleBot(CHAVE_API)  
    bot.send_message(820304760, escolha)

    @bot.message_hanlder(commands=['caes'])
    def caes(mensagem):
            st.write("Ele respondeu caes")
            bot.send_message(820304760, "deu certo")
    
    def verificar(mensagem):
        return True

    @bot.message_handler(func=verificar)
    def responder(mensagem):
        texto="""Escolha uma das opçoes:
              /caes
              /gatos
              /lembretes
              /como_ajudar
              /adocao
              /amigo"""
        bot.reply_to(mensagem, texto)
    
    


senha = st.sidebar.selectbox(
    "Escolha um autor para continuar",
    ("Sheets", "Programas", "Cifras", "Simon")
)
if senha == "Sheets":
  st.sidebar.link_button("Controle de Ponto","https://docs.google.com/spreadsheets/d/1CcE0dc60ezKeIVTOlXOoM42UBDve46HI4GTSxIs_qY0/edit?gid=577486192#gid=577486192")

if senha=="Programas":
    st.sidebar.link_button("Memorando SANEAR", "https://comunicasanear-avcnrpqesbpzeg2ecsmuun.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Cadastro de animais", "https://causanimal.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Galeria de fotos", "https://galeria.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Controle de Estoque", "https://estoque1.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Video do Youtube", "https://www.youtube.com/watch?v=JnxCIRxt3kQ&t=19s", use_container_width=True)
    st.sidebar.link_button("Faça sua doação", "https://www.mercadopago.com.br/integrations/v1/web-payment-checkout.js", use_container_width=True)
    st.sidebar.link_button("Lojinha", "https://loja1dosebo.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Aciona Telegram", "https://sebodomarcao-g4cnpbtuc8aclncvnvzr4e.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Sobre museu Rosa Bororo - fonte: ATribunamt", "https://www.atribunamt.com.br/opiniao-do-leitor/2024/05/entre-o-passado-e-o-futuro-o-papel-do-museu-rosa-bororo-na-historia-em-rondonopolis/", use_container_width=True)
    st.sidebar.link_button("Condominio Brumatti", "http://inquilinos.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Projeto Modernizacao", "http://controle1.streamlit.app", use_container_width=True)

    #st.sidebar.markdown(":red[Trabalhadores de todo mundo, UNI-VOS]")
    #st.sidebar.markdown(":sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:")

if senha=="Cifras":
    
    st.sidebar.link_button("Aluga se", "https://www.cifraclub.com.br/raul-seixas/aluga-se/", use_container_width=True)
    st.sidebar.link_button("Flor e o beija flor", "https://www.cifraclub.com.br/henrique-e-juliano/flor-e-o-beija-flor/", use_container_width=True)
    st.sidebar.markdown(":sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:")

if senha=="Simon":
    st.sidebar.markdown(":violet[Aquele que serve a uma revolução ara no mar]")
    st.sidebar.markdown(":musical_note:")
    st.sidebar.audio("06-Hc3", format="audip/mpeg")


st.header(":green[Sebo do Marcão]", divider="orange")
st.markdown("Tente fazer coisas diferentes para melhorar o seu dia :musical_note:")
st.write("---")
#st.image("IMG_20220616_220024.jpg")
st.image("crie_uma_imagem_de_um_violao_inteirona_diagonal_ladeado_por_livros_e_notas_musicais_png.png")



cols = st.columns((1,1,1,1,1))
cols[0].link_button("PCI", "https://www.pciconcursos.com.br/", use_container_width=True)
cols[1].link_button("SANEAR", "https://www.sanearmt.com.br", use_container_width=True)
cols[2].link_button("PREFEITURA", "http://www.rondonopolis.mt.gov.br", use_container_width=True)
cols[3].link_button("A TRIBUNA", "https://www.atribunamt.com.br", use_container_width=True)
cols[4].link_button("CATRACA", "https://catracalivre.com.br/", use_container_width=True)


a = st.selectbox("Escolha a opção desejada",("Mensagem para o Marcao", "Desejar bom dia ao Marcao", "Desejar boa noite ao Marcao", "Telegram"))
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
elif a == "Telegram":
  bot_telegram()  
  
  
