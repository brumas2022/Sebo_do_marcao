import streamlit as st
import telebot
import psycopg2
import os
from dotenv import load_dotenv
from st_pages import show_pages_from_config, add_page_title
import requests




senha = st.sidebar.selectbox(
    "Escolha um autor para continuar",
    ("Appsmith", "Programas", "Cifras", "Musicas")
)
if senha == "Appsmith":
   caminho = "https://sanear.appsmith.com" 
   st.sidebar.link_button("Cadastro de Atividades", caminho)

if senha=="Programas":
    st.sidebar.link_button("Memorando SANEAR", "https://comunicasanear-avcnrpqesbpzeg2ecsmuun.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Cadastro de animais", "https://causanimal.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Galeria de fotos", "https://galeria.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Controle de Estoque", "https://estoque1.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Video do Youtube", "https://www.youtube.com/watch?v=JnxCIRxt3kQ&t=19s", use_container_width=True)
    st.sidebar.link_button("Abertura SANEAR", "https://abertura.streamlit.app", use_container_width=True)
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
    surfin = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/20%20-%20Surfin%20Bird.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvMjAgLSBTdXJmaW4gQmlyZC5tcDMiLCJpYXQiOjE3MzE2MTUyODgsImV4cCI6MTczNDIwNzI4OH0.uYKjP4pROOOZmUdHR1SppybMrYbxAKYv5T33xWf8ifE&t=2024-11-14T20%3A15%3A22.667Z'
    cantares = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/01-Cantares.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy8wMS1DYW50YXJlcy5tcDMiLCJpYXQiOjE3MzE2MTUwMzcsImV4cCI6MTczNDIwNzAzN30.QYl4S-YOaxFR-ADZfOm9i9-sgWMF6ku9c54nHToNhA0&t=2024-11-14T20%3A11%3A11.889Z'
    chico = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Chico%20Buarque%20-%20Vai%20Passar.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9DaGljbyBCdWFycXVlIC0gVmFpIFBhc3Nhci5tcDMiLCJpYXQiOjE3MzI1NjEwNzEsImV4cCI6MTc2NDA5NzA3MX0.w_oB288ldIZaC15_J2na5OlhW2xu_ypUv_ZCA0Zb3BQ&t=2024-11-25T18%3A57%3A51.202Z'
    abreu = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Fernanda%20Abreu%20-%20Katia%20Flavia.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9GZXJuYW5kYSBBYnJldSAtIEthdGlhIEZsYXZpYS5tcDMiLCJpYXQiOjE3MzI1NjExMTcsImV4cCI6MTc2NDA5NzExN30.5FNWk3kCm-KwrmKrPMhE7zVe4BvymEwEzLHlMt6j6Vs&t=2024-11-25T18%3A58%3A38.225Z'
    bohe = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Queen%20-%20Bohemian%20Rhapsody.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9RdWVlbiAtIEJvaGVtaWFuIFJoYXBzb2R5Lm1wMyIsImlhdCI6MTczMjU2MTE1MSwiZXhwIjoxNzY0MDk3MTUxfQ.fmpVTG9ZiXvLu7J9-0ztlYaJCRkYX7YUFJOEroY0sWc&t=2024-11-25T18%3A59%3A12.014Z'
    pedro = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Raul%20Seixas%20-%20Meu%20Amigo%20Pedro.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9SYXVsIFNlaXhhcyAtIE1ldSBBbWlnbyBQZWRyby5tcDMiLCJpYXQiOjE3MzI1NjExNzYsImV4cCI6MTc2NDA5NzE3Nn0.BWtQzY4eZiPUBttNE9xCbgGm8OHck8g9xcZZkJfWqrM&t=2024-11-25T18%3A59%3A36.950Z'
    zegeraldo = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Ze%20Geraldo%20-%20Meiga%20Senhorita.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9aZSBHZXJhbGRvIC0gTWVpZ2EgU2VuaG9yaXRhLm1wMyIsImlhdCI6MTczMjU2NTk4MywiZXhwIjoxNzY0MTAxOTgzfQ.Ifu6e3bbQA7SPz7403G7JoQ036C1_tHeOSEJvIbTkYg&t=2024-11-25T20%3A19%3A43.675Z' 
    
    #audio1_file = open('https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-10/01-Cantares.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMC8wMS1DYW50YXJlcy5tcDMiLCJpYXQiOjE3MzA5MjIxMDYsImV4cCI6MTczMTUyNjkwNn0.E7gXHtius5OTuz6slQvzV3B367HdPwW86WChKAE_Jpw&t=2024-11-06T19%3A42%3A18.206Z', 'rb')
    #audio1_bytes = audio1_file.read()
    st.sidebar.audio(cantares, format='audio/mpeg')
    st.sidebar.audio(surfin, format='audio/mpeg')
    st.sidebar.audio(chico, format='audio/mpeg')
    st.sidebar.audio(abreu, format='audio/mpeg')
    st.sidebar.audio(bohe, format='audio/mpeg')
    st.sidebar.audio(pedro, format='audio/mpeg')
    st.sidebar.audio(zegeraldo, format='audio/mpeg')

st.header(":green[Sebo do Marcão]", divider="orange")
link_api="https://api.adviceslip.com/advice"
resposta = requests.get(link_api)
dados_requisicao = resposta.json()
conselho = dados_requisicao['slip']['advice']
st.markdown(conselho)
st.write("---")
#st.image("IMG_20220616_220024.jpg")
#st.image("crie_uma_imagem_de_um_violao_inteirona_diagonal_ladeado_por_livros_e_notas_musicais_png.png")
st.image("a_colorful_image_o_image_.jpg")


cols = st.columns((0.75,1,1.25,1,1,1))
cols[0].link_button("PCI", "https://www.pciconcursos.com.br/", use_container_width=True)
cols[1].link_button("SANEAR", "https://www.sanearmt.com.br", use_container_width=True)
cols[2].link_button("PREFEITURA", "http://www.rondonopolis.mt.gov.br", use_container_width=True)
cols[3].link_button("A TRIBUNA", "https://www.atribunamt.com.br", use_container_width=True)
cols[4].link_button("CATRACA", "https://catracalivre.com.br/", use_container_width=True)
cols[5].link_button("DOU", "https://www.in.gov.br/servicos/diario-oficial-da-uniao", use_container_width=True)


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

  
  
  
