import psycopg2
from model.conexaodb import *
from flask import Flask, render_template,url_for, request, redirect,abort
import psycopg2
import model


def inserir_usuario(username, senha):
    banco = Banco()
    banco.connec()
    inserir = """INSERT INTO users (username, senha) VALUES (%s, %s)"""
    print("Usuário adicionado com sucesso!")
    sqls = username, senha
    banco.dml(inserir, sqls)


def deletar_usuario(username):
    banco = Banco()
    banco.connec()
    deletar = """DELETE FROM users WHERE username = %s"""
    print("Usuário excluído com sucesso!")
    sqls = (username,)
    banco.dml(deletar, sqls)


def selecionar_usuario(username):
    banco = Banco()
    banco.connec()
    consultar = """SELECT * FROM users WHERE username = %s"""
    sqls = (username,)
    resultado = banco.select(consultar, sqls)

    if resultado:
        print("Usuário encontrado!")
        banco.fechar_conexao()
        return resultado
    else:
        print("Usuário não encontrado.")
        banco.fechar_conexao()
        return None



