import model.BD as BD
from mysql.connector import Error

def criar_medico(nome, crm):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_servico = 'INSERT INTO medico (nome, crm) VALUES (%s, %s)'
            cursor.execute(comando_servico, [nome,crm])
            conexao.commit()
            id = cursor.lastrowid
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()
            return id

def listar_medico():
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = """
                        SELECT md.*,
                       (select GROUP_CONCAT(e.descricao) 
                       from especialidade e
                       left join medico_especialidade me
                       on me.FK_medico = md.id
                       and me.FK_especialidade = e.id
                       where me.id is not null) as especialidades
                       
                    FROM Agenda.medico md;
            """
            cursor.execute(comando)
            resultado = cursor.fetchall()
            return resultado
        except Error as e:
            print(f"Erro ao executar o comando de seleção: {e}")
            return []
        finally:
            cursor.close()
            conexao.close()

def atualizar_medico(idMedico, novoNome, novoCRM, novaEspecialidade):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_atualiza_medico = 'UPDATE medico SET nome = %s, crm = %s WHERE id = %s'
            cursor.execute(comando_atualiza_medico, [novoNome, novoCRM,idMedico])
            
            comando_atualiza_especialidade = 'UPDATE especialidade SET descricao = %s WHERE id = %s'
            cursor.execute(comando_atualiza_especialidade, [novaEspecialidade, idMedico])
            
            conexao.commit()
    
        except Error as e:
            print(f"Erro ao executar o comando de atualização: {e}")
        finally:
            cursor.close()
            conexao.close()

def deletar_medico(id):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'DELETE FROM medico WHERE id = %s'
            cursor.execute(comando, [id])
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de exclusão: {e}")
        finally:
            cursor.close()
            conexao.close()

#################### Especialidades Medico ##################
def addEspecialidadesDoMedico(idMedico,listaEspecialidades):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            for idEspecialidade in listaEspecialidades:
                comando_servico = 'INSERT INTO medico_especialidade (FK_medico, FK_especialidade) VALUES (%s, %s)'
                cursor.execute(comando_servico, [idMedico, idEspecialidade])
                conexao.commit()

        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()
            return id

def removerTodasEspecialidadesDoMedico(idMedico):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_servico = 'DELETE FROM medico_especialidade WHERE FK_medico= %s'
            cursor.execute(comando_servico, [idMedico])
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()

def atualizarEspecialidadesMedico(idMedico, listaEspecialidades):
    removerTodasEspecialidadesDoMedico(idMedico)
    addEspecialidadesDoMedico(idMedico,listaEspecialidades)


#################### Servicos Medico

def addServicosDoMedico(idMedico,listaServicos):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            for idServico in listaServicos:
                comando_servico = 'INSERT INTO medico_servico (FK_medico, FK_servico) VALUES (%s, %s)'
                cursor.execute(comando_servico, [idMedico, idServico])
                conexao.commit()

        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()
            return id

def removerTodosOsServicosDoMedico(IdMedico):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_servico = 'DELETE FROM medico_servico WHERE FK_medico= %s'
            cursor.execute(comando_servico, [IdMedico])
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()

def atualizarListaServicosMedico(idMedico,listaServicos):
    removerTodosOsServicosDoMedico(idMedico)
    addServicosDoMedico(idMedico, listaServicos)
    
def getListaMedicoByServicos(idServico):
    query = """

SELECT 
    m.nome,
    m.crm,
    e.descricao AS especialidade,
    d.horario_inicio,
    d.horario_fim,
    d.tempo_consulta_min,
    d.DiaAtendimento
FROM 
    medico_servico ms
INNER JOIN medico m ON m.id = ms.FK_medico
LEFT JOIN medico_especialidade me ON me.FK_medico = m.id
LEFT JOIN especialidade e ON e.id = me.FK_especialidade
LEFT JOIN disponibilidade d ON m.id = d.FK_medico
WHERE 
    ms.FK_servico = %s
    """

    
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            cursor.execute(query, [idServico])
            resultado = cursor.fetchall()
            return resultado
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()
            
def getHorariosByMedicos(idDisponibilidade):
    query = """
            select * from disponibilidade d
where d.FK_medico in (3, 14)
    """
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            cursor.execute(query, [idDisponibilidade])
            resultado = cursor.fetchall()
            return resultado
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()