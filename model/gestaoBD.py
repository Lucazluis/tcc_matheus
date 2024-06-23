import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="WAGUINHO451",
    database="Agenda"
)
    
# Get a cursor object to execute queries
cursor = conexao.cursor()


# CRUD for 'servico' table
def criar_servico():
    descricao = input("Digite a descrição do serviço: ")
    nomeServico = input("Digite o nome do serviço: ")

    comando_servico = f'INSERT INTO servico (descricao, nomeServico) VALUES("{descricao}", "{nomeServico}")'
    cursor.execute(comando_servico)
    conexao.commit()

    cursor.execute("SELECT LAST_INSERT_ID()")
    servico_id = cursor.fetchone()[0]
    print(f"Serviço '{nomeServico}' criado com sucesso! ID: {servico_id}")

def listar_servicos():
    comando = 'SELECT * FROM servico;'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print("Serviços cadastrados:")
    for servico in resultado:
        print(f"- ID: {servico[0]} | Descrição: {servico[1]} | Nome: {servico[2]}")

def atualizar_servico():
    id_servico = int(input("Digite o ID do serviço a ser atualizado: "))
    descricao_nova = input("Digite a nova descrição do serviço: ")
    nomeServico_novo = input("Digite o novo nome do serviço (opcional, se vazio mantém o atual): ")

    if nomeServico_novo == "":
        comando = f'UPDATE servico SET descricao = "{descricao_nova}" WHERE id = {id_servico}'
    else:
        comando = f'UPDATE servico SET descricao = "{descricao_nova}", nomeServico = "{nomeServico_novo}" WHERE id = {id_servico}'

    cursor.execute(comando)
    conexao.commit()
    print("Serviço atualizado com sucesso!")

def deletar_servico():
    id_servico = int(input("Digite o ID do serviço a ser deletado: "))
    comando = f'DELETE FROM servico WHERE id = {id_servico}'
    cursor.execute(comando)
    conexao.commit()
    print("Serviço deletado com sucesso!")

# CRUD for 'medico' table
def criar_medico():
    nome = input("Digite o nome do médico: ")
    crm = input("Digite o CRM do médico: ")

    comando_medico = f'INSERT INTO medico (nome, crm) VALUES("{nome}", "{crm}")'
    cursor.execute(comando_medico)
    conexao.commit()

    cursor.execute("SELECT LAST_INSERT_ID()")
    medico_id = cursor.fetchone()[0]
    print(f"Médico '{nome}' criado com sucesso! ID: {medico_id}")

def listar_medicos():
    comando = 'SELECT * FROM medico;'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print("Médicos cadastrados:")
    for medico in resultado:
        print(f"- ID: {medico[0]} | Nome: {medico[1]} | CRM: {medico[2]}")

def atualizar_medico():
    id_medico = int(input("Digite o ID do médico a ser atualizado: "))
    nome_novo = input("Digite o novo nome do médico (opcional, se vazio mantém o atual): ")
    crm_novo = input("Digite o novo CRM do médico (opcional, se vazio mantém o atual): ")

    if nome_novo == "":
        comando = f'UPDATE medico SET crm = "{crm_novo}" WHERE id = {id_medico}'
    elif crm_novo == "":
        comando = f'UPDATE medico SET nome = "{nome_novo}" WHERE id = {id_medico}'
    else:
        comando = f'UPDATE medico SET nome = "{nome_novo}", crm = "{crm_novo}" WHERE id = {id_medico}'

    cursor.execute(comando)
    conexao.commit()
    print("Médico atualizado com sucesso!")

def deletar_medico():
    id_medico = int(input("Digite o ID do médico a ser deletado: "))
    comando = f'DELETE FROM medico WHERE id = {id_medico}'
    cursor.execute(comando)
    conexao.commit()
    print("Médico deletado com sucesso!")

# CRUD for 'horarios' table
def criar_horario():
    id_medico = int(input("Digite o ID do médico: "))
    id_servico = int(input("Digite o ID do serviço: "))
    hora = input("Digite a data e hora (no formato AAAA-MM-DD HH:MM:SS): ")

    comando_horario = f'INSERT INTO horarios (id_medico, id_servico, hora ) VALUES({id_medico}, {id_servico}, "{hora}")'
    cursor.execute(comando_horario)
    conexao.commit()
    print("Horário criado com sucesso!")

def listar_horarios():
    comando = 'SELECT horarios.id, medico.nome, servico.nomeServico, horarios.hora  FROM horarios INNER JOIN medico ON horarios.id_medico = medico.id INNER JOIN servico ON horarios.id_servico = servico.id;'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print("Horários cadastrados:")
    for horario in resultado:
        print(f"- ID: {horario[0]} | Médico: {horario[1]} | Serviço: {horario[2]} | Hora: {horario[3]} | ")

def atualizar_horario():
    id_horario = int(input("Digite o ID do horário a ser atualizado: "))
    id_medico_novo = int(input("Digite o novo ID do médico (opcional, se vazio mantém o atual): "))
    id_servico_novo = int(input("Digite o novo ID do serviço (opcional, se vazio mantém o atual): "))
    hora_nova = input("Digite a nova data e hora (no formato AAAA-MM-DD HH:MM:SS): ")

    comando = f'UPDATE horarios SET hora = "{hora_nova}"'

    if id_medico_novo:
        comando += f', id_medico = {id_medico_novo}'
    if id_servico_novo:
        comando += f', id_servico = {id_servico_novo}'
    
    comando += f' WHERE id = {id_horario}'

    cursor.execute(comando)
    conexao.commit()
    print("Horário atualizado com sucesso!")

def deletar_horario():
    id_horario = int(input("Digite o ID do horário a ser deletado: "))
    comando = f'DELETE FROM horarios WHERE id = {id_horario}'
    cursor.execute(comando)
    conexao.commit()
    print("Horário deletado com sucesso!")

# Main program loop
def main():
    while True:
        print("\nSistema de Gestão")
        print("1. Gerenciar serviços")
        print("2. Gerenciar médicos")
        print("3. Gerenciar horários")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("\nGerenciamento de Serviços")
            print("1. Criar serviço")
            print("2. Listar serviços")
            print("3. Atualizar serviço")
            print("4. Deletar serviço")
            opcao_servico = int(input("Escolha uma opção: "))
            if opcao_servico == 1:
                criar_servico()
            elif opcao_servico == 2:
                listar_servicos()
            elif opcao_servico == 3:
                atualizar_servico()
            elif opcao_servico == 4:
                deletar_servico()
        elif opcao == 2:
            print("\nGerenciamento de Médicos")
            print("1. Criar médico")
            print("2. Listar médicos")
            print("3. Atualizar médico")
            print("4. Deletar médico")
            opcao_medico = int(input("Escolha uma opção: "))
            if opcao_medico == 1:
                criar_medico()
            elif opcao_medico == 2:
                listar_medicos()
            elif opcao_medico == 3:
                atualizar_medico()
            elif opcao_medico == 4:
                deletar_medico()
        elif opcao == 3:
            print("\nGerenciamento de Horários")
            print("1. Criar horário")
            print("2. Listar horários")
            print("3. Atualizar horário")
            print("4. Deletar horário")
            opcao_horario = int(input("Escolha uma opção: "))
            if opcao_horario == 1:
                criar_horario()
            elif opcao_horario == 2:
                listar_horarios()
            elif opcao_horario == 3:
                atualizar_horario()
            elif opcao_horario == 4:
                deletar_horario()
        elif opcao == 0:
            print("Saindo do sistema....")
            break

# Run the main loop
main()

# Close the database connection
cursor.close()
conexao.close()