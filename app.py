from flask import Flask, render_template, url_for, request, redirect, make_response, flash, make_response, jsonify
from model.conexaodb import *
import psycopg2
import model
import re
from services import*
from datetime import datetime, timedelta
from functools import wraps
import requests
import jwt
from model.main import Main




app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

SECRET_KEY = 'SECRET_KEY'
"""
     Gera um token JWT para o nome de usuário fornecido.

     :param username: O nome de usuário para o qual o token JWT é gerado.
     :tipo de nome de usuário: str
     :return: O token JWT gerado.
     :rtype: str
"""

from flask import Flask, render_template, jsonify

app = Flask(__name__)




def generate_jwt_token(username):
    expiration = datetime.utcnow() + timedelta(days=1)
    payload = {
        'id': id,
        'username': username,
        'exp': expiration,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id, token = loginhandler.logar("", username, password)
        if token is not None:
            id = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            consulta = id.get('id')

            payload = {'id': consulta}  # Modifica o payload para passar o nome do departamento
            token = jwt.encode(payload, SECRET_KEY)
            response = make_response(redirect(url_for('inicio')))
            response.set_cookie('jwt_token', token, httponly=True)
            return response

        else:
            error = 'Credenciais inválidas. Tente novamente.'
    return render_template('login.html', error=error)


@app.route('/inicio')
def inicio():
    token = request.cookies.get('jwt_token')
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            id = payload.get('id')

            main = Main()
            id_dp = main.consulta_id_dp(id)

            departamento = main.consultar_dp(id_dp[0], id)  # Aqui estamos pegando apenas o primeiro ID de departamento, assumindo que é o único


            user = payload['id']

            if user:
                print(departamento)
                return render_template('inicio.html', id=id, departamento=departamento,id_dp=id_dp)
            return render_template('inicio.html', error=None)
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            pass
    return render_template('login.html', error=None)





def verificar_permissao_usuario(id_usuario, setor):
    main = Main()  # Supondo que Main() seja uma classe que gerencia conexão com o banco de dados

    # Consulta ao banco de dados para verificar se o usuário tem acesso total
    consultar_acesso_total = "SELECT COUNT(*) FROM users WHERE id = %s AND acesso_total = true"
    sqls_acesso_total = (id_usuario,)
    resultado_acesso_total = main.banco.select_one(consultar_acesso_total, sqls_acesso_total)

    # Verifica se o resultado da consulta de acesso total é maior que zero, o que indica que o usuário tem acesso total
    if resultado_acesso_total and resultado_acesso_total[0] > 0:
        return True  # Se o usuário tem acesso total, retorna True

    # Consulta ao banco de dados para verificar se o setor existe e se o usuário tem permissão para acessá-lo
    consultar_departamento_usuario = "SELECT COUNT(*) FROM users WHERE id = %s AND departamento_id IN (SELECT id FROM departamento WHERE nomedepartamento = %s)"
    sqls_departamento_usuario = (id_usuario, setor)
    resultado = main.banco.select_one(consultar_departamento_usuario, sqls_departamento_usuario)

    # Verifica se o resultado da consulta é maior que zero, o que indica que o usuário tem permissão para acessar o setor
    if resultado and resultado[0] > 0:
        return True  # Retorna True se o usuário tem permissão para acessar o setor
    else:
        return False  # Retorna False se o usuário não tem permissão para acessar o setor



@app.route('/topicos/<setor>', methods=['GET', 'POST'])
def topicos(setor):
    token = request.cookies.get('jwt_token')
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            id_usuario = payload.get('id')

            # Verifica se o usuário tem permissão para acessar o setor
            if verificar_permissao_usuario(id_usuario, setor):
                main = Main()
                id_dp = main.consulta_id_departamento_topico(setor)
                topicos = main.consultar_topicos(id_dp)

                if request.method == 'POST':
                    # Lidar com a lógica do método POST
                    print(f"Setor recebido: {setor}", topicos)
                else:
                    # Lidar com a lógica do método GET
                    print(f"Setor recebido: {setor}", topicos)

                return render_template('topicos.html', topicos=topicos)
            else:
                # Se o usuário não tiver permissão, redirecione para uma página de acesso negado
                return render_template('acesso_negado.html')
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return redirect(url_for('login'))
    return redirect(url_for('login'))
@app.route("/saude")

def saude ():
    token = request.cookies.get('jwt_token')
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            username = payload.get('username')
            user_id = payload.get('id')
            # Aqui você pode implementar lógica adicional para a rota de "/saude"
            return render_template('saude.html', username=username, id=user_id)
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            pass
    return render_template('login.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)
