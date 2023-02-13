import modulo1.conexion as c

conexion = c.conectar()
database = conexion[0]
cursor = conexion[1]

class Notas:

    def __init__(self,usuario_id,titulo,descripcion):
        self.usuario_id=usuario_id
        self.titulo=titulo
        self.descripcion=descripcion
    
    def guardar(self):
        sql = "insert into notes values(null,%s,%s,%s,now())"
        nota_a_insertar = (self.usuario_id,self.titulo,self.descripcion)

        cursor.execute(sql,nota_a_insertar)
        database.commit()

        return [cursor.rowcount,self]
    
    def mostrar(self):
        sql = f"select * from notes where notes_usuarios_id={self.usuario_id}"
        
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def eliminar(self):
        sql = f"delete from notes where notes_title='{self.titulo}' AND notes_usuarios_id={self.usuario_id}"
        #forma para el el titulo ingresado este contenido en el titulo guardado en la bd notes_title LIKE '%{titulo}%'
        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount,self]