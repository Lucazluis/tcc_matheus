from flask import Flask, render_template, redirect, request, session, url_for

import model.gestaoBD as gestaoBD
import model.servicoBD as servicoBD
import model.usuarioBD as usuarioBD
import model.especialidadeBD as especialidadeBD
import model.medicoBD as medicoBD

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
    return render_template("servicos.html", listaServicos=servicos)


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
        descricao = request.form["Descricao"]
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
    especialidades = especialidadeBD.listar_especialidade()
    servicos = servicoBD.listar_servicos()
    return render_template("medicos.html", listaMedicos=medicos, listaEspecialidades=especialidades, listaServico=servicos)


@app.post("/medico/cadastrar")
def cadastrarMedico():
    nome = request.form["nome"]
    crm = request.form["crm"]
    especialidades = request.form.getlist("especialidades")
    servicos = request.form.getlist("servicos")

    idMedicoCadastrado = medicoBD.criar_medico(nome, crm)
    medicoBD.addEspecialidadesDoMedico(idMedicoCadastrado, especialidades)
    medicoBD.addServicosDoMedico(idMedicoCadastrado, servicos)
    return redirect(url_for('medicosGet'))

@app.post("/medico/atualizar")
def atualizarMedico():
    id = request.form["id"]
    nome = request.form["nome"]
    crm = request.form["crm"]
    especialidades = request.form.getlist("especialidades")
    servicos = request.form.getlist("servicos")
    
    medicoBD.atualizar_medico(id,nome,crm)
    medicoBD.atualizarEspecialidadesMedico(id,especialidades)
    medicoBD.atualizarListaServicosMedico(id,servicos)
    return redirect(url_for('medicosGet'))

@app.post("/medico/deletar")
def deletarMedico():
    id = request.form["id"]
    medicoBD.deletar_medico(id)
    medicoBD.removerTodasEspecialidadesDoMedico(id)
    medicoBD.removerTodosOsServicosDoMedico(id)
    
    return redirect(url_for('medicosGet'))
############# Rotas de Gestão ##################


@app.get("/gestao")
def gestaoGet():
    servicos = gestaoBD.listar_servicos()
    return render_template("gestao_servico.html", listaServicos=servicos)

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
