import model.BD as BD
from mysql.connector import Error


def pegarUsuario(email):
    conexao  = BD.iniciarConexao()
    cursor = conexao.cursor()
    query = "SELECT * FROM usuario WHERE email = %s"
    parametros = [email]

    cursor.execute(query, parametros)
    resultados = cursor.fetchone()

    return resultados

################################ paciente ####################################


def criar_paciente( nome, data_nascimento, e_mail, telefone1, telefone2, cpf):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_paciente = 'INSERT INTO paciente (cpf, nome, data_nascimento, e_mail, telefone1, telefone2) VALUES (%s, %s, %s, %s, %s, %s)'
            cursor.execute(comando_paciente, ( nome, data_nascimento, e_mail, telefone1, telefone2, cpf))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()
            
def atualizar_paciente(cpf, nome_novo, data_nascimento_novo, e_mail_novo, telefone1_novo, telefone2_novo):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'UPDATE paciente SET nome = %s, data_nascimento = %s, e_mail = %s, telefone1 = %s, telefone2= %s WHERE id = %s' 
            cursor.execute(comando, (nome_novo, data_nascimento_novo, e_mail_novo, telefone1_novo, telefone2_novo, cpf))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de atualização: {e}")
        finally:
            cursor.close()
            conexao.close()
            
def deletar_paciente(id_paciente):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'DELETE FROM paciente WHERE id = %s'
            cursor.execute(comando, (id_paciente))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de exclusão: {e}")
        finally:
            cursor.close()
            conexao.close()
################################ usuario ####################################

def criar_usuario(email, senha, FK_Paciente):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_usuario = 'INSERT INTO usuario (email, senha, tipo, FK_Paciente) VALUES (%s, %s,"paciente",%s)'
            
            cursor.execute(comando_usuario, (email, senha, FK_Paciente))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()
            
def atualizar_usuario(id_usuario, email_novo, senha_nova, FK_Paciente_novo):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'UPDATE usuario SET email = %s, senha = %s, tipo = "paciente", FK_Paciente = %s WHERE id = %s' 
            cursor.execute(comando, (email_novo, senha_nova, FK_Paciente_novo, id_usuario))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de atualização: {e}")
        finally:
            cursor.close()
            conexao.close()
            
def deletar_usuario(id_usuario):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'DELETE FROM servico WHERE id = %s'
            cursor.execute(comando, (id_usuario,))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de exclusão: {e}")
        finally:
            cursor.close()
            conexao.close()


################################ endereço ####################################

def criar_endereco(rua,bairro,cidade,estado,pais,cep,numero_casa,complemento, referencia,cpf_paciente):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando_endereco = 'INSERT INTO endereco (rua,bairro,cidade,estado,pais,cep,numero_casa,complemento, referencia,cpf_paciente) VALUES (%s, %s,%s, %s, %s,%s, %s, %s,%s,%s)'
            
            cursor.execute(comando_endereco, (rua,bairro,cidade,estado,pais,cep,numero_casa,complemento, referencia,cpf_paciente))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de inserção: {e}")
        finally:
            cursor.close()
            conexao.close()
            
def atualizar_endereco(idEndereço,rua_nova,bairro_novo,cidade_nova,estado_novo,pais_novo,cep_novo,numero_casa_nova,complemento_novo, referencia_nova,cpf_paciente):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'UPDATE endereco SET rua = %s, bairro = %s, cidade = %s, estado = %s, pais= %s, cep= %s, numero_casa= %s, complemento= %s, referencia= %s WHERE id = %s' 
            cursor.execute(comando, (rua_nova,bairro_novo,cidade_nova,estado_novo,pais_novo,cep_novo,numero_casa_nova,complemento_novo, referencia_nova,cpf_paciente, idEndereço))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de atualização: {e}")
        finally:
            cursor.close()
            conexao.close()
            
def deletar_endereço(id_endereco):
    conexao = BD.iniciarConexao()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            comando = 'DELETE FROM endereco WHERE id = %s'
            cursor.execute(comando, (id_endereco))
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar o comando de exclusão: {e}")
        finally:
            cursor.close()
            conexao.close()