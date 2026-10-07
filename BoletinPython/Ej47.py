class Cliente:
    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Correo:", self.correo)
        print("Teléfono:", self.telefono)


# Crear dos objetos
cliente1 = Cliente("Juan García", "juan@gmail.com", "600123456")
cliente2 = Cliente("Ana López", "ana@gmail.com", "611987654")

# Mostrar datos
cliente1.mostrar_datos()
print()
cliente2.mostrar_datos()
