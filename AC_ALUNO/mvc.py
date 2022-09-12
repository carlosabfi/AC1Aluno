import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'alunos'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('formulario.html')


@app.route('/formulario', methods=['POST', 'GET'])
def aluno():
    nome = request.form['nome']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    if nome and cpf and endereco:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into alunos (user_name, user_cpf, user_endereco) VALUES (%s, %s, %s)', (nome, cpf, endereco))
        conn.commit()
    return render_template('formulario.html')


@app.route('/lista', methods=['POST', 'GET'])
def listaraluno():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select user_name, user_cpf, user_endereco from alunos')
    data = cursor.fetchall()
    conn.commit()
    return render_template('lista.html', datas=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8888))
    app.run(host='0.0.0.0', port=port)
