from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin321**'
app.config['MYSQL_DB'] = 'usuarios'

mysql = MySQL()



if __name__ == '__main__':
    app.run(port = 3306, debug = True)


