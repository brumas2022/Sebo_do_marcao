import streamlit as st
import telebot
st.markdown("RECANTO DOS USADOS")
st.image("IMG_20220616_220024.jpg")
st.markdown("PREÇO : 250,00")
CHAVE_API = "6253633084:AAEDJfuYUyNWydjAJR4dsZUh3vZGmLfSUps"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)

def responder(mensagem):
    texto = """
    /SERVICO
    Reservatorios
    -----------------------------------------"""
    bot.send_message(mensagem.chat.id, "Escolha elevatoria ")

bot.infinity_polling()
