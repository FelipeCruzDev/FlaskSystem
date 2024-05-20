from flask import Flask, render_template,url_for, request, redirect
from model.conexaodb import *
import psycopg2
import model
from services import*

app = Flask(__name__)

@app.route('/login',methods=['GET', 'POST'])

def login():
    return logar()


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route("/saude")

def saude ():
    return render_template('saude.html')

if __name__ == '__main__':
    app.run(debug=True)

