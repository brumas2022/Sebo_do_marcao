import streamlit as st
import telebot 
import psycopg2
import os
from dotenv import load_dotenv
import chatterbot # nao consegui fazer nada aqui

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()
# Acessando a variável de ambiente API_KEY
CHAVE_API = os.getenv("CHAVE_API")

st.title("Este site aciona o bot do telegram sobre os animais")

a=st.text_input("Qual é a senha?")
b=os.getenv("senha")
if a==b:
   st.write("Vc acertou!!!")
   
escolha=st.text_input("Digite sua mensagem")

#CHAVE_API = "6369586964:AAFm3QLWBNnLYUwtl2xyqi0145oYJd8OHNc"

bot = telebot.TeleBot(CHAVE_API)  


bot.send_message(820304760, escolha)



   


##@bot.message_handler(commands=["exibir"])
#def exibir(mensagem):
#   try:
#    connection = psycopg2.connect(
#                   host='aws-0-sa-east-1.pooler.supabase.com',
#                   user='postgres.ibhcxtnwnonsnycfgjay',
#                   password='Hoje#estamos#firmes#como#geleia',
#                   database='postgres',
#                   port='5432'
                   
#    )
#    cursor = connection.cursor()
              
#    comando = f"""SELECT * FROM caninos WHERE genero='macho' and vivo=True"""
#    cursor.execute(comando)
#    resultado = cursor.fetchall()
#    st.write(resultado)
#    ##st.markdown(":dog2: O numero de machos é : "+str(len(resultado)))
#    bot.send_message(820304760, resultado)
#   except Exception as ex
#    bot.send_message(mensagem.chat.id, ex)

@bot.message_handler(commands=["amor"])
def amor(mensagem):
    bot.send_message(820304760, "Vou verificar o que tenho para fazer")
        
@bot.message_handler(commands=["adocao"])
def adocao(mensagem):
    #bot.send_message(820304760, "Hoje nos temos 08 filhotes para doar") 
    bot.send_image(820304760,"zeroum.jpg")
    
@bot.message_handler(commands=["como_ajudar"])
def como_ajudar(mensagem):
    bot.send_message(820304760, "Atraves do PIX 66992097580 você pode ajudar estes animaiszinhos")

@bot.message_handler(commands=["caes"])
def caes(mensagem):
   bot.send_message(820304760, "Hoje temos 64 caes, sendo 34 machos e 30 femeas")


@bot.message_handler(commands=["gatos"])
def gatos(mensagem):
   bot.send_message(820304760, "Temos cerca de 35 gatos atualmente. Todos estao castrados")


@bot.message_handler(commands=["lembretes"])
def lembretes(mensagem):
   

   
   bot.send_message(820304760, "Machos a serem castrados: Gervasio, Zerotres, Jaba, Lobo e filhotes Branquinha. Femea para castrar: Dina, Fiona, Branquinha e Joaninha")
  


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
          /amor"""
    bot.reply_to(mensagem, texto)


bot.infinity_polling()
