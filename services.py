import psycopg2
from model.conexaodb import Banco
from flask import Flask, render_template, url_for, request, redirect, abort
import jwt

SECRET_KEY = 'SECRET_KEY'


class loginhandler:
    def logar(self,username, password):
        # Aqui você precisa fazer a consulta ao banco de dados para verificar as credenciais
        banco = Banco()
        conn = banco.connec()  # Mudança: use 'connect' em vez de 'connec'
        cur = conn.cursor()
        consulta = "SELECT * FROM users WHERE username = %s AND senha = %s"
        cur.execute(consulta, (username, password))

        # Mudança: usar fetchone para obter o resultado da consulta
        row = cur.fetchone()

        # Mudança: adicionar manipulação de exceção para psycopg2.errors
        try:
            if row:
                # Atribui os valores das colunas a variáveis individuais, se necessário
                id = row[0]
                username = row[1]

                # Crie o token JWT com os dados do usuário
                token = jwt.encode({
                    'id': id,
                    'username': username
                }, SECRET_KEY, algorithm='HS256')  # Mudança: adicionei o algoritmo

                # Retorna o ID do usuário e o token JWT
                print(token,id)
                return id, token

            else:
                # Falha no login
                return None, None
        except (IndexError, psycopg2.errors.UniqueViolation):
            # Trata exceção para quando não há resultados ou violação única
            return None, None


def saude():
    return render_template('pages/saude.html')



