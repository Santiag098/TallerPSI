def ordinal(numero):
    if numero == 1:
        return "Primero"
    elif numero == 2:
        return "Segundo"
    elif numero == 3:
        return "Tercero"
    elif numero == 4:
        return "Cuarto"
    elif numero == 5:
        return "Quinto"
    elif numero == 6:
        return "Sexto"
    elif numero == 7:
        return "Septimo"
    elif numero == 8:
        return "Octavo"
    elif numero == 9:
        return "Noveno"
    elif numero == 10:
        return "Decimo"
    elif numero == 11:
        return "Decimo Primero"
    elif numero == 12:
        return "Decimo Segundo"
    else:
        return ""

for i in range(1,13):
    print(i,ordinal(i))