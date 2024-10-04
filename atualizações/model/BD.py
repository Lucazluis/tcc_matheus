import mysql.connector

# def iniciarConexao():
#     conexao = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="WAGUINHO451",
#         database="Agenda"
#     )
#     return conexao

# import mysql.connector 

def iniciarConexao():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="WAGUINHO451",
            database="Agenda"
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None