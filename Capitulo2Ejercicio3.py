letra = str(input("Ingrese una letra: "))

if letra in ('a','e','i','o','u'):
    print("La letra",letra,"es una vocal")
elif letra == 'y':
    print("La letra",letra,"a veces es vocal, a veces es consonante")
else:
    print("La letra",letra,"es una consonante")