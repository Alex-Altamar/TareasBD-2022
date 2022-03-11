#******************************
#    MANEJO DE DICCIONARIOS   *
#******************************

def main ():
   #Aplicacion de los diccionarios estos tienen propiedades y valores

   #crea un diccionario en este caso persona
   persona = {
      "Nombre": "Doris",
      "Apellidos": "Altamar Vanegas",
      "Edad": 20
   }
   
   #crea un diccionario con 2 diccionarios dentro
   persona2 = {
      "Datos Personales": {
      "Nombre": "Alexander",
      "Apellidos": "Altamar Vanegas",
      "Edad": 25,
      },
      "Salarial":{
         "Salario": 1000000,
         "SubTransporte": 50000,
         "SubAlimentacion": 60000 
      }
   }
   print("Muestra diccionario con atributos")
   print(f"Datos: \n ||Nombre: {persona['Nombre']}\n ||Apellidos:  {persona['Apellidos']}\n ||Edad:{persona['Edad']}\n") 

   print("Muestra diccionarios dentro de diccionario y sus atributos")
   print(f"Datos: \n ||Nombre: {persona2['Datos Personales']['Nombre']}\n ||Apellidos: {persona2['Datos Personales']['Apellidos']}\n ||Edad:{persona2['Datos Personales']['Edad']}\n ||Salario: {persona2['Salarial']['Salario']}\n ||Subsidio de trasporte: {persona2['Salarial']['SubTransporte']}\n ||Subsidio de Alimentacion: {persona2['Salarial']['SubAlimentacion']}\n")

   print("Muestra Valores especificos del diccionario en este caso nombres y salario")
   print(f"Datos: \n ||Nombre: {persona2['Datos Personales']['Nombre']}\n ||Apellidos: {persona2['Datos Personales']['Apellidos']}\n ||Salario: {persona2['Salarial']['Salario']}\n")
   
   print("Cambia valor de un atributo especifico de un atributo del diccionario en este caso el nombre")
   persona2["Nombre"] = "Enrique"
   print(f"||Nombre: {persona2['Nombre']}\n||Apellidos: {persona2['Datos Personales']['Apellidos']}\n")

if __name__ == "__main__":
    main()