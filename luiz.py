import json
from flask import Flask, render_template, redirect, url_for, request, flash
from flask import make_response
from functools import wraps
import jwt
import secrets
from flask_cors import CORS
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from modulos.conexao import ConexaoHandler
from flask_jwt_extended import jwt_required, get_jwt_identity
from modulos.login import LoginHandler
import requests
from modulos.codechat import CodeChatAPI
from flask import Markup
from jwt.exceptions import DecodeError


app.secret_key = 'h7k@54tE$e0s1CfR!gKp2vQb6'
# Chave secreta para assinar o JWT (mantenha-a segura na vida real)
SECRET_KEY = 'm1nha_C#4v3_s3cr3t@_JWT'
"""
     Gera um token JWT para o nome de usuário fornecido.

     :param username: O nome de usuário para o qual o token JWT é gerado.
     :tipo de nome de usuário: str
     :return: O token JWT gerado.
     :rtype: str
"""
# Função para gerar o token JWT com expiração de 1 dia
def generate_jwt_token(username):
    expiration = datetime.utcnow() + timedelta(days=1)
    payload = {
        'username': username,
        'exp': expiration,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token
# Decorador que verifica se o usuário está autenticado antes de executar a função.
def requires_authentication(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('jwt_token')
        if token:
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
                username = payload['username']
                if username is not None:
                    return redirect(url_for('painel'))
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                pass
        return f(*args, **kwargs)
    return decorated_function
# Rota para a página inicial (login)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
@requires_authentication
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id, token = login_handler.fazer_login(username, password)
        if token is not None:
            payload = {'id': user_id, 'username': username}
            token = jwt.encode(payload, SECRET_KEY)
            response = make_response(redirect(url_for('painel')))
            response.set_cookie('jwt_token', token, httponly=True)
            return response
        else:
            flash('Credenciais inválidas. Tente novamente.', 'error')
    return render_template('login.html', error=None)
"""
     Manipula a rota '/painel' para solicitações GET e POST.
     :return: Se o usuário for autenticado, retorna uma resposta JSON com uma mensagem de sucesso e código de status 200 para solicitações POST.
         Para solicitações GET, renderiza o modelo 'painel/index.html' com o nome de usuário do usuário autenticado e o registro de data e hora do último login.
         Se o usuário não for autenticado, renderiza o modelo 'index.html' sem nenhuma mensagem de erro.
"""
@app.route('/painel', methods=['GET', 'POST'])
def painel():
    token = request.cookies.get('jwt_token')
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            username = payload['username']
            id = payload['id']

            if request.method == 'POST':
                return jsonify({'message': 'Usuário autenticado com sucesso.'}), 200
            else:
                # Aqui você pode buscar informações do usuário no banco de dados
                # utilizando o 'username' que foi obtido do token
                user = payload['username']
                if user:
                    return render_template('painel/index.html',
                                           username=username,id=id)
            return render_template('index.html', error=None)
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            pass
    return render_template('index.html', error=None)