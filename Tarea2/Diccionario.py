

def main():
    #diccionario
    # persona={
    #     "nombre":"Diego",
    #     "apellido":"Tarazona",
    #     "edad":"23"
    # }

    persona={
        "datosPersonales":{
        "nombre":"Diego",
        "apellido":"Tarazona",
        "edad":"23"
        },
        "salarial":{
        "salario":"2000000",
        "subsidioT":"500000",
        "subsidioA":"600000"

        }
    }
        


    #otras maneras de imprimir
    # print(persona["nombre"]+ " " +persona["apellido"])
    # print(f"{persona['nombre']} {persona['apellido']}")
    print(f"Nombre: {persona['datosPersonales']} Salarial: {persona['salarial']}")
    print("")

   
    

if __name__=="__main__":
    main()