year = int(input("Ingrese la edad del perro(min 1): "))

if year == 1:
    print("El perro tiene 7 años caninos")
elif year == 2:
    print("El perro tiene 10,5 años caninos")
elif year > 2:
    resta = year -2
    ycanino = 4
    suma = resta * ycanino
    calculo = 10.5 + suma
    print ("El perro tiene",calculo,"años caninos")
elif year <= 0:
    print("Error, edad no valida")