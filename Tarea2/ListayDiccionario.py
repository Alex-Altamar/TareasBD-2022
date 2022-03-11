def lista():

    print("")
    print("")

    print("********** IMPRESION DE LISTAS **********")

    print("")
    print("")

    listaDatosRafa = ["Rafael", "Amaya Fajardo", "Ing de Sistemas", 22, "10mo semestre", ["calle 10", 11, 44]]

    for i in range(len(listaDatosRafa)):
        print(listaDatosRafa[i])

    listaDatosRafa.insert(1, "Jose")

    print("")
    print("")

    j = 0
    while j < len(listaDatosRafa):
        print(listaDatosRafa[j])
        j = j + 1

    print("")
    print("")

    del listaDatosRafa[6]

    print("")
    print("")

    for i in range(len(listaDatosRafa)):
        print(listaDatosRafa[i])

    print("")
    print("")

    listaDatosRafa.remove(22)

    print("")
    print("")

    j = 0
    while j < len(listaDatosRafa):
        print(listaDatosRafa[j])
        j = j + 1

    print("")
    print("")


def diccionario():
    
    print("********** IMPRESION DE DICCIONARIO **********")

    print("")
    print("")

    rafael = {
        "datosbasicos": {
            "nombre": "rafael",
            "apellido": "amaya",
            "edad": 22,
            "celular": "322 618 0402",
        },

        "datosacademicos": {
            "universidad": "Universidad de la Guajira",
            "programa": "Ing de Sistemas",
            "facultad": "Ingenieria",
            "semestre": 20
        }
    }

    print(rafael)

    print("")
    print("")

    print(f"nombre: {rafael['datosbasicos']['nombre']} {rafael['datosbasicos']['apellido']}")

    print(f"programa: {rafael['datosacademicos']['programa']}")




def main():
    lista()
    diccionario()


if __name__ == "__main__":
    main()