import BD


def servicosAgendamento():
    conexao  = BD.iniciaConexao()
    cursor = conexao.cursor()
    query = "SELECT * FROM servico"

    cursor.execute(query)
    resultados = cursor.fetchall()
    
    print(resultados)
    
def listar_servicos():
    conexao  = BD.iniciarConexao()
    cursor = conexao.cursor()
    query = "SELECT * FROM servico"

    cursor.execute(query)
    resultados = cursor.fetchall()
    
    print(resultados)
    
listar_servicos()