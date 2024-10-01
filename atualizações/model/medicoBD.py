import model.BD as BD
from mysql.connector import Error
from datetime import *

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
    select
    m.id,
    m.nome,
    m.crm,

    
    (select GROUP_CONCAT(se.descricao)
		from medico_especialidade sme
	 left join especialidade se
	 on se.id = sme.FK_especialidade

	 where sme.FK_medico = m.id) AS especialidade,
    d.DiaAtendimento,
    d.horario_inicio,
    d.horario_fim,
    d.tempo_consulta_min
    
  
    
     
	from medico_servico ms

	left join medico m
	on m.id = ms.FK_medico
 
    left join disponibilidade d
    on d.FK_medico = m.id

	where ms.FK_servico = %s and d.id is not null;
    """

    
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            cursor.execute(query, [idServico])
            resultado = cursor.fetchall()
            return ajusteDadosDisponibilidade(resultado)
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()
            
def ajusteDadosDisponibilidade(lista):
    novaLista = []
    for row in lista:
        resultado = getIndexMedicoJaExistente(row[0], novaLista)
        if(getIndexMedicoJaExistente(row[0], novaLista) is not False):
            novaLista[resultado][4] = novaLista[resultado][4] + getHorarios(row[5],row[6],row[7], row[4])
        else:
            temp = []
            horarios = getHorarios(row[5],row[6],row[7], row[4])
            for n in range(4):
                temp.append(row[n])
            temp.append(horarios)
            novaLista.append(temp)
    return novaLista

def getIndexMedicoJaExistente(id, novaLista):
    for i in range(len(novaLista)):
        if(id in novaLista[i]):
            return i
    return False

def getHorarios(inicio, fim, intervalo, dia):
    delta = timedelta(minutes=intervalo)
    listaHorario = []
    while(inicio <= fim):
        listaHorario.append([dia, format_timedelta_to_HHMMSS(inicio)])
        inicio = inicio + delta
    return listaHorario
    
def format_timedelta_to_HHMMSS(td):
    td_in_seconds = td.total_seconds()
    hours, remainder = divmod(td_in_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    if minutes < 10:
        minutes = "0{}".format(minutes)
    if seconds < 10:
        seconds = "0{}".format(seconds)
    return "{}:{}".format(hours, minutes)