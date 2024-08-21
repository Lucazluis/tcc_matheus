from flask import Flask, render_template, redirect, request, session
import model.BD


def servicosAgendamento():
    conexao  = model.BD.iniciaConexao()
    cursor = conexao.cursor()
    query = "SELECT * FROM servico"

    cursor.execute(query)
    resultados = cursor.fetchall()

    return resultados

def criarServiço():
    pass

