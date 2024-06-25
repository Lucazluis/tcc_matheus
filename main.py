from flask import Flask, render_template, redirect, request, session
import model.gestaoBD
import model.servicoBD as user
import model.usuarioBD

app = Flask(__name__)
app.secret_key = "WagnerELucas"

    #Inicio
@app.route("/")
def hello_world():
        return render_template("index.html")


    #Pagina servicos --- Get
@app.get("/servico")
def servicosGet():
        servicos = user.servicosAgendamento()
        return render_template("servicos.html", listaServico = servicos)

@app.post("/servico")
def servicoPost():
        return render_template("servicos.html")

@app.get("/gestao")
def gestaoGet():
        servicos = model.gestaoBD.listar_servicos()
        return render_template("gestao_servico.html", listaServicos = servicos)

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

app.run(debug=True)