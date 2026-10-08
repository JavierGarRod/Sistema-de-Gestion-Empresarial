class Producto:
    def __init__(self, codigo, nombre, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias

    def mostrar(self):
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Precio:", self.precio, "€")
        print("Existencias:", self.existencias)
        print("--------------------")


def añadir_producto():
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    existencias = int(input("Existencias: "))

    producto = Producto(codigo, nombre, precio, existencias)
    productos.append(producto)

    print("Producto añadido correctamente.")


def mostrar_productos():
    if len(productos) == 0:
        print("No hay productos.")
    else:
        for producto in productos:
            producto.mostrar()


def buscar_producto():
    codigo = input("Código del producto: ")

    for producto in productos:
        if producto.codigo == codigo:
            producto.mostrar()
            return

    print("Producto no encontrado.")


def vender_producto():
    codigo = input("Código del producto: ")

    for producto in productos:
        if producto.codigo == codigo:
            cantidad = int(input("Cantidad a vender: "))

            if cantidad <= producto.existencias:
                producto.existencias -= cantidad
                total = cantidad * producto.precio

                print("Venta realizada.")
                print("Total:", total, "€")
                print("Stock restante:", producto.existencias)
            else:
                print("No hay suficiente stock.")

            return

    print("Producto no encontrado.")


def reponer_producto():
    codigo = input("Código del producto: ")

    for producto in productos:
        if producto.codigo == codigo:
            cantidad = int(input("Cantidad a reponer: "))
            producto.existencias += cantidad

            print("Producto repuesto.")
            print("Existencias:", producto.existencias)
            return

    print("Producto no encontrado.")


def mostrar_valor_inventario():
    total = 0

    for producto in productos:
        total += producto.precio * producto.existencias

    print("Valor total del inventario:", total, "€")


productos = []

while True:
    print("\n========================")
    print("   GESTIÓN DE PRODUCTOS")
    print("========================")
    print("1. Añadir producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Vender producto")
    print("5. Reponer producto")
    print("6. Mostrar valor total del inventario")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        añadir_producto()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        buscar_producto()

    elif opcion == "4":
        vender_producto()

    elif opcion == "5":
        reponer_producto()

    elif opcion == "6":
        mostrar_valor_inventario()

    elif opcion == "7":
        print("Programa terminado.")
        break

    else:
        print("Opción incorrecta.")