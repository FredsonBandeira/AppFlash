from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'testingdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)



"""from flask import Flask, json, request, jsonify
from flask_mysqldb import MySQL, MySQLdb  # pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb

app = Flask(__name__)

app.secret_key = "caircocoders-ednalan-2020"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def index():
    return 'index'

@app.route('/livro', methods=['GET'])
def getlistar():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM livro")
    rv = cur.fetchall()
    employee = []
    content = {}
    for result in rv:
        content = {'isbn': result['isbn'], 'titulo': result['titulo'], 'autor': result['autor'],
                   'preco': result['preco']}
        employee.append(content)
        content = {}
    return jsonify(employee)


@app.route('/actualizarlivro/<isbn>', methods=['POST'])
def update_livro(isbn):
        cursor = mysql.connection.cursor()
        file = open('output.json', 'r')
        file_content = file.read()
        file.close()
        sql = "INSERT INTO t1 (tablename) VALUES (%s)"
        val = (json.dumps(file_content))
        cursor.execute(sql, val)
        db.commit()
        db.close()
        return 200

if __name__ == '__main__':
    app.run(debug=True)"""
