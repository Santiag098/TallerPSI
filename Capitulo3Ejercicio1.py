numero = 1
suma = 0
contador = 0
while numero != 0:
    numero = int(input("Digite un numero: "))
    suma += numero
    contador +=1
    if numero == 0:
        print("Error, el primer numero no puede ser cero")
        break;
total = suma / (contador-1)
print ("El promedio es: ",total)
