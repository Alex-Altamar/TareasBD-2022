listaEmpleados = []      # Lista Vacia
empleado = {}            # Diccionario Vacio

def agregarEmpleado():
    #creando el empleado nuevo vacio
    empleado = {}


    #creado el empleado con  datos del usuario
    empleado["codigo"] = input("Ingrese el Codigo ==>  ")
    empleado["nombre"] = input("Ingrese el Nombre ==>  ")
    empleado["apellido"] = input("Ingrese el Apellido ==>  ")
    empleado["direccion"] = input("Ingrese la Direccion ==>  ")
    empleado["telefono"] = input("Ingrese el Telefono ==>  ")
    empleado["sueldo"] = input("Ingrese el Sueldo ==>  ")

    #agregar ese empleado a la lista
    listaEmpleados.append(empleado)

def mostrarEmpleado():
    print("******************************")
    print("      LISTA DE EMPLEADOS      ")
    print("******************************")
    for emp in listaEmpleados:
        print(emp["codigo"], "  |  ", emp["nombre"], "  |  ", emp["apellido"], "  |  ", emp["direccion"], "  |  ", emp["telefono"], "  |  ", emp["sueldo"])

def buscarCodigo(codigo):
    #recorremos la lista

    for emp in listaEmpleados: 
        if (emp["codigo"] == codigo):
            listaEmpleados.remove(empleado)


def buscarNombre(nombre):
    for emp in listaEmpleados: 
        if (emp["nombre"] == nombre):
            listaEmpleados.remove(empleado)

    

def main():
    while(True):
        print("******************************")
        print("             MENU             ")
        print("******************************")
        print("1 - AGREGAR EMPLEADO")
        print("2 - ELIMINAR EMPLEADO")
        print("3 - MOSTRAR EMPLEADO")
        print("4 - SALIR")
        
        while(True):
            op = input("Ingrese Opcion: ")
            if (op != ""):
                break

        if (op == "1"):
            agregarEmpleado()
        elif (op == "2"):
            mostrarEmpleado()
        elif (op == "3"):
            print("1 - Eliminar Por Codigo")
            print("2 - Eliminar Por Nombre")
            op2 = input("Ingrese la Opcion == >  ")

            if (op2 == "1"):
                 codigo = input("Codigo: ")
                 buscarCodigo(codigo)
            elif (op2 == "2"):
                 nombre = input("Nombre: ")
                 buscarNombre(nombre)  
        elif (op == "4"):
            break