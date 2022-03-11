#********************************
#*        MANEJO DE LISTAS      *
#********************************

from api.library import *



print("-----------------------------------------------------------------")
print("Elimina elemento especifico de la lista en este caso estudiante")
ListaConElementos.remove("Estudiante")
print(ListaConElementos)

print("-----------------------------------------------------------------")
print("Elimina elemento en posicion especifica de la lista en este caso 2000000")
del ListaConElementos[1]
print(ListaConElementos)
print("-----------------------------------------------------------------")
print("Adiciona en la lista en este caso Sede Riohacha")
ListaConElementos.append("Sede Riohacha")
print(ListaConElementos)
print("-----------------------------------------------------------------")
print("Adiciona arreglo dentro del arreglo en este caso agregamos areglo de 2 elementos [Derecho, Doris Altamar")
ListaConElementos.append(["Derecho", "Doris Altamar"])
print(ListaConElementos)
print("-----------------------------------------------------------------")
print("Adiciona arreglo dentro del arreglo en una posicion especifica, en este caso agregamos areglo de 2 elementos [BD_Avanzada", "Python] en la posicion 2")

ListaConElementos.insert(2,["BD_Avanzada", "Python"])
print(ListaConElementos)
print("-----------------------------------------------------------------")
print("Recorre el arreglo y lo muestra\n")
j=0
while j < len(ListaConElementos):
    print(ListaConElementos[j])
    j+=1
print("-----------------------------------------------------------------")
print("Muestra elementos pares del arreglo")
print(ListaConElementos[1:8:2])
print("-----------------------------------------------------------------")
print("Muestra elementos impares del arreglo")
print(ListaConElementos[0:7:2])
print("-----------------------------------------------------------------")
print("Muestra elementos en la posicion indicada del arreglo")
print(ListaConElementos[2])
print("-----------------------------------------------------------------")
print("Muestra elementos de un arreglo dentro de otro arreglo")
print(ListaConElementos[5][1])
print("-----------------------------------------------------------------")
print("Muestra el ultimo elemento de un arreglo ")
print(ListaConElementos[-1])
print("-----------------------------------------------------------------")
print("Muestra el ultimo elemento de un arreglo dentro de otro arreglo en la ubicacion seleccionada")
print(ListaConElementos[-1][1])


def main():
    listas()


if __name__ == "__main__":
    main()