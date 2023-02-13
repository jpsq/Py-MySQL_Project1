#dentro del paquete usuarios

class Acciones:

    def registro(self):
        print("\nIniciando registro en el sistema...")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo electronico: ")
        password = input("Ingrese su contrasenia:")

    def login(self):
        print("\nIniciando logueo en el sistema...")
        correo = input("Ingrese su correo electronico: ")
        password = input("Ingrese su contrasenia: ")