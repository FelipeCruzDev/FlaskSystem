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
                    # Se o usuário tem acesso total, retorna apenas os nomes dos departamentos
                    consultar_departamentos = "SELECT nomedepartamento FROM departamento"
                    lista_departamentos = self.banco.select(consultar_departamentos, ())

                    # Extrai apenas os nomes dos departamentos da lista de tuplas

                    return lista_departamentos
                    print("Lista de departamentos completa:", nomes_departamentos)
                     # Retorna a lista de nomes dos departamentos
                else:
                    # Se o usuário não tem acesso total, retorna apenas o departamento vinculado ao seu ID
                    consultar_departamento_usuario = "SELECT nomedepartamento FROM departamento WHERE id = %s"
                    sqls_departamento_usuario = (id_dp,)
                    departamento_usuario = self.banco.select(consultar_departamento_usuario, sqls_departamento_usuario)
                    print("Lista de departamentos do usuário:", departamento_usuario)
                    return departamento_usuario  # Retorna a lista de tuplas sem descompactar
            else:
                return "Usuário não encontrado."  # Retorne uma mensagem de erro
        else:
            return "ID de usuário inválido."  # Retorne uma mensagem de errodef consultar_dp(self, id_dp, id_user):
        if id_user:  # Verifica se o id do usuário não está vazio ou None
            # Construa a consulta SQL para verificar o acesso total do usuário
            consultar_acesso = "SELECT acesso_total FROM users WHERE id = %s"
            sqls_acesso = (id_user,)
            acesso_total = self.banco.select(consultar_acesso, sqls_acesso)

            if acesso_total:  # Verifica se a consulta retornou algum resultado
                if acesso_total[0][0]:  # Verifica se o acesso total está definido como True
                    # Se o usuário tem acesso total, retorna apenas os nomes dos departamentos
                    consultar_departamentos = "SELECT nomedepartamento FROM departamento"
                    lista_departamentos = self.banco.select(consultar_departamentos, ())

                    # Extrai apenas os nomes dos departamentos da lista de tuplas

                    return lista_departamentos
                    print("Lista de departamentos completa:", nomes_departamentos)
                     # Retorna a lista de nomes dos departamentos
                else:
                    # Se o usuário não tem acesso total, retorna apenas o departamento vinculado ao seu ID
                    consultar_departamento_usuario = "SELECT nomedepartamento FROM departamento WHERE id = %s"
                    sqls_departamento_usuario = (id_dp,)
                    departamento_usuario = self.banco.select(consultar_departamento_usuario, sqls_departamento_usuario)
                    print("Lista de departamentos do usuário:", departamento_usuario)
                    return departamento_usuario  # Retorna a lista de tuplas sem descompactar
            else:
                return "Usuário não encontrado."  # Retorne uma mensagem de erro
        else:
            return "ID de usuário inválido."  # Retorne uma mensagem de erro

    def consultar_topicos(self, id_departamento):
        try:
            # Consulta SQL para obter os tópicos vinculados ao departamento
            consultar_topicos_departamento = "SELECT id,topico FROM topicos WHERE departamento_id = %s"
            sqls_topicos_departamento = (id_departamento,)
            topicos_departamento = self.banco.select(consultar_topicos_departamento, sqls_topicos_departamento)
            if topicos_departamento:
                conexoes = []
                for row in topicos_departamento:
                    conexao = {
                        'id': row[0],
                        'topico': row[1]
                    }
                    conexoes.append(conexao)

                print (conexoes )


            return topicos_departamento

        except Exception as e:
            return f"Erro ao consultar tópicos: {str(e)}"

    def consulta_id_departamento_topico(self, setor_nome):
        try:
            # Consulta SQL para obter o ID do departamento vinculado ao setor
            consulta_id_departamento = """SELECT id FROM departamento WHERE nomedepartamento = %s"""
            sqls_id_departamento = (setor_nome,)
            departamento_id = self.banco.select(consulta_id_departamento, sqls_id_departamento)

            if departamento_id:
                # Retorna apenas o número do departamento vinculado ao setor
                return departamento_id[0][0]
            else:
                return None  # Retorna None se não houver departamento vinculado ao setor
        except Exception as e:
            return f"Erro ao consultar ID do departamento: {str(e)}"

    def Consulta_checklist(self,user_id,id_topico):
        # Consulta a pergunta da tabela checklist, com filtro no User_id
        consulta = "SELECT pergunta FROM checklist WHERE id_topico AND user_id = %s"
        parametros = (id_topico,user_id)
        checklist = self.banco.select(consulta, parametros)
        print(checklist)
        return checklist

