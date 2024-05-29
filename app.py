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


@app.route('/topicos',methods=['GET', 'POST'])
def topicos():
    if request.method == 'POST':
        setor = request.form.get('setor')
        main = Main()
        id_dp= main.consulta_id_departamento_topico(setor)


        topicos = main.consultar_topicos(id_dp)


        print(f"Setor recebido: {setor}", topicos)
        # Aqui você pode adicionar o código para processar os dados do setor
        return 'Dados do setor recebidos com sucesso'

if __name__ == "__main__":
    app.run(debug=True)


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
