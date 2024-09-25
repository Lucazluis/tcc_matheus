import sqlite3
import model.BD as BD
from mysql.connector import Error 

def listar_servicos():
    conexao  = BD.iniciarConexao()
    cursor = conexao.cursor()
    query = "SELECT * FROM servico"

    cursor.execute(query)
    resultados = cursor.fetchall()
    
    print(resultados)
    cursor.close()
    conexao.close()
    return resultados

