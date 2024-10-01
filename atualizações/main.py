from flask import Flask, render_template, redirect, request, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy


import model.gestaoBD as gestaoBD
import model.servicoBD as servicoBD
import model.usuarioBD as usuarioBD
import model.especialidadeBD as especialidadeBD
import model.medicoBD as medicoBD
import model.disponibilidade as disponibilidadeBD
import model.agendarConsultaBD as agendarConsultaBD

app = Flask(__name__)
app.secret_key = "WagnerELucas"

# Inicio


@app.route("/")
def index():
    return render_template("index.html")

############# Rotas de serviço ##################
@app.route("/servico")
def servicosGet():
    servicos = servicoBD.listar_servicos()
    return render_template("gestao_servico.html", listaServicos=servicos)

@app.route("/servico/cadastrar", methods=["POST"])
def servicoCadastrar():
    if "email" in session and session.get("nivel") == "secretaria":
        servico = request.form["Servico"]
        descricao = request.form["Descrição"]
        try:
            servicoBD.criar_servico(descricao, servico)
            flash("Serviço criado com sucesso!", "success")  # Mensagem flash
            return redirect("/gestao")
        except Exception as e:
            flash(f"Ocorreu um erro ao criar o serviço: {e}", "error")
            return redirect("/gestao") 
    else:
        flash("Você precisa estar logado como secretaria para realizar esta ação.", "error")
        return redirect("/login")

@app.route("/servico/atualizar", methods=["POST"])
def servicoAtualizar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]
        servico = request.form["Servico"]
        descricao = request.form["Descrição"]
        try:
            servicoBD.atualizar_servico(int(id), descricao, servico)
            flash("Serviço atualizado com sucesso!", "success")
            return redirect("/gestao")
        except Exception as e:
            flash(f"Ocorreu um erro ao atualizar o serviço: {e}", "error")
            return redirect("/gestao") 
    else:
        flash("Você precisa estar logado como secretaria para realizar esta ação.", "error")
        return redirect("/login")


@app.route("/servico/deletar", methods=["POST"])
def servicoDeletar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]

        try:
            servicoBD.deletar_servico(int(id))
            flash("Serviço deletado com sucesso!", "success") 
            return redirect("/gestao")
        except Exception as e:
            flash(f"Ocorreu um erro ao deletar o serviço: {e}", "error") 
            return redirect("/gestao")
    else:
        flash("Você precisa estar logado como secretaria para realizar esta ação.", "error") 
        return redirect("/login") 

############# Rotas de Especialidades ##################

@app.get("/especialidades")
def especialidadeGet():
    especialidades = especialidadeBD.listar_especialidade()
    return render_template("especialidades.html", listaEspecialidades=especialidades)


@app.post("/especialidade/cadastrar")
def especialidadeCadastrar():
    if "email" in session and session.get("nivel") == "secretaria":
        descricao = request.form["Descrição"]
        try:
            especialidadeBD.criar_especialidade(descricao)
            flash("Especialidade criada com sucesso!", "success")
        except Exception as e:
            flash(f"Ocorreu um erro ao criar a especialidade: {e}", "error")

        return redirect(url_for('especialidadeGet'))
    else:
        flash("Você precisa estar logado como secretaria para realizar esta ação.", "error")
        return redirect("/login")


@app.post("/especialidade/atualizar")
def especialidadeAtualizar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]
        descricao = request.form["Descricao"]
        try:
            especialidadeBD.atualizar_especialidade(int(id), descricao)
            flash("Especialidade atualizada com sucesso!", "success")
            return redirect(url_for('especialidadeGet'))
        except Exception as e:
            flash(f"Ocorreu um erro ao atualizar a especialidade: {e}", "error")
            return redirect("/login")


@app.post("/especialidade/deletar")
def especialidadeDeletar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]

        try:
            especialidadeBD.deletar_especialidade(int(id))
            flash("Especialidade deletada com sucesso!", "success")
        except Exception as e:
            flash(f"Ocorreu um erro ao deletar a especialidade: {e}", "error")

        return redirect(url_for('especialidadeGet'))
    else:
        flash("Você precisa estar logado como secretaria para realizar esta ação.", "error")
        return redirect("/login")

############# Rotas de Medico ##################

@app.get("/medicos")
def medicosGet():
    medicos = medicoBD.listar_medico()
    especialidades = especialidadeBD.listar_especialidade()
    servicos = servicoBD.listar_servicos()
    return render_template("gestao_medico.html", listaMedicos=medicos, listaEspecialidades=especialidades, listaServico=servicos)

@app.post("/medico/cadastrar")
def medicoCadrastar():
    nome = request.form["NOME"]
    crm = request.form["CRM"]
    especialidades = request.form.getlist("especialidades")
    servicos = request.form.getlist("servicos")

    try:
        idMedicoCadastrado = medicoBD.criar_medico(nome, crm)
        medicoBD.addEspecialidadesDoMedico(idMedicoCadastrado, especialidades)
        medicoBD.addServicosDoMedico(idMedicoCadastrado, servicos)
        flash("Médico cadastrado com sucesso!", "success")
    except Exception as e:
        flash(f"Ocorreu um erro ao cadastrar o médico: {e}", "error")

    return redirect(url_for('medicosGet'))

@app.post("/medico/atualizar")
def medicoAtualizar():
    id = request.form["IDMEDICO"]
    nome = request.form["NOME"]
    crm = request.form["CRM"]
    novaEspecialidade = request.form["especialidades"]
    especialidade = request.form.getlist("especialidades")
    servicos = request.form.getlist("servicos")
    
    try:
        medicoBD.atualizar_medico(id,nome,crm,novaEspecialidade)
        medicoBD.atualizarEspecialidadesMedico(id,especialidade)
        medicoBD.atualizarListaServicosMedico(id,servicos)
        flash("Médico atualizado com sucesso!", "success")
    except Exception as e:
        flash(f"Ocorreu um erro ao atualizar o médico: {e}", "error")

    return redirect(url_for('medicosGet'))

@app.post("/medico/deletar")
def medicoDelatar():
    id = request.form["IDMEDICO"]
    
    try:
        medicoBD.deletar_medico(id)
        medicoBD.removerTodasEspecialidadesDoMedico(id)
        medicoBD.removerTodosOsServicosDoMedico(id)
        flash("Médico deletado com sucesso!", "success")
    except Exception as e:
        flash(f"Ocorreu um erro ao deletar o médico: {e}", "error")

    return redirect(url_for('medicosGet'))

############# Rotas de Dispoonibilidade ##################

@app.get("/disponibilidade")
def disponibilidadeGet():
    disponibilidade = disponibilidadeBD.listar_disponibilidade()
    return render_template("disponibilidade.html", listarDisponibilidade=disponibilidade)


@app.post("/disponibilidade/cadastrar")
def disponibilidadeCadastrar():
    if "email" in session and session.get("nivel") == "secretaria":
        FK_medico = request.form["idMedico"]
        horario_inicio = request.form["horaInicio"]
        horario_fim = request.form["horaFim"]
        tempo_consulta_min = request.form["tempo"]
        DiaAtendimento = request.form["dia"]
        dataDisponivel = request.form["data"]
        
        try:
            disponibilidadeBD.criar_disponibilidade( int(FK_medico), horario_inicio,horario_fim,tempo_consulta_min,DiaAtendimento,dataDisponivel)
            flash("Disponibilidade criada com sucesso!", "success")
        except Exception as e:
            flash(f"Ocorreu um erro ao criar a disponibilidade: {e}", "error")

        return redirect(url_for('disponibilidadeGet'))
    else:
        flash("Você precisa estar logado como secretaria para realizar esta ação.", "error")
        return redirect("/login")


@app.post("/disponibilidade/atualizar")
def disponibilidadeAtualizar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]
        FK_medico = request.form["idMedico"]
        horario_inicio = request.form["horaInicio"]
        horario_fim = request.form["horaFim"]
        tempo_consulta_min = request.form["tempo"]
        DiaAtendimento = request.form["dia"]
        dataDisponivel = request.form["data"]

        try:
            disponibilidadeBD.atualizar_disponibilidade(int(id), int(FK_medico),horario_inicio,horario_fim,int(tempo_consulta_min),DiaAtendimento,dataDisponivel)
            flash("Disponibilidade atualizada com sucesso!", "success")
            return redirect(url_for('disponibilidadeGet'))
        except Exception as e:
            flash(f"Ocorreu um erro ao atualizar a disponibilidade: {e}", "error")
            return redirect("/login")


@app.post("/disponibilidade/deletar")
def disponibilidadeDeletar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]

        try:
            disponibilidadeBD.deletar_disponibilidade(int(id))
            flash("Disponibilidade deletada com sucesso!", "success")
        except Exception as e:
            flash(f"Ocorreu um erro ao deletar a disponibilidade: {e}", "error")

        return redirect(url_for('disponibilidadeGet'))
    else:
        flash("Você precisa estar logado como secretaria para realizar esta ação.", "error")
        return redirect("/login")
############# Rotas de Agendamento ##################

@app.get("/agendamento")
def agendamentoGet():
    idServico = request.args.get("servicos")
    servicos = agendarConsultaBD.listar_servicos()
    listaMedicosHorarios = []
    
    if(idServico):
        listaMedicosHorarios = medicoBD.getListaMedicoByServicos(idServico)
    return render_template("agendamento.html", listaServico = servicos, listaMedicosHorarios = listaMedicosHorarios)




# tem que complementar




############# Rotas de Gestão ##################

@app.get("/gestao")
def gestaoGet():
    servicos = gestaoBD.listar_servicos()
    return render_template("gestao_servico.html", listaServicos=servicos)

############# Rotas de controle de acesso ##################
    
@app.route("/consultasAgendadas")
def consultasAgendadas():
        return render_template("consultas_agendadas.html")

@app.route("/sobre")
def sobre():
        return render_template("sobre.html")

@app.route("/contato")
def contato():
        return render_template("contato.html")

@app.route("/usuario")
def usuario():
        return render_template("usuario1.0.html")

############# Rotas de Cadastro ##################

@app.get("/cadastro")

def cadastroGet():
    return render_template("tela_cadastro.html")


@app.post("/cadastro")
def contaCadastrar():
    if 1==1:
        email = request.form["email"]
        senha = request.form["senha"]
        FK_Paciente = request.form["cpf"]
        cpf = request.form["cpf"]
        nome = request.form["nome"]
        data_nascimento = request.form["dataNascimento"]
        e_mail = request.form["email"]
        telefone1 = request.form["telefone1"]
        telefone2 = request.form["telefone2"]
        cep = request.form["cep"]
        estado = request.form["estado"]
        cidade = request.form["cidade"]
        bairro = request.form["bairro"]
        rua = request.form["rua"]
        numero_casa = request.form["numero"]
        complemento = request.form["complemento"]
        pais = request.form["pais"]
        referencia = request.form["referencia"]
        cpf_paciente = request.form["cpf"]
        try:
            usuarioBD.criar_paciente(cpf, nome, data_nascimento, e_mail, telefone1, telefone2)
            usuarioBD.criar_usuario(email, senha, FK_Paciente)
            usuarioBD.criar_endereco(rua,bairro,cidade,estado,pais,cep,numero_casa,complemento, referencia,cpf_paciente)
            flash("Cadastro realizado com sucesso!", "success")
        except Exception as e:
            flash(f"Ocorreu um erro ao realizar o cadastro: {e}", "error")
        print("deu certo")

        return redirect(url_for('loginGet'))

    else:
        flash("Você precisa estar logado como secretaria para realizar esta ação.", "error")
        print("deu erro")
        return redirect("/erro")
    
    
@app.post("/cadastro/atualizar")
def contaAtualizar():
    if "email" in session and session.get("nivel") == "secretaria":
        email = request.form["email"]
        senha = request.form["senha"]
        FK_Paciente = request.form["cpf"]
        cpf = request.form["cpf"]
        nome = request.form["nome"]
        data_nascimento = request.form["dataNascimento"]
        e_mail = request.form["email"]
        telefone1 = request.form["telefone1"]
        telefone2 = request.form["telefone2"]
        cep = request.form["cep"]
        estado = request.form["estado"]
        cidade = request.form["cidade"]
        bairro = request.form["bairro"]
        rua = request.form["rua"]
        numero_casa = request.form["numero"]
        complemento = request.form["complemento"]
        pais = request.form["pais"]
        referencia = request.form["referencia"]
        cpf_paciente = request.form["cpf"]
        try:
            disponibilidadeBD.atualizar_usuario(email, senha, FK_Paciente)
            disponibilidadeBD.atualizar_paciente(cpf, nome, data_nascimento, e_mail, telefone1, telefone2)
            disponibilidadeBD.atualizar_endereco(rua,bairro,cidade,estado,pais,cep,numero_casa,complemento, referencia,cpf_paciente)
            flash("Cadastro atualizado com sucesso!", "success")
            return render_template("index.html")
        except Exception as e:
            flash(f"Ocorreu um erro ao atualizar o cadastro: {e}", "error")
            return redirect("/login")
    
############# Rotas de controle de acesso ##################
# @app.get("/login")
# def loginGet():
#     return render_template("tela_login.html")


# @app.post("/login")
# def loginPost():
#     email = request.form["email"]
#     senha = request.form["senha"]
#     usuario = usuarioBD.pegarUsuario(email)
#     if (email == usuario[1] and senha == usuario[2]):
#         session["nivel"] = usuario[3]
#         session["email"] = usuario[1]
#         return redirect("/")
#     else:
#         return redirect("/login")


# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/")


@app.get("/login")
def loginGet():
    return render_template("tela_login.html")


@app.post("/login")
def loginPost():
    email = request.form["email"]
    senha = request.form["senha"]
    usuario = usuarioBD.pegarUsuario(email)
    if (email == usuario[1] and senha == usuario[2]):
        session["nivel"] = usuario[3]
        session["email"] = usuario[1]
        flash("Login realizado com sucesso!", "success")
        return redirect("/")
    else:
        flash("E-mail ou senha incorretos.", "error")
        return redirect("/login")


@app.route("/logout")
def logout():
    session.clear()
    flash("Você foi deslogado com sucesso!", "success")
    return redirect("/")

app.run(debug=True)




