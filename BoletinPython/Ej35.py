numero_ventas = 0
total_vendido = 0

venta = float(input("Introduce el importe de la venta (0 para terminar): "))

while venta != 0:
    numero_ventas = numero_ventas + 1
    total_vendido = total_vendido + venta

    venta = float(input("Introduce el importe de la venta (0 para terminar): "))

print("Número de ventas:", numero_ventas)
print("Total vendido:", total_vendido, "€")
