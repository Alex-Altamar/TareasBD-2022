import datetime

# Almacena todas las ids disponibles para las nuevas notas
ultima_id = 0

class Persona:
    '''Representa una nota en el cuaderno. Se compara con un String
    en las búsquedas y las etiquetas para cada nota'''
    def __init__(self,tags=''):
        '''inicializa una nota con memo y opcional tags
        separado por comas. Automáticamente configura la fecha
        de creación de la nota y una única id'''
        self.cedula=input("Ingrese numero de cedula: ")
        self.nombre=input("Ingrese el nombre:   ")
        self.apellido=input("Ingrese el apellido:  ")
        self.direccion=input("Ingrese la direccion: ")
        self.telefono=input("Ingrese el telefono:  ")
        self.tags = tags
        self.creation_date = datetime.date.today()
        global ultima_id
        ultima_id += 1
        self.id = ultima_id
    def match(self, filter):
        '''Determina si esta nota concuerda con el filtro
        de texto. Devuelve True si concuerda, en otro caso False.
        Búsqueda es case sensitive y compara tanto con text como
        con tags.'''
        return filter in self.cedula or filter in self.tags

class Empleado():
    '''Representa una colección de notas que pueden ser etiquetadas,
    modificadas, y se pueden buscar.'''

    def __init__(self):
        super().__init__()
        '''Inicialiaza lista pleado con una lista vacía.'''
        self.lista = []

    def nuevo_empleado(self, cedula, nombre, apellido, telefono, direccion, tags=''):
        '''Crea un nuevo empleado y lo añade a la lista.'''
        self.lista.append(Persona(cedula, nombre, apellido, telefono, direccion, tags))

    def _encontrar_empleado(self, persona_id):
        '''Localiza el empleado con la id dada.'''
        for persona in self.lista:
            if str (persona.id) == str(persona_id):
                return persona
        return None

    def modificar_empleado(self, persona_id, cedula, nombre, apellido, telefono, direccion):
        '''Encuentra la nota con la id dada y cambia al valor dado.'''
        persona = self._encontrar_empleado(persona_id)
        if persona:
            persona.cedula, persona.nombre, persona.apellido, persona.telefono, persona.direccion =  cedula, nombre, apellido, telefono, direccion
            return True
        return False

    def modificar_tags(self, persona_id, tags):
        '''Encuentra la nota con la id dada y cambia sus
        tags al valor dado.'''
        persona = self._encontrar_persona(persona_id)
        if persona:
            persona.tags = tags
            return True
        return False
    def search(self, filter):
        '''Encuentra todas las notas que concuerdan con
        el filtro string dado.'''
        return [persona for persona in self.lista if
                persona.match(filter)]