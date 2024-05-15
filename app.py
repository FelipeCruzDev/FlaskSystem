from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/login')
def inicio():
    return render_template('index.html')

@app.route('/inicio')
def saude():
    return render_template('index1.html')

@app.route("/saude")
def site():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)

