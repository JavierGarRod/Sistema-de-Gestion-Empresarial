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

    def valor_stock(self):
        return self.precio * self.existencias


# Crear producto
producto1 = Producto("P001", "Monitor", 200, 5)

print("Producto:", producto1.nombre)
print("Precio:", producto1.precio, "€")
print("Stock:", producto1.existencias)

print("Valor del stock:", producto1.valor_stock(), "€")
