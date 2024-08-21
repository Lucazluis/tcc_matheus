from flask import Flask, render_template, redirect, request, session
import model.servicoBD as user
import model.usuarioBD
import model.medicoBD as medicoBD
import model.gestaoBD
import model.horarioBD as horarioBD 
import model.especialidadeBD as especialidadeBD

app = Flask(__name__)
app.secret_key = "WagnerELucas"

    # Inicio #
@app.route("/")
def hello_world():
        return render_template("index.html")

    #   rotas     #
@app.route("/servico/gestao/consultasAgendadas")
def consultasAgendadas():
        return render_template("consultas_agendadas.html")

@app.route("/servico/gestao/consultasAgendadas/sobre")
def sobre():
        return render_template("sobre.html")

@app.route("/servico/gestao/consultasAgendadas/sobre/contato")
def contato():
        return render_template("contato.html")

@app.route("/servico/gestao/consultasAgendadas/sobre/contato/usuario")
def usuario():
        return render_template("usuario1.0.html")
    
    
    #   login e logout  #
@app.get("/login")
def loginGet():
        return render_template("tela_login.html")

@app.post("/login")
def loginPost():
        email = request.form["email"]
        senha = request.form["senha"]
        usuario = model.usuarioBD.pegarUsuario(email)
        if(email == usuario[1] and senha == usuario[2]):
            session["nivel"] = usuario[3]
            session["email"] = usuario[1]
            return redirect("/")
        else:
            return redirect("/login")
        
@app.route("/logout")
def logout():
        session.clear()
        return redirect("/")  
      
    
    #   para servicos   #
@app.get("/servico")
def servicosGet():
        servicos = user.servicosAgendamento()
        return render_template("servicos.html", listaServico = servicos)

@app.post("/servico")
def servicoPost():
        return render_template("servicos.html")

@app.get("/gestao/servico")
def gestaoServicoGet():
        servicos = model.gestaoBD.listar_servicos()
        return render_template("gestao_servico.html", listaServicos = servicos)

@app.get("/gestao/medico")
def gestaoMedicoGet():
        medicos = medicoBD.listar_medicos()
        return render_template("gestao_medico.html", listaMedico = medicos)
    
@app.get("/gestao/horario")
def gestaoHorarioGet():
        horario = horarioBD.listar_horario()
        return render_template("gestao_horario.html", listaHorario = horario)

@app.post("/gestao")
def gestaoPost():
    if "email" in session and session.get("nivel") == "secretaria":
        servico = request.form["Servico"]
        descricao = request.form["Descrição"]
        try:
            model.gestaoBD.criar_servico(descricao,servico)
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


@app.post("/gestao/atualizar")
def gestaoatualizarPost():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]
        servico = request.form["Servico"]                                                                                                                                                       
        descricao = request.form["Descricao"]
        try:
            model.gestaoBD.atualizar_servico(int(id), descricao, servico)
            session["mensagem"] = "Serviço criado com sucesso!"
            session["tipo_mensagem"] = "success"
            return redirect("/gestao")
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao criar o serviço: {e}"
            session["tipo_mensagem"] = "error"
            return redirect("/login")
        
@app.post("/gestao/atualizar/deletar")
def gestaodeletarPost():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["id"]

        try:
            model.gestaoBD.deletar_servico(int(id))
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #   para medicos    #
@app.get("/")
def medicoGet():
        medicos = model.medicoBD.listar_medicos()
        return render_template("gestao_servico.html", listaMedicos = medicos)
    
@app.post("/medico/adicionar")
def medicoPost():
    if "email" in session and session.get("nivel") == "secretaria":
        try:
            nome = request.form["NOME"]
            crm = request.form["CRM"]
            especialidade = request.form["especialidade"]

            medicoBD.adiciona_medico(nome,crm)
            especialidadeBD
            return redirect("/gestao/medico")
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao adicionar o medico: {e}"
            session["tipo_mensagem"] = "error"
        
            return redirect("/erro")
    else:
        session["mensagem"] = "Você precisa estar logado como secretaria para realizar esta ação."
        session["tipo_mensagem"] = "error"
        return redirect("/login")

@app.post("/medico/atualiza")
def medicoAtualizarPost():
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["IDMEDICO"]
        nome = request.form["NOME"]                                                                                                                                                       
        crm = request.form["CRM"]
        try:
            medicoBD.atualizar_medico(int(id), nome, crm)
            return redirect("/gestao/medico")
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao atualizar medico: {e}"
            session["tipo_mensagem"] = "error"
            return redirect("/login")
        
@app.post("/medico/deleta")
def medicoDeletarPost():    
    if "email" in session and session.get("nivel") == "secretaria":
        id = request.form["IDMEDICO"]

        try:
            medicoBD.deletar_medico(int(id))
            return redirect("/gestao/medico")
        except Exception as e:
            session["mensagem"] = f"Ocorreu um erro ao deletar medico: {e}"
            session["tipo_mensagem"] = "error"

        return redirect("/gestao")
    else:
        session["mensagem"] = "Você precisa estar logado como secretaria para realizar esta ação."
        session["tipo_mensagem"] = "error"
        return redirect("/login")
    
app.run(debug=True)