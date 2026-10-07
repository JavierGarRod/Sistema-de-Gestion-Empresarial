class Producto:
    def __init__(self, codigo, nombre, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias

    def mostrar_info(self):
        print(f"{self.codigo} - {self.nombre} - {self.precio:.2f} € - Stock: {self.existencias}")

    def reponer(self, cantidad):
        self.existencias += cantidad


# Crear producto
producto1 = Producto("P001", "Monitor", 199.99, 5)

print("Stock inicial:", producto1.existencias)

producto1.reponer(3)

print("Reposición: 3")
print("Stock final:", producto1.existencias)
