import streamlit as st
import telebot 

st.markdown("Album dos caes abrigado na arpaa")

st.markdown("aqui teremos fotos")


bot = telebot.TeleBot(CHAVE_API)  

        bot.send_message(820304760, nome)
