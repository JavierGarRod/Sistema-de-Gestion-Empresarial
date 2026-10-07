def calcular_total(ventas):
    total = 0

    for venta in ventas:
        total = total + venta

    return total


# Prueba
ventas = [100, 250, 50, 75]
print(calcular_total(ventas))