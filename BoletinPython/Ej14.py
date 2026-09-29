productos = [
    "Teclado",
    "Ratón",
    "Monitor",
    "Webcam",
    "Impresora"
]

producto = input("Introduce el nombre del producto: ")

if producto in productos:
    print("Producto encontrado")
else:
    print("Producto no encontrado")
