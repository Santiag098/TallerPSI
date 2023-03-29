def calculoMedia(numero1,numero2,numero3):
    operacion = numero1+numero2+numero3 - min(numero1,numero2,numero3) - max(numero1,numero2,numero3)
    return operacion

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el tercer numero: "))

print("La media de",numero1,",",numero2,"y",numero3,"es: ",calculoMedia(numero1,numero2,numero3))