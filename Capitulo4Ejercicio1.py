
def calculoHipotenusa(cateto1, cateto2):
    hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5
    return hipotenusa


cateto1 = float(input("Ingrese el valor del primer cateto: "))
cateto2 = float(input("Ingrese el valor del segundo cateto: "))

print("El valor de la hipotenusa es: {:.2f}".format(calculoHipotenusa(cateto1,cateto2)))