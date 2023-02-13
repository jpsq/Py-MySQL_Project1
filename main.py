"""
    Proyecto Python y MySQL
    - Abrir asistente
    - Login
    - Al elegir registro, creara un usuario en la bd
    - Al elegir login, loguera y luego preguntara si:
    - Crear nota, mostrar notas o borrarlas.
"""

print("""

    Acciones disponibles:
        - registro
        - login
""")

accion = input("Elije una opcion: ")

if accion == "registro":
    print("\nIniciando registro en el sistema...")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo electronico: ")
    password = input("Ingrese su contrasenia:")
    
elif accion == "login":
    print("\nIniciando logueo en el sistema...")
    correo = input("Ingrese su correo electronico: ")
    password = input("Ingrese su contrasenia: ")
    

  