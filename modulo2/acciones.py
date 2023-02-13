import modulo2.notas as n

class Acciones:

    def crear(self,usuario):
        titulo = input("Ingrese el titulo de la nota: ")
        descripcion = input("Escriba la nota: ")

        nota = n.Notas(usuario[0],titulo,descripcion)
        resultado = nota.guardar()

        if(resultado[0] >= 1):
            print(f"Nota {nota.titulo} guardada")
        else:
            print("Problema al guardar la nota")

    def mostrar(self,usuario):
        print("Mostrando notas: ")

        nota = n.Notas(usuario[0],"","")
        notas = nota.mostrar()
        
        for nota in notas:
            print("*******************************************")
            print(nota[2])
            print(nota[3])
            print(f"Fecha de creacion: {nota[4]}")
            print("*******************************************")

    def borrar(self,usuario):
        print(f"\nIniciando borrado de nota...")
        titulo = input("Ingrese el titulo de la nota a borrar: ")

        nota = n.Notas(usuario[0],titulo,"")
        resultado = nota.eliminar()

        if resultado[0] >= 1:
            print("Nota borrada.")
        else:
            print("Error, no se pudo borrar la nota.")