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


def criar_agendamento(idMedico, idServico, data, horaInicio, ):  # Adiciona cpf_paciente como parâmetro
    conexao = BD.iniciarConexao()
    
    if conexao is None:
        print("Erro ao conectar ao banco de dados.")
        return False

    try:
        cursor = conexao.cursor()

        # Verificando se os dados obrigatórios estão presentes
        if not idMedico or not idServico or not data or not horaInicio:
            print("Erro: Dados incompletos fornecidos.")
            return False

        comando_agendamento = '''
            INSERT INTO agendamentos (id_medico, id_servico, data, hora_inicio, )  # Adiciona a coluna id_cpf_paciente
            VALUES (%s, %s, %s, %s) 
        '''
        parametros = (idMedico, idServico, data, horaInicio, )  # Inclui o CPF nos parâmetros
        
        cursor.execute(comando_agendamento, parametros)
        conexao.commit()  # Add this line to commit the changes

        # Verificando se a inserção foi realizada
        if cursor.lastrowid:  # ID da última linha inserida
            print(f"Agendamento criado com sucesso, ID: {cursor.lastrowid}")
            return True
        else:
            print("Falha ao criar o agendamento. Nenhuma linha inserida.")
            return False

    except Error as e:
        print(f"Erro ao inserir agendamento: {e}")
        return False
    
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
            
def listar_agendamentos():
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'SELECT * FROM agendamentos'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print("Agendamentos:")
            for agendamento in resultado:
                print(agendamento)
            return resultado
        except Error as e:
            print(f"Erro ao executar o comando de seleção: {e}")
            return []
        finally:
            cursor.close()
            conexao.close()

