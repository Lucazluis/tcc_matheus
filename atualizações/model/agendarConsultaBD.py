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

def criar_agendamento(id_medico, id_servico, data, hora_inicio, hora_fim, status_servico, id_cpf_paciente):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_agendamento = 'INSERT INTO agendamentos (id_medico, id_servico, data, hora_inicio, hora_fim, status_servico, id_cpf_paciente) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(comando_agendamento, [id_medico, id_servico, data, hora_inicio, hora_fim, status_servico, id_cpf_paciente])
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()

# def listar_agendamentos():
#     conexao = BD.iniciarConexao()
#     if conexao is not None:
#         try:
#             cursor = conexao.cursor()
#             comando = 'SELECT * FROM agendamentos'
#             cursor.execute(comando)
#             resultado = cursor.fetchall()
#             return resultado
#         except Error as e:
#             print(f"Erro ao executar o comando de seleção: {e}")
#             return []
#         finally:
#             cursor.close()
#             conexao.close()

# def atualizar_agendamento(id_agendamento, id_medico_novo, id_servico_novo, data_novo, hora_inicio_novo, hora_fim_novo, status_servico_novo, id_cpf_paciente_novo):
#     conexao = BD.iniciarConexao()
#     if conexao is not None:
#         try:
#             cursor = conexao.cursor()
#             comando_atualiza_agendamento = 'UPDATE agendamentos SET id_medico = %s, id_servico = %s, data = %s, hora_inicio = %s, hora_fim = %s, status_servico = %s, id_cpf_paciente = %s WHERE id = %s'
#             cursor.execute(comando_atualiza_agendamento, [id_medico_novo, id_servico_novo, data_novo, hora_inicio_novo, hora_fim_novo, status_servico_novo, id_cpf_paciente_novo, id_agendamento])
#             conexao.commit()
#         except Error as e:
#             print(f"Erro ao executar o comando de atualização: {e}")
#         finally:
#             cursor.close()
#             conexao.close()

# def deletar_agendamento(id):
#     conexao = BD.iniciarConexao()
#     if conexao is not None:
#         try:
#             cursor = conexao.cursor()
#             comando = 'DELETE FROM agendamentos WHERE id = %s'
#             cursor.execute(comando, [id])
#             conexao.commit()
#         except Error as e:
#             print(f"Erro ao executar o comando de exclusão: {e}")
#         finally:
#             cursor.close()
#             conexao.close()