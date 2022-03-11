import math

def Ecuacion(a,b,c):
    
    Calcular = ((b**2)-4*a*c)
    return Calcular
           

def main():
    print("Resolveremos la operacion\n(-{b}+√{b}^2-4({a})*({c})))/2a")
    print("(-{b}-√{b}^2-4({a})*({c})))/2a\n")
    b = int(input("Digite el valor de b --> "))
    a = int(input("Digite el valor de a --> "))
    c = int(input("Digite el valor de c --> "))
    Calcular=Ecuacion(a,b,c)
    R=0
    R2=0
    if Calcular==0:
        print(f"La respuesta de la operacion (-{b}+√{b}^2-4({a})*({c}))/2 es 0")
    elif Calcular<0:
        print(f"La operacion (-{b}+√{b}^2-4({a})*({c}))/2 es indeterminada")
    else: 
        R=(-b+math.sqrt(b**2-(4*a*c)))/(2*a)
        R2=(-b-math.sqrt(b**2-(4*a*c)))/(2*a)
        print(f"El resultado de la ecuacion (-b+√b^2-4(a)*(c))/2a es ==> {R:.2f}")
        print(f"El resultado de la ecuacion (-b-√b^2-4(a)*(c))/2a es ==> {R2:.2f}")
    

if __name__ == "__main__":
    main()
