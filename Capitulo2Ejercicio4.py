figura = int(input("Ingrese la cantidad de lados (3-10): "))

if figura == 3:
    print("Las figuras de",figura,"lados son TRIANGULOS")
elif figura == 4:
    print("Las figuras de",figura,"lados son CUADRILATEROS")
elif figura == 5:
    print("Las figuras de",figura,"lados son PENTAGONOS")
elif figura == 6:
    print("Las figuras de",figura,"lados son HEXAGONOS")
elif figura == 7:
    print("Las figuras de",figura,"lados son HEPTAGONOS")
elif figura == 8:
    print("Las figuras de",figura,"lados son OCTAGONOS")
elif figura == 9:
    print("Las figuras de",figura,"lados son ENEAGONOS")
elif figura == 10:
    print("Las figuras de",figura,"lados son DECAGONOS")
else:
    print("Error, no esta en el rango establecido")