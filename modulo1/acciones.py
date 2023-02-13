#dentro del paquete modulo1
import modulo1.usuarios as modulo
import modulo2.acciones as modulo2

class Acciones:

    def registro(self):
        print("\nIniciando registro en el sistema...")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo electronico: ")
        password = input("Ingrese su contrasenia:")

        usuario = modulo.Usuario(nombre,apellido,correo,password)
        registro = usuario.registrar() #lo registro con el metodo de la clase usuario

        if(registro[0] >= 1): #pregunta por el resultado de la funcion registro
            print(f"Usuario {registro[1].nombre} registrado")
        else:
            print("Error en el proceso de registro")

    def login(self):
        print("\nIniciando logueo en el sistema...")
        correo = input("Ingrese su correo electronico: ")
        password = input("Ingrese su contrasenia: ")

        usuario = modulo.Usuario('','',correo,password)
        login = usuario.identificar()

        if correo == login[3]:
            print(f"Usuario {login[1]} logueado con exito")
            self.sistemaNotas(login)


    def sistemaNotas(self,usuario):
        print("""
            Acciones disponibles:
            - Crear notas (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)

        accion = input("¿Que desea hacer? ")
        sistemaNota = modulo2.Acciones() 
        
        if accion=="crear":
            sistemaNota.crear(usuario)
            self.sistemaNotas(usuario)

        elif accion=="mostrar":
            sistemaNota.mostrar(usuario)      
            self.sistemaNotas(usuario)
            
        elif accion=="eliminar":
            sistemaNota.borrar(usuario)
            self.sistemaNotas(usuario)

        elif accion=="salir":
            exit()
        else: self.sistemaNotas(usuario)