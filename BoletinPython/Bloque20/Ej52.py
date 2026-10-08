class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class Cliente(Persona):
    def __init__(self, nombre, email, numero_cliente):
        super().__init__(nombre, email)
        self.numero_cliente = numero_cliente


cliente = Cliente("Ana", "ana@gmail.com", "C001")

print("Nombre:", cliente.nombre)
print("Email:", cliente.email)
print("Número de cliente:", cliente.numero_cliente)