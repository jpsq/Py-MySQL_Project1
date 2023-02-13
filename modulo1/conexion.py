import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="49800jil02",
        database="python_proyecto1",
        port=3306
    )
    cursor = database.cursor(buffered=True)

    return [database,cursor]

def ExcepcionEmailDuplicado():
    return mysql.connector.errors.IntegrityError

