from flask import Flask, render_template, url_for, request, redirect, make_response, flash, make_response, jsonify
from model.conexaodb import *
import psycopg2
import model
from services import*
from datetime import datetime, timedelta
from functools import wraps
import requests
import jwt


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
    error = None  # Inicialize a variável de erro como None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id, token = loginhandler.logar("",username, password)
        if token is not None:
            payload = {'username': username}
            token = jwt.encode(payload, SECRET_KEY)
            response = make_response(redirect(url_for('inicio')))
            response.set_cookie('jwt_token', token, httponly=True)
            return response
        else:
            error = 'Credenciais inválidas. Tente novamente.'  # Defina a mensagem de erro
    return render_template('login.html', error=error)  # Passe a variável de erro para o template



@app.route('/inicio')
def inicio():
    token = request.cookies.get('jwt_token')
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            username = payload.get('username')
            id = payload.get('id')

            if request.method == 'POST':
                return jsonify({'message': 'Usuário autenticado com sucesso.'}), 200
            else:
                # Aqui você pode buscar informações do usuário no banco de dados
                # utilizando o 'username' que foi obtido do token
                user = payload['username']
                if user:
                    return render_template('inicio.html',
                                           username=username, id=id)
            return render_template('inicio.html', error=None)
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            pass
    return render_template('login.html', error=None)

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