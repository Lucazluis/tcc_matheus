#cod para o crud da tabela servico#
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

def criar_servico(descricao, nomeServico):
    conexao = iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_servico = 'INSERT INTO servico (descricao, nomeServico) VALUES (%s, %s)'
            cursor.execute(comando_servico, (descricao, nomeServico))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()

def listar_servicos():
    conexao = iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'SELECT * FROM servico'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            return resultado
        except Error as e:
            print(f"Erro ao executar o comando de seleção: {e}")
            return []
        finally:
            cursor.close()
            conexao.close()

def atualizar_servico(id_servico, descricao_nova, nomeServico_novo):
    conexao = iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'UPDATE servico SET descricao = %s, nomeServico = %s WHERE id = %s'
            cursor.execute(comando, (descricao_nova, nomeServico_novo, id_servico))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de atualização: {e}")
        finally:
            cursor.close()
            conexao.close()

def deletar_servico(id_servico):
    conexao = iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'DELETE FROM servico WHERE id = %s'
            cursor.execute(comando, (id_servico,))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de exclusão: {e}")
        finally:
            cursor.close()
            conexao.close()