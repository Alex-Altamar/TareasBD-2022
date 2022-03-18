import sys
from api.library import *

class Menu:
    '''Muestra un menu y responde a elecciones cuando se ejecuta.'''
    def __init__(self):
        self.empleado = Empleado()
        self.elecciones = {
                "1" : self.add_empleado,
                "2" : self.mostrar_empleados,
                "3" : self.search_empleados,
                "4" : self.modificar_empleado,
                "5" : self.quit
                } 

    def mostrar_menu(self):
        print("""
Menu Cuaderno

1 Añadir Empleado
2 Mostrar todos los empleados
3 Buscar empleado
4 Modificar empelado
5 Salir
""")

    def run(self):
        '''Muestra el menú y responde a las elecciones.'''
        while True:
            self.mostrar_menu()
            eleccion = input("Escribe una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print("{0} no es una elección válida".format(eleccion))

    def mostrar_empleados(self, lista=None):
        if not lista:
            lista = self.empleado.lista
        for persona in lista:
            print("{0}: {1}\n{2}\n{3}\n{4}\n{5}\n{6}".format(persona.id, persona.cedula, persona.nombre, persona.apellido, persona.telefono, persona.direccion, persona.tags))

    def search_empleados(self):
        filter = input("Buscar por ID: ")
        lista = self.empleado.search(filter)
        self.mostrar_empleados(lista)

    def add_empleado(self):
        cedula=input("Ingrese numero de cedula: ")
        nombre=input("Ingrese el nombre:   ")
        apellido=input("Ingrese el apellido:  ")
        direccion=input("Ingrese la direccion: ")
        telefono=input("Ingrese el telefono:  ")
        self.empleado.nuevo_empleado(Persona(cedula, nombre, apellido, telefono, direccion))

        print("Tu empleado ha sido añadido.")

    def modificar_empleado(self):
        id = input("Escribe el id de un empleado: ")
        cedula=input("Ingrese numero de cedula: ")
        nombre=input("Ingrese el nombre:   ")
        apellido=input("Ingrese el apellido:  ")
        direccion=input("Ingrese la direccion: ")
        telefono=input("Ingrese el telefono:  ")
        tags = input("Escribe tags: ")
        if Persona:
            self.empleado.modificar_empleado(id, cedula, nombre, apellido, direccion, telefono, tags)
        if tags:
            self.empleado.modificar_tags(id, tags)

    def quit(self):
        print("Gracias por usar tu cuaderno hoy.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
