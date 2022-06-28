import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/NovoLivro', methods=['POST'])
def create_emp():
    try:
        _json = request.json
        _titulo = _json['titulo']
        _autor = _json['autor']
        _genero = _json['genero']
        _preco = _json['preco']

        if _titulo and _autor and _preco  and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO employee(titulo, autor,genero, preco) VALUES(%s, %s, %s, %s)"
            bindData = (_titulo, _autor,  _genero, _preco)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Adicionado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/livro',methods=['GET'])
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, titulo, autor, genero, preco FROM employee")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_autor/<string:autor>',methods=['GET'])
def delete_autor(autor):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employee WHERE id =%s", (autor,))
            conn.commit()
            respone = jsonify('Deletado com sucesso!')
            respone.status_code = 200
            return respone
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


@app.route('/AtualizarLivro/<id>', methods=['PUT'])
def update_emp(id):
    try:
        _json = request.json
        _id = _json['id']
        _titulo = _json['titulo']
        _autor = _json['autor']
        _genero = _json['genero']
        _preco = _json['preco']
        if _titulo and _autor and _genero and _preco and _id and request.method == 'PUT':
            sqlQuery = "UPDATE employee SET titulo=%s, autor=%s, genero=%s, preco=%s WHERE id=%s"
            bindData = (_titulo, _autor, _genero, _preco, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Atualizado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#procurar por nome
@app.route('/PROCURARlIVRO_autor/<string:autor>',methods=['GET'])
def emp_autor(autor):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, titulo, autor, genero, preco FROM employee WHERE autor =%s", autor)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/eliminarLivro/<id>', methods=['DELETE'])
def delete_emp(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employee WHERE id =%s", (id,))
        conn.commit()
        respone = jsonify('Deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#get total de livros
@app.route('/totallivros', methods=['GET'])    #criar a rota
def get_livros_total():  #criar a funcao
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "SELECT count(autor)  FROM employee"
        cursor.execute(query)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#livro mais caro
@app.route('/livroMaisCaro', methods=['GET'])    #criar a rota
def get_livrosCaro():  #criar a funcao
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "SELECT MAX(preco)  FROM employee"
        cursor.execute(query)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#livro mais BARATO
@app.route('/livrobarato', methods=['GET'])    #criar a rota
def get_livrosbarato():  #criar a funcao
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "SELECT MIN(preco)  FROM employee"
        cursor.execute(query)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
#CD/DVD
@app.route('/cd',methods=['GET'])
def cd():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, tituloalbum, artista, ano, genero, num_disco, duracao, preco FROM dvd")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#procurar por nome em comum
@app.route('/listar_autor_artistacomun',methods=['GET'])
def comun_autor():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM employee  INNER JOIN dvd  ON employee.autor = dvd.artista ")
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()




@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)