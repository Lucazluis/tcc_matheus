import model.BD 
from mysql.connector import Error

def pegarUsuario(email):
    conexao  = model.BD.iniciarConexao()
    cursor = conexao.cursor()
    query = "SELECT * FROM usuario WHERE email = %s"
    parametros = [email]

    cursor.execute(query, parametros)
    resultados = cursor.fetchone()

    return resultados


def criarUsuario(email,senha,FK_Paciente):
    conexao = model.BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_usuario = "INSERT INTO Usuario (email,senha,tipo,FK_Paciente ) values(%s,%s,'paciente',%s)"
            cursor.execute(comando_usuario, [email,senha,FK_Paciente])
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()
