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
   bot.send_message(820304760, "Hoje temos 64 caes, sendo 34 machos e 30 femeas")


@bot.message_handler(commands=["gatos"])
def gatos(mensagem):
   bot.send_message(820304760, "Temos cerca de 35 gatos atualmente. Todos estao castrados")


@bot.message_handler(commands=["lembretes"])
def lembretes(mensagem):
   
   bot.send_message(820304760, "As proximas a serem castradas deve ser Lucinha, Fiona ou Estiolada")
   bot.send_message(820304760, "Tem ainda a Branquinha, Latoia, Pitoca, Boca e Menininha")


def verificar(mensagem):
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto="""/caes
             /gatos
             /lembretes"""
    bot.reply_to(mensagem, texto)


bot.infinity_polling()
