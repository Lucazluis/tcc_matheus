import model.BD


def pegarUsuario(email):
    conexao  = model.BD.iniciarConexao()
    cursor = conexao.cursor()
    query = "SELECT * FROM usuario WHERE email = %s"
    parametros = [email]

    cursor.execute(query, parametros)
    resultados = cursor.fetchone()

    return resultados
