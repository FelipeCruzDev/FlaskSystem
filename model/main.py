import psycopg2
from model.conexaodb import Banco
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

class Main:
    def __init__(self):
        self.banco = Banco()
        self.banco.connec()

    def inserir_usuario(self, username, senha):
        inserir = """INSERT INTO users (username, senha) VALUES (%s, %s)"""
        print("Usuário adicionado com sucesso!")
        sqls = (username, senha)
        self.banco.dml(inserir, sqls)

    def deletar_usuario(self, username):
        deletar = """DELETE FROM users WHERE username = %s"""
        print("Usuário excluído com sucesso!")
        sqls = (username,)
        self.banco.dml(deletar, sqls)

    def selecionar_usuario(self, username):
        consultar = """SELECT * FROM users WHERE username = %s"""
        sqls = (username,)
        resultado = self.banco.select(consultar, sqls)
        if resultado:
            print("Usuário encontrado!")
        else:
            print("Usuário não encontrado.")
        return resultado

    def consulta_id_dp(self, id_user):
        consultar = """SELECT departamento_id FROM users WHERE id = %s"""
        sqls = (id_user,)
        resultado = self.banco.select(consultar, sqls)
        return resultado

    def consultar_dp(self, id_dp, id_user):
        if id_user:  # Verifica se o id do usuário não está vazio ou None
            # Construa a consulta SQL para verificar o acesso total do usuário
            consultar_acesso = "SELECT acesso_total FROM users WHERE id = %s"
            sqls_acesso = (id_user,)
            acesso_total = self.banco.select(consultar_acesso, sqls_acesso)

            if acesso_total:  # Verifica se a consulta retornou algum resultado
                if acesso_total[0][0]:  # Verifica se o acesso total está definido como True
                    # Se o usuário tem acesso total, retorna a lista completa de departamentos
                    consultar_departamentos = "SELECT nomedepartamento FROM departamento"
                    lista_departamentos = self.banco.select(consultar_departamentos, ())
                    print(lista_departamentos)
                    return lista_departamentos
                else:
                    # Se o usuário não tem acesso total, retorna apenas o departamento vinculado ao seu ID
                    consultar_departamento_usuario = "SELECT nomedepartamento FROM departamento WHERE id = %s"
                    sqls_departamento_usuario = (id_dp,)
                    departamento_usuario = self.banco.select(consultar_departamento_usuario, sqls_departamento_usuario)
                    return departamento_usuario
            else:
                return "Usuário não encontrado."
        else:
            return "ID de usuário inválido."
