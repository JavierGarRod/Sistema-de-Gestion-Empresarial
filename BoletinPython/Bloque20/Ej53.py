class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class Cliente(Persona):
    def __init__(self, nombre, email, numero_cliente):
        super().__init__(nombre, email)
        self.numero_cliente = numero_cliente


class ClienteVIP(Cliente):
    def __init__(self, nombre, email, numero_cliente, descuento):
        super().__init__(nombre, email, numero_cliente)
        self.descuento = descuento

    def calcular_precio(self, precio):
        return precio - (precio * self.descuento / 100)


cliente = ClienteVIP("Ana", "ana@gmail.com", "C001", 20)

print("Nombre:", cliente.nombre)
print("Email:", cliente.email)
print("Número de cliente:", cliente.numero_cliente)
print("Descuento:", cliente.descuento, "%")

precio = 100
print("Precio final:", cliente.calcular_precio(precio), "€")