class Producto:
    def __init__(self, codigo, nombre, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias

    def mostrar_info(self):
        print(f"{self.codigo} - {self.nombre} - {self.precio:.2f} € - Stock: {self.existencias}")

    def reponer(self, cantidad):
        if cantidad > 0:
            self.existencias += cantidad

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
        elif cantidad > self.existencias:
            print("No hay suficiente stock.")
        else:
            self.existencias -= cantidad
            print("Venta realizada correctamente.")


# Crear producto
producto1 = Producto("P001", "Monitor", 199.99, 8)

producto1.mostrar_info()

# Vender 3 unidades
producto1.vender(3)

producto1.mostrar_info()
