from flask import Flask, render_template,url_for, request, redirect
from model.conexaodb import*
import psycopg2
import model



app = Flask(__name__)

@app.route('/login',methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if username in USERS and USERS[username] == password:
                # Login bem-sucedido, redirecione para a página principal
                return redirect(url_for('pagina_principal'))
            else:
                # Credenciais inválidas, exiba uma mensagem de erro
                return render_template('login.html', error='Credenciais inválidas. Tente novamente.')
        return render_template('login.html', error=None)



@app.route('/inicio')
def saude():
    return render_template('index1.html')

@app.route("/saude")
def site():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)

