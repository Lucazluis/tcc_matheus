from flask import Flask, send_from_directory, render_template, redirect, request, session, url_for


import model.gestaoBD as gestaoBD
import model.servicoBD as servicoBD
import model.usuarioBD as usuarioBD
import model.especialidadeBD as especialidadeBD
import model.medicoBD as medicoBD
import model.disponibilidade as disponibilidadeBD

app = Flask(__name__)
app.secret_key = "WagnerELucas"

# Inicio


@app.route("/")
def index():
    return render_template("index.html")

############# Rotas de serviço ##################


@app.get("/servico")
def servicosGet():
    servicos = servicoBD.listar_servicos()
    return render_template("gestao_servico.html", listaServicos=servicos)


@app.post("/servico/cadastrar")
def servicoCadastrar():
    if "email" in session and session.get("nivel") == "secretaria":
        servico = request.form["Servico"]
        descricao = request.form["Descrição"]
        try:
            servicoBD.criar_servico(descricao, servico)
            session["mensagem"] = "Serviço criado com sucesso!"
            session["tipo_mensagem"] = "success"
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao criar o serviço: {e}"
            session["tipo_mensagem"] = "error"

        return redirect("/gestao")
    else:
        session["mensagem"] = "Você precisa estar logado como secretaria para realizar esta ação."
        session["tipo_mensagem"] = "error"
        return redirect("/login")


@app.post("/servico/atualizar")
def servicoAtualizar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]
        servico = request.form["Servico"]
        descricao = request.form["Descrição"]
        try:
            servicoBD.atualizar_servico(int(id), descricao, servico)
            session["mensagem"] = "Serviço criado com sucesso!"
            session["tipo_mensagem"] = "success"
            return redirect("/gestao")
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao criar o serviço: {e}"
            session["tipo_mensagem"] = "error"
            return redirect("/login")


@app.post("/servico/deletar")
def servicoDeletar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]

        try:
            servicoBD.deletar_servico(int(id))
            session["mensagem"] = "Serviço criado com sucesso!"
            session["tipo_mensagem"] = "success"
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao criar o serviço: {e}"
            session["tipo_mensagem"] = "error"

        return redirect("/gestao")
    else:
        session["mensagem"] = "Você precisa estar logado como secretaria para realizar esta ação."
        session["tipo_mensagem"] = "error"
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
            session["mensagem"] = "Serviço criado com sucesso!"
            session["tipo_mensagem"] = "success"
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao criar o serviço: {e}"
            session["tipo_mensagem"] = "error"

        return redirect(url_for('especialidadeGet'))
    else:
        session["mensagem"] = "Você precisa estar logado como secretaria para realizar esta ação."
        session["tipo_mensagem"] = "error"
        return redirect("/login")


@app.post("/especialidade/atualizar")
def especialidadeAtualizar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]
        descricao = request.form["Descricao"]
        try:
            especialidadeBD.atualizar_especialidade(int(id), descricao)
            session["mensagem"] = "Serviço criado com sucesso!"
            session["tipo_mensagem"] = "success"
            return redirect(url_for('especialidadeGet'))
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao criar o serviço: {e}"
            session["tipo_mensagem"] = "error"
            return redirect("/login")


@app.post("/especialidade/deletar")
def especialidadeDeletar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]

        try:
            especialidadeBD.deletar_especialidade(int(id))
            session["mensagem"] = "Serviço criado com sucesso!"
            session["tipo_mensagem"] = "success"
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao criar o serviço: {e}"
            session["tipo_mensagem"] = "error"

        return redirect(url_for('especialidadeGet'))
    else:
        session["mensagem"] = "Você precisa estar logado como secretaria para realizar esta ação."
        session["tipo_mensagem"] = "error"
        return redirect("/login")

############# Rotas de Medico ##################
@app.get("/medicos")
def medicosGet():
    medicos = medicoBD.listar_medico()
    return render_template("gestao_medico.html", listaMedicos=medicos)


@app.post("/medico/cadastrar")
def medicoCadrastar():
    nome = request.form["NOME"]
    crm = request.form["CRM"]
    especialidades = request.form.getlist("especialidade")
    servicos = request.form.getlist("servicos")

    idMedicoCadastrado = medicoBD.criar_medico(nome, crm)
    medicoBD.addEspecialidadesDoMedico(idMedicoCadastrado, especialidades)
    medicoBD.addServicosDoMedico(idMedicoCadastrado, servicos)
    return redirect(url_for('medicosGet'))

@app.post("/medico/atualizar")
def medicoAtualizar():
    id = request.form["IDMEDICO"]
    nome = request.form["NOME"]
    crm = request.form["CRM"]
    novaEspecialidade = request.form["especialidade"]

    especialidade = request.form.getlist("especialidade")
    servicos = request.form.getlist("servicos")
    
    medicoBD.atualizar_medico(id,nome,crm,novaEspecialidade)
    medicoBD.atualizarEspecialidadesMedico(id,especialidade)
    medicoBD.atualizarListaServicosMedico(id,servicos)
    return redirect(url_for('medicosGet'))

@app.post("/medico/deletar")
def medicoDelatar():
    id = request.form["IDMEDICO"]
    medicoBD.deletar_medico(id)
    medicoBD.removerTodasEspecialidadesDoMedico(id)
    medicoBD.removerTodosOsServicosDoMedico(id)
    
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
        
        try:
            disponibilidadeBD.criar_disponibilidade( int(FK_medico), horario_inicio,horario_fim,tempo_consulta_min,DiaAtendimento)
            session["mensagem"] = "disponibilidade criado com sucesso!"
            session["tipo_mensagem"] = "success"
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao criar a disponibilidade: {e}"
            session["tipo_mensagem"] = "error"

        return redirect(url_for('disponibilidadeGet'))
    else:
        session["mensagem"] = "Você precisa estar logado como secretaria para realizar esta ação."
        session["tipo_mensagem"] = "error"
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
        try:
            disponibilidadeBD.atualizar_disponibilidade(int(id), int(FK_medico),horario_inicio,horario_fim,int(tempo_consulta_min),DiaAtendimento)
            session["mensagem"] = "disponibilidade criado com sucesso!"
            session["tipo_mensagem"] = "success"
            return redirect(url_for('disponibilidadeGet'))
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao criar a disponibilidade: {e}"
            session["tipo_mensagem"] = "error"
            return redirect("/login")


@app.post("/disponibilidade/deletar")
def disponibilidadeDeletar():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]

        try:
            disponibilidadeBD.deletar_disponibilidade(int(id))
            session["mensagem"] = "Serviço criado com sucesso!"
            session["tipo_mensagem"] = "success"
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao criar o serviço: {e}"
            session["tipo_mensagem"] = "error"

        return redirect(url_for('disponibilidadeGet'))
    else:
        session["mensagem"] = "Você precisa estar logado como secretaria para realizar esta ação."
        session["tipo_mensagem"] = "error"
        return redirect("/login")

############# Rotas de Gestão ##################

@app.get("/gestao")
def gestaoGet():
    servicos = gestaoBD.listar_servicos()
    return render_template("gestao_servico.html", listaServicos=servicos)


############# Rotas de controle de acesso ##################

@app.route("/agendarConsulta")
def agendarConsulta():
        return render_template("agendamento.html")
    
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
def cadastroPost():
        email = request.form["email"]
        senha = request.form["senha"]
        cpf = request.form["cpf"]
        
        try:
                usuarioBD.criar_usuario( email,senha,cpf)
                session["mensagem"] = "usuario criado com sucesso!"
                session["tipo_mensagem"] = "success"
        except Exception as e:
                session["mensagem"] = f"Ocorreu um erro ao criar o usuario: {e}"
                session["tipo_mensagem"] = "error"
                
        return redirect(url_for('disponibilidadeGet'))
############# Rotas de controle de acesso ##################
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
        return redirect("/")
    else:
        return redirect("/login")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


app.run(debug=True)





