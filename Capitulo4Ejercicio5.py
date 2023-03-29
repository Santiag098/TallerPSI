def primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for i in range(3, int(numero ** 0.5)+ 1,2):
            if numero % i == 0:
                return False
        return True

numero = int(input("Ingrese un numero mayor a 1: "))

if primo(numero):
    print("El numero",numero,"es primo")
else:
    print("El numero",numero,"no es primo")
