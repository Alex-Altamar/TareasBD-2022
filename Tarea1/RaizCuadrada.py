# Ejercicio Raiz Cuadrada
import math

def raiz_cuadrada(numero):
    if numero < 0 :
       print("indeterminado")
    elif numero == 0 :
        return 0
    else:
        raiz = math.sqrt(numero)
        return raiz


def main():

    numero = int(input("Calcular la raiz cuadrada de ==>  "))

    raiz = raiz_cuadrada(numero)

    print("la raiz cuadrada de este numero es: ",(raiz))

if __name__ == "__main__":
    main()