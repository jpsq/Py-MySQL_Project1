import datetime
import hashlib
import modulo1.conexion as c

conexion = c.conectar()
database = conexion[0]
cursor = conexion[1]

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
        except c.ExcepcionEmailDuplicado():
           print("Ya existe un usuario registrado con este correo electronico")
           result = [0,self] #ninguna columna afectada
        except Exception as e:
            print("Ha ocurrido un error", type(e).__name__)
            result = [0,self] #ninguna columna afectada
        
        return result #end of method
    
    def identificar(self):

        try:
            sql = "select * from users where users_email = %s and users_password = %s" #da error si el select no es con *
            usuario_a_loguear = [self.email,hashlib.sha256(self.password.encode('utf-8')).hexdigest()]

            cursor.execute(sql,usuario_a_loguear)
            result = cursor.fetchone()
            
            return result
        
        except Exception as e:
            
            print(type(e).__name__)
            print("Login fallido.")
