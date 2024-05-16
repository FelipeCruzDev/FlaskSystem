from flask import Flask, render_template,url_for, request, redirect,abort
from model.conexaodb import *

import psycopg2
import model



app = Flask(__name__)

@app.route('/login',methods=['GET', 'POST'])

def login():
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
            abort(401)


    return render_template('login.html', error=None)


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route("/saude")
def site():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)

