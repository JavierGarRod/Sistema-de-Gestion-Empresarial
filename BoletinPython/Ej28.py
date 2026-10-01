stock = int(input("Introduce el stock disponible: "))
cantidad = int(input("¿Cuántas unidades quieres comprar? "))

if cantidad <= stock:
    print("Venta posible")
else:
    print("Stock insuficiente")
