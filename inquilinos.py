import streamlit as st
import psycopg2
import pandas as pd




st.set_page_config(page_title="Caes abrigados", layout="wide")

def apresenta():
    try:
        
        connection = psycopg2.connect(
                   host='aws-0-sa-east-1.pooler.supabase.com',
                   user='postgres.ibhcxtnwnonsnycfgjay',
                   password='Hoje#estamos#firmes#como#geleia',
                   database='postgres',
                   port='5432'
                   ##host='db.ibhcxtnwnonsnycfgjay.supabase.co',
                   ##user='postgres',
                   ##password='Hoje#estamos#fortes#como#geleia',
                   ##database='postgres',
                   ##port= '5432'
        )
        st.write("conexao exitosa")
        cursor = connection.cursor()
        
        
        comando = f"""SELECT * FROM caninos WHERE genero='macho' and vivo=True"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":dog2: O numero de machos é : "+str(len(resultado)))

        comando = f"""SELECT * FROM caninos WHERE genero='femea' and vivo=True"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":dog: O numero de femeas é : "+ str(len(resultado)))

        comando = f"""SELECT * FROM caninos WHERE castrado=True"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":sunglasses: :sunglasses: O numero de castrados é : "+str(len(resultado)))
       
        comando = f"""SELECT * FROM caninos WHERE vivo=True"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":sunglasses: :sunglasses: O numero de total é : "+str(len(resultado)))

        
        
    except Exception as ex:
            st.write(ex)
    
    #st.column_config.ImageColumn(label="12", width="small", help=None)
    #st.dataframe(resultado)
    st.data_editor(resultado,column_config={"12": st.column_config.ImageColumn("Preview Image", help="Streamlit app preview screenshots")}, hide_index=True,)

def inserir(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12):
    try:
     connection = psycopg2.connect(
               host='aws-0-sa-east-1.pooler.supabase.com',
               user='postgres.hdhvkseneldllvnlvpgc',
               password='Hoje#estamos#firmes#como#geleia',
               database='postgres',
               port='5432'


        
               ##host='db.ibhcxtnwnonsnycfgjay.supabase.co',
               ##user='postgres',
               ##password='Hoje#estamos#fortes#como#geleia',
               ##database='postgres',
               ##port='5432'
     )
     st.write("conexao exitosa")

     cursor = connection.cursor()



     comando = f"""INSERT INTO saobernardo (nome, cpf, rg, civil, entrada, saida, contato, casa, prazo, foto, conjuge, historico) VALUES ('{a1}', '{a2}', '{a3}', '{a4} ', '{a5}', '{a6}', '{a7}', '{a8}', '{a9}', '{a10} ', '{a11}', '{a12} ')"""
     

     cursor.execute(comando)
     connection.commit()
     st.text("Cadastro efetuado com sucesso")
     cursor.close()
     connection.close()

          
    except Exception as ex:
            st.write(ex)

def captura():
    with st.form("Caputar dados", clear_on_submit=True):
        col = st.columns((1,1))
        a1 = col[0].text_input("Nome do inquilino(a)")
        a2 = col[0].text_input("CPF")
        a3 = col[0].text_input("RG")
        a4 = col[0].text_input("Estado civil")
        a5 = col[0].date_input("Data da entrada no imovel")
        a6 = col[0].date_input("Data da saida do imovel")
        a7 = col[1].text_input("Telefone de contato")
        a8 = col[1].text_input("Casa alugada")
        a9 = col[1].text_input("Prazo do contrato")
        a10 = col[1].text_input("Foto do documento")
        a11 = col[1].text_input("Nome do conjuge")
        a12 = col[1].text_input("Historico do inquilino")
        enviar = st.form_submit_button()
        if enviar:
            inserir(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)
        
def consulta():
    
    ##nome1 = st.radio("Escolha o nome", ("Bob", "Gorda", "Mosquito", "Baby", "Jhony", "Margarete", "Vira lata", "Magrelo", "Jair", "Branquelo", "Boca preta", "Betina"))
    cols = st.columns((1,1,1))              
    
    try:
        
        connection = psycopg2.connect(
                   host='aws-0-sa-east-1.pooler.supabase.com',
                   user='postgres.ibhcxtnwnonsnycfgjay',
                   password='Hoje#estamos#firmes#como#geleia',
                   database='postgres',
                   port='5432'
            
                   ##ANTIGA CONFIGURACAO DO DATABASE
                   ##host='db.ibhcxtnwnonsnycfgjay.supabase.co',
                   ##user='postgres',
                   ##password='Hoje#estamos#fortes#como#geleia',
                   ##database='postgres',
                   ##port= '5432'
        )

        cursor = connection.cursor()
       
        caozinho = f"""SELECT nome FROM caninos"""
        cursor.execute(caozinho)
        nome2 = cursor.fetchall()
        df = pd.DataFrame(nome2)
        nome2 = df[0].tolist()
        
        nome1 = cols[0].radio("Escolha o caozinho", (nome2))
        
        
        
        comando = f"""SELECT * FROM caninos WHERE nome='{nome1}'"""
        cursor.execute(comando)
        resultado = cursor.fetchone()
    except Exception as ex:
            st.write(ex)
        
    if resultado[14]==True:
       cols[2].markdown("***Animal castrado(a)***")
    
    cols[2].markdown("Nome : "+resultado[2])
    cols[2].markdown("Genero : "+resultado[3])
    cols[1].image(resultado[12])
    cols[2].markdown("Data entrada :"+resultado[4].strftime("%d/%m/%y"))
    cols[2].markdown("Historia :"+resultado[13])
    


st.title("Cadastro dos inquilinos")
st.divider()
selecao = st.selectbox("Escolha o modulo", ("CADASTRAR", "CONSULTAR", "REMOVER", "CONTRATO"))
if selecao == "CADASTRAR":
    captura()
    
elif selecao == "CONSULTAR":
    consulta()
    
elif selecao == "REMOVER":
    st.text("Este modulo ainda está em construção")
    
elif selecao == "CONTRATO":
    apresenta()
    
    
