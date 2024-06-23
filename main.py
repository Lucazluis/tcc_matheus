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

@app.get("/gestão")
def gestaoGet():
    servicos = user.servicosAgendamento()
    return render_template("gestao_servico.html")

@app.get("/gestão")
def gestaoPost():
    return render_template("gestao_servico.html")


@app.route("/servico/gestão/consultasAgendadas")
def consultasAgendadas():
    return render_template("consultas_agendadas.html")

@app.route("/servico/gestão/consultasAgendadas/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/servico/gestão/consultasAgendadas/sobre/contato")
def contato():
    return render_template("contato.html")

@app.route("/servico/gestão/consultasAgendadas/sobre/contato/usuario")
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