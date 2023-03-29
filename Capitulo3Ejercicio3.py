print("Celsius  Fahrenheit")

for celsius in range (0,101,10):
    fahrenheit = (celsius*1.8)+32
    print("{:>5.2f}{:>10.2f}".format(celsius,fahrenheit))
