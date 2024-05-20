import psycopg2
from model.conexaodb import *
from flask import Flask, render_template,url_for, request, redirect,abort
import psycopg2
import model

def logar():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Aqui você precisa fazer a consulta ao banco de dados para verificar as credenciais
        banco = Banco()
        banco.connec()
        consulta = "SELECT * FROM users WHERE username = %s AND senha = %s"
        resultado = banco.select(consulta, (username, password))
        banco.fechar_conexao()

        if resultado:
            # Login bem-sucedido, redirecione para a página principal
            return redirect(url_for('inicio'))
        else:
            # Credenciais inválidas, exiba uma mensagem de erro
            #abort(401)
            return render_template('login.html', error='Credenciais inválidas. Tente novamente.')

    return render_template('login.html', error=None)


def saude():
    return render_template('pages/saude.html')

