def calculoEnvio(cantidadElementos):
    if cantidadElementos == 1:
        return 10.95
    elif cantidadElementos > 1:
        add = cantidadElementos -1
        total = 10.95 + (add*2.95)
        return total


cantidadElementos = int(input("Ingrese la cantidad de elementos comprados: "))

print("El costo total de su envio es: {:.2f}".format(calculoEnvio(cantidadElementos)))