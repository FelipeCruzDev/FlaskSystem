import psycopg2
from model.conexaodb import*
def inserir_usuario(username, senha):
            banco = Banco()
            banco.connec()
            inserir = """INSERT INTO users (username, senha) VALUES (%s, %s)"""
            print("Usuário adicionado com sucesso!")
            sqls = username,senha
            banco.dml(inserir,sqls)



inserir_usuario("Luizlindao2","123")