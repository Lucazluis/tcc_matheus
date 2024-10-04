import model.BD as BD
from mysql.connector import Error 

def get_consultas_agendadas():
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'SELECT * FROM agendamentos WHERE status_servico = "Marcada"'
            cursor.execute(comando)
            resultados = cursor.fetchall()
            consultas = []
            for resultado in resultados:
                consulta = {
                    'id': resultado[0],
                    'paciente': resultado[1],
                    'servico': resultado[2],
                    'hora': resultado[3],
                    'profissional': resultado[4]
                }
                consultas.append(consulta)
            return consultas
        except Error as e:
            print(f"Erro ao executar o comando de consulta: {e}")
        finally:
            cursor.close()
            conexao.close()
