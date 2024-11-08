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
    ("Sheets", "Programas", "Cifras", "Musicas")
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

if senha=="Musicas":
    st.sidebar.markdown(":violet[Aquele que serve a uma revolução ara no mar]")
    #st.sidebar.markdown(":musical_note:")
    #st.sidebar.audio("Eu Amo Esse Homem (Trecho).mp3", loop=True)
    #audio_file = open('06-Hc3.mp3','rb') #enter the filename with filepath
    #audio_bytes = audio_file.read() #reading the file
    st.sidebar.write("HC3")
    #st.sidebar.audio(audio_bytes, format='audio/mpeg') #displaying the audio
    st.sidebar.audio('06-Hc3.mp3',format='audio/mpeg')
    chico = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Chico%20Buarque%20-%20Vai%20Passar.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9DaGljbyBCdWFycXVlIC0gVmFpIFBhc3Nhci5tcDMiLCJpYXQiOjE3MzEwOTM1ODksImV4cCI6MTczMTY5ODM4OX0.HpkFzg_DiS4OGcXeq5OdHT_lJz5CjXkYD2Uw4E8vLrI&t=2024-11-08T19%3A20%3A21.079Z'
    abreu = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Fernanda%20Abreu%20-%20Katia%20Flavia.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9GZXJuYW5kYSBBYnJldSAtIEthdGlhIEZsYXZpYS5tcDMiLCJpYXQiOjE3MzEwOTM3ODUsImV4cCI6MTczMTY5ODU4NX0.tHCZKrnSR_xhLnoBaUxJiOvkXqdFWB_nIni-2jUjtSw&t=2024-11-08T19%3A23%3A36.944Z'
    bohe = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Queen%20-%20Bohemian%20Rhapsody.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9RdWVlbiAtIEJvaGVtaWFuIFJoYXBzb2R5Lm1wMyIsImlhdCI6MTczMTA5MzgzMSwiZXhwIjoxNzMxNjk4NjMxfQ.7fO9M8yi6-G-ZoqcBrH6cCBFKiannEiDS1n9zEpF30Q&t=2024-11-08T19%3A24%3A23.095Z'
    pedro = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Raul%20Seixas%20-%20Meu%20Amigo%20Pedro.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9SYXVsIFNlaXhhcyAtIE1ldSBBbWlnbyBQZWRyby5tcDMiLCJpYXQiOjE3MzEwOTM4NzksImV4cCI6MTczMTY5ODY3OX0.nnSH_99lX-4Il1yVD5Fc6Pg_mBrJGm86K8C6Ea8yh8U&t=2024-11-08T19%3A25%3A11.592Z'
    
    #audio1_file = open('https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-10/01-Cantares.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMC8wMS1DYW50YXJlcy5tcDMiLCJpYXQiOjE3MzA5MjIxMDYsImV4cCI6MTczMTUyNjkwNn0.E7gXHtius5OTuz6slQvzV3B367HdPwW86WChKAE_Jpw&t=2024-11-06T19%3A42%3A18.206Z', 'rb')
    #audio1_bytes = audio1_file.read()
    st.sidebar.audio('https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-10/01-Cantares.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMC8wMS1DYW50YXJlcy5tcDMiLCJpYXQiOjE3MzA5MjIxMDYsImV4cCI6MTczMTUyNjkwNn0.E7gXHtius5OTuz6slQvzV3B367HdPwW86WChKAE_Jpw&t=2024-11-06T19%3A42%3A18.206Z', format='audio/mpeg')
    st.sidebar.audio('https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-10/20%20-%20Surfin%20Bird.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMC8yMCAtIFN1cmZpbiBCaXJkLm1wMyIsImlhdCI6MTczMDkyMzQ4OCwiZXhwIjoxNzMxNTI4Mjg4fQ.mNNoIYEqdplTWToCSJA624OHxBpro9n4yULJUxtcOgc&t=2024-11-06T20%3A05%3A19.937Z', format='audio/mpeg')
    st.sidebar.audio(chico, format='audio/mpeg')
    st.sidebar.audio(abreu, format='audio/mpeg')
    st.sidebar.audio(bohe, format='audio/mpeg')
    st.sidebar.audio(pedro, format='audio/mpeg')

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
  
  
