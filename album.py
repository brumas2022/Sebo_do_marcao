import streamlit as st
import telebot 

st.markdown("Album dos caes abrigado na arpaa")

st.markdown("aqui teremos fotos")
escolha=st.selectbox("o que deseja fazer?", ("voar", "sair", "ouvir"))

CHAVE_API = "6369586964:AAFm3QLWBNnLYUwtl2xyqi0145oYJd8OHNc"

bot = telebot.TeleBot(CHAVE_API)  

if escolha=="ouvir":
   bot.send_message(820304760, "tente ouvir mais do que falar")


if escolha=="voar":
   bot.send_message(820304760, "dê asas a sua imaginacao")

if escolha=="sair":
   oi = st.text_input("digite)
   bot.send_message(820304760, oi)