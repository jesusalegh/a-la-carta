from flask import Flask, render_template, request, url_for, redirect
import mysql.connector


app = Flask(__name__)

cnx = mysql.connector.connect(user = 'jesusalegh',
                              password= 'admin321**',
                              host = '127.0.0.1',
                              db = 'usuarios')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create_account', methods = ['GET','POST'])
def login():
     if request.method == 'POST':
        Nombres = request.form['Nombres']
        Apellidos = request.form['Apellidos']
        Email = request.form['Email']
        Contraseña = request.form['Contraseña']
        cursor = cnx.cursor()
        info = 'INSERT INTO usuarios.usuario (Nombres, Apellidos, Email, Contraseña) VALUES (%s, %s, %s, %s)'
        datos = (Nombres, Apellidos, Email, Contraseña)
        cursor.execute(info, datos)
        cnx.commit()
        return redirect('inicio_sesion')
     else:
        return render_template('create_account.html')

@app.route('/inicio_sesion')
def signin():
    return render_template('inicio_sesion.html')

@app.route('/change_password')
def change_pass():
    return render_template('change_pass.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')



if __name__ == '__main__':
    app.run(port = 5000, debug = True)