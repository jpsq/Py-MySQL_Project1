from modulo1 import acciones as modulo1

"""
    Proyecto Python y MySQL
    - Abrir asistente
    - Login
    - Al elegir registro, creara un usuario en la bd
    - Al elegir login, loguera y luego preguntara si:
    - Crear nota, mostrar notas o borrarlas.
"""
#pantalla inicial
print("""

    Acciones disponibles:
        - registro
        - login
""")

interactuador = modulo1.Acciones() #creo el objeto
accion = input("¿Que quiere hacer? ")
if accion=="registro":
    interactuador.registro()
elif accion=="login":
    interactuador.login()

