costoTotal = 0

while True:
    edades = input("Ingrese su edad (Presione Enter para salir): ")

    if not edades:
        break

    edad = int(edades)

    if edad <= 2:
        costo = 0
    elif edad <= 12:
        costo = 14.00
    elif edad >= 65:
        costo = 18.00
    else:
        costo = 23.00
    
    costoTotal += costo

print("El total a pagar para el grupo es: ${:.2f}".format(costoTotal))