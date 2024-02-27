import streamlit as st
import telebot 

st.markdown("Album dos caes abrigado na arpaa")

st.markdown("aqui teremos fotos")


CHAVE_API = "6369586964:AAFm3QLWBNnLYUwtl2xyqi0145oYJd8OHNc"

bot = telebot.TeleBot(CHAVE_API)  

        bot.send_message(820304760, nome)
