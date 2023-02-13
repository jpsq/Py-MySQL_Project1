import mysql.connector
import datetime
import hashlib

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="49800jil02",
    database="python_proyecto1",
    port=3306
)

cursor = database.cursor(buffered=True)

class Usuario:

    def __init__(self,nombre,apellido,email,password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
    
    #codigos provisionales
    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "insert into users values(null,%s,%s,%s,%s,%s)"
        usuario_a_registrar = (
                               self.nombre,
                               self.apellido,
                               self.email,hashlib.sha256(self.password.encode('utf-8')).hexdigest(),
                               fecha
                               )

        try: #este bloque podria tener un error en el registro, por error de acceso a la bd o email repetido 
            cursor.execute(sql,usuario_a_registrar)
            database.commit()
            result = [cursor.rowcount, self] #retorna cantidad de columnas modificadas por la consulta
        except mysql.connector.errors.IntegrityError:
           print("Ya existe un usuario registrado con este correo electronico")
           result = [0,self] #ninguna columna afectada
        except Exception as e:
            print("Ha ocurrido un error", type(e).__name__)
            result = [0,self] #ninguna columna afectada
        
        return result #end of method
    
    def identificar(self):
        return self.nombre
