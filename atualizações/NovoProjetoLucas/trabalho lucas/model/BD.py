import mysql.connector

def iniciarConexao():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="pitang",
        database="Agenda"
    )

    return conexao
