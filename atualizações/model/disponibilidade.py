import model.BD as BD
from mysql.connector import Error

def criar_disponibilidade(idMedico, horaInicio, horaFim, tempConsulta, diaSemana):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_disponibilidade = 'INSERT INTO disponibilidade (FK_medico, horario_inicio, horario_fim, tempo_consulta_min, DiaAtendimento) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(comando_disponibilidade, [idMedico, horaInicio, horaFim, tempConsulta, diaSemana])
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()
            
def listar_disponibilidade():
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'SELECT * FROM disponibilidade'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            return resultado
        except Error as e:
            print(f"Erro ao executar o comando de seleção: {e}")
            return []
        finally:
            cursor.close()
            conexao.close()

def atualizar_disponibilidade(id_disponibilidade, id_medico, hora_inicio, hora_fim, tempo_consulta, dia_semana):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_atualiza_disponibilidade = """
                UPDATE disponibilidade
                SET FK_medico = %s, horario_inicio = %s, horario_fim = %s, tempo_consulta_min = %s, DiaAtendimento = %s
                WHERE id = %s
            """
            cursor.execute(comando_atualiza_disponibilidade, [id_medico, hora_inicio, hora_fim, tempo_consulta, dia_semana, id_disponibilidade])
            conexao.commit()
            return True
        except Exception as e:
            print(f"Ocorreu um problema ao atualizar a disponibilidade: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()

def deletar_disponibilidade(id_disponibilidade):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_deletar_disponibilidade = "DELETE FROM disponibilidade WHERE id = %s"
            cursor.execute(comando_deletar_disponibilidade, [id_disponibilidade])
            conexao.commit()
            return True
        except Exception as e:
            print(f"Ocorreu um problema ao excluir a disponibilidade: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()





