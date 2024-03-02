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
   bot.send_message(820304760, "nao pense nisso")

if escolha=="sair":
   oi = st.text_input("digite")
   bot.send_message(820304760, oi)


@bot.message_handler(commands=["caes"])
def caes(mensagem):
   bot.send_message(820304760, "Voce entrou na area de caes. Cuidado!!")


@bot.message_handler(commands=["gatos"])
def gatos(mensagem):
   bot.send_message(820304760, "Eu acho que eu vi um gatinho!!")


@bot.message_handler(commands=["lembretes"])
def lembretes(mensagem):
   bot.send_message(820304760, "Voce entrou na area de caes. Cuidado!!")

def verificar(mensagem):
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto="""/caes
             /gatos
             /lembretes"""
    bot.reply_to(mensagem, texto)


bot.infinity_polling()
