precios = [10, 250, 30, 150, 80, 300]

cantidad = 0

for precio in precios:
    if precio > 100:
        print(precio, "€")
        cantidad = cantidad + 1

print("Cantidad de productos:", cantidad)
