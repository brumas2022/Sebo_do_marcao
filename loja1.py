import streamlit as st
import telebot
st.markdown("RECANTO DOS USADOS")
st.image("IMG_20220616_220024.jpg")
st.markdown("PREÇO : 250,00")
CHAVE_API = "6253633084:AAEDJfuYUyNWydjAJR4dsZUh3vZGmLfSUps"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["servico"])
def servico(mensagem):
    bot.reply_to(mensagem, "Este servico ficara disponivel a partir de amanha")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)

def responder(mensagem):
    texto = """
    /servico
    /mat
    /caes
    """
     bot.reply_to(mensagem, texto)
    ##bot.send_message(mensagem.chat.id, "Escolha elevatoria ")

bot.infinity_polling()
