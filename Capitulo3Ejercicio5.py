cadena = input("Ingrese una palabra: ")

indice1 = 0
indice2 = len(cadena)-1

palindromo = True

while indice1 < indice2:

    if cadena[indice1] != cadena[indice2]:
        palindromo = False
        break

    indice1 +=1
    indice2 -=1

if palindromo:
    print("la palabra", cadena,"es un palindromo")
else:
    print("La palabra",cadena,"no es un palindromo")
