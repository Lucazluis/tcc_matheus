import mysql.connector

def iniciarConexao():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="WAGUINHO451",
        database="Agenda"
    )

    return conexao