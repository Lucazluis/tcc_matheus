import model.BD as BD
from mysql.connector import Error

def criar_especialidade(descricao):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_servico = 'INSERT INTO especialidade (descricao) VALUES (%s)'
            cursor.execute(comando_servico, [descricao])
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()

def listar_especialidade():
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'SELECT * FROM especialidade'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            return resultado
        except Error as e:
            print(f"Erro ao executar o comando de seleção: {e}")
            return []
        finally:
            cursor.close()
            conexao.close()

def atualizar_especialidade(id_especialidade, descricao_nova):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'UPDATE especialidade SET descricao = %s WHERE id = %s'
            cursor.execute(comando, [descricao_nova, id_especialidade])
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de atualização: {e}")
        finally:
            cursor.close()
            conexao.close()

def deletar_especialidade(id):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_deletar_especialidade = "DELETE FROM especialidade WHERE id = %s"
            cursor.execute(comando_deletar_especialidade, [id])
            conexao.commit()
            return True
        except Exception as e:
            print(f"Ocorreu um problema ao excluir a especialidade: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()
