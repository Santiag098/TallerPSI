numero1 = int(input("Digite un numero: "))
operador = str(input("Seleccione: + | - | * | / |: "))
numero2 = int(input("Digite un numero: "))

def sumar (a,b):
    suma = a + b
    print("Suma: ")
    print(a,"+",b)
    return suma

def restar (a,b):
    resta = a - b
    print("Resta: ")
    print(a,"-",b)
    return resta

def multiplicar (a,b):
    multiplo = a * b
    print("Multiplicacion: ")
    print(a,"*",b)
    return multiplo

def dividir (a,b):
    if numero1 == 0 or numero2 == 0 :
        print ("Error...")
        dividido = "No se puede dividir entre 0"
    else:
        dividido = a / b
    print("Division: ")
    print(a,"/",b)
    return dividido


if (operador == "+"):
    print(sumar(numero1,numero2))
elif operador == "-" :
    print (restar(numero1,numero2))
elif operador == "*" :
    print (multiplicar(numero1,numero2))
else :
    print (dividir(numero1,numero2))
