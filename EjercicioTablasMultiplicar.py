numeros = str(input("digite par o impar:"))
if numeros == "par":
    print("Tablas de multiplicar pares")
    for p in range (1,11):
        multiplo = 2*p
        print("2x",p," = ",multiplo)
    print("")
    for k in range (1,11):
        multiplo = 4*k
        print("4x",k," = ",multiplo)
    print("")
    for j in range (1,11):
        multiplo = 6*j
        print("6x",j," = ",multiplo)
    print("")
    for l in range (1,11):
        multiplo = 8*l
        print("8x",l," = ",multiplo)
    print("")
elif numeros == "impar": 
    print("Tablas de multiplicar impares")
    for p in range (1,11):
        multiplo = 1*p
        print("1x",p," = ",multiplo)
    print("")
    for k in range (1,11):
        multiplo = 3*k
        print("3x",k," = ",multiplo)
    print("")
    for j in range (1,11):
        multiplo = 5*j
        print("5x",j," = ",multiplo)
    print("")
    for l in range (1,11):
        multiplo = 7*l
        print("7x",l," = ",multiplo)
    print("")
    for h in range (1,11):
        multiplo = 9*h
        print("9x",h," = ",multiplo)
    print("")