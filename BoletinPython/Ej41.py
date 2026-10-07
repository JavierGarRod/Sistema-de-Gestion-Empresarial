def buscar_producto(productos, nombre):
    for producto in productos:
        if producto == nombre:
            return True
    return False


# Pruebas
productos = ["Teclado", "Monitor", "Ratón", "Impresora"]

print(buscar_producto(productos, "Monitor"))
print(buscar_producto(productos, "Ordenador"))