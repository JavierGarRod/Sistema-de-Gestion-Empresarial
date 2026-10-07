class Producto:
    def __init__(self, codigo, nombre, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias

    def mostrar_info(self):
        print(f"{self.codigo} - {self.nombre} - {self.precio:.2f} € - Stock: {self.existencias}")


# Crear un producto
producto1 = Producto("P001", "Monitor", 199.99, 8)

# Mostrar información
producto1.mostrar_info()
