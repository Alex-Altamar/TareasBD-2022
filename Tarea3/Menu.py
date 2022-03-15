def menu():
    
    menuPrincipal = int(input("Menu Principal: \n 1 - Insertar Persona \n 2 - Mostrar Persona \n 3 - Eliminar Persona \n 0 - Salir \n "))

    while menuPrincipal !=0:
        if menuPrincipal == 1:
            print("Insertando Persona")
        elif menuPrincipal == 2:
            print("Mostrando Persona")
        elif menuPrincipal == 3:
            print("Eliminando Persona")
        else:
            print("Digita una correcta")

        menuPrincipal = int(input("Menu Principal: \n 1 - Insertar Persona \n 2 - Mostrar Persona \n 3 - Eliminar Persona \n 0 - Salir \n "))



def main():
	menu()
 
	


if __name__ == "__main__":
    main()