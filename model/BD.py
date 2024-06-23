import mysql.connector

def iniciaConexao():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="WAGUINHO451",
        database="Agenda"
    )

    return conexao
