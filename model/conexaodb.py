# -*- coding: latin-1 -*-
import psycopg2
class Banco:
    def __init__(self, database="system", host="localhost", user="postgres", password="1234", port="5432"):


        self.database = database
        self.host = host
        self.user = user
        self.passwd = password
        self.port = port

    def connec(self):
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

            return self.con  # Adiciona esta linha para retornar a conexão

        except psycopg2.Error as e:
            print("Erro ao conectar ao banco de dados:", e)

    def dml(self,sql,dados):
        self.cur.execute(sql,dados)
        self.con.commit()
        self.fechar_conexao()

    def select_one(self, consulta, parametros):
        """
        Executa a consulta SQL e retorna apenas a primeira linha de resultado.
        """
        self.cur.execute(consulta, parametros)
        resultado = self.cur.fetchone()
        return resultado

    def select(self, consulta, parametros):
        # Executa a consulta SQL e retorna os resultados usando fetchall()

        self.cur.execute(consulta, parametros)
        resultados = self.cur.fetchall()
        return resultados

    def fechar_conexao(self):
        try:
            self.cur.close()
            self.con.close()
            print("Conexão encerrada.")
        except psycopg2.Error as e:
            print("Erro ao fechar conexão:", e)

    def fetchone(self):
        pass

