descuento = 0.6
preciosOriginales = [4.95,9.95,14.95,19.95,24.95]

print("Precio Original  Descuento   Nuevo Precio")

for precio in preciosOriginales:
    descuentoPor = precio * descuento
    nuevoPrecio = precio - descuentoPor
    print("{:>10.2f}{:>13.2f}{:>14.2f}".format(precio, descuentoPor,nuevoPrecio))


