#crud para medicoa#
import mysql.connector
from mysql.connector import Error

def iniciarConexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WAGUINHO451",
            database="Agenda"
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def adiciona_medico(nome, crm):
     conexao = iniciarConexao()
     if conexao is not None:
         try:
             cursor = conexao.cursor()
             comando_medico = 'INSERT INTO medico (nome, crm) VALUES (%s, %s)'
             cursor.execute(comando_medico, (nome, crm))
             conexao.commit()
         except Error as e:
             print(f"Erro ao executar o comando de inserção: {e}")
         finally:
            cursor.close()
            conexao.close()

def listar_medicos():
    conexao = iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'SELECT * FROM medico'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            return resultado
        except Error as e:
            print(f"Erro ao executar o comando de seleção: {e}")
            return []
        finally:
            cursor.close()
            conexao.close()

def atualizar_medico(id, nome, crm):
     conexao = iniciarConexao()
     if conexao is not None:
         try:
             cursor = conexao.cursor()
             comando = 'UPDATE medico SET nome = %s, crm = %s WHERE id = %s'
             cursor.execute(comando, (nome, crm, id))
             conexao.commit()
         except Error as e:
             print(f"Erro ao executar o comando de atualização: {e}")
         finally:
             cursor.close()
             conexao.close()

def deletar_medico(id_medico):
    conexao = iniciarConexao()
    if conexao is not None:
         try:
             cursor = conexao.cursor()
             comando = 'DELETE FROM medico WHERE id = %s'
             cursor.execute(comando, [id_medico])
             conexao.commit()
         except Error as e:
             print(f"Erro ao executar o comando de exclusão: {e}")
         finally:
             cursor.close()
             conexao.close()    