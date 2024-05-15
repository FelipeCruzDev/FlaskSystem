# -*- coding: latin-1 -*-
import psycopg2

class Banco:
    def __init__(self, database="system", host="localhost", user="postgres", password="1234", port="5432"):
        self.database = database
        self.host = host
        self.user = user
        self.passwd = password
        self.port = port

    def conec(self):
        try:
            self.con = psycopg2.connect(
                database=self.database,
                host=self.host,
                user=self.user,
                password=self.passwd,
                port=self.port
            )
            self.cur = self.con.cursor()
            print("Conexão bem-sucedida!")
        except psycopg2.Error as e:
            print("Erro ao conectar ao banco de dados:", e)

# Exemplo de uso:
# Criando uma instância da classe Banco
banco = Banco()

# Chamando o método conec para conectar ao banco de dados
banco.conec()

