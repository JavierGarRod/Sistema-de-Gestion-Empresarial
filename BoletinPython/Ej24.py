clientes = [
    {
        "nombre": "Ana",
        "email": "ana@email.com",
        "ciudad": "Sevilla"
    },
    {
        "nombre": "Luis",
        "email": "luis@email.com",
        "ciudad": "Córdoba"
    },
    {
        "nombre": "Marta",
        "email": "marta@email.com",
        "ciudad": "Sevilla"
    },
    {
        "nombre": "Carlos",
        "email": "carlos@email.com",
        "ciudad": "Sevilla"
    }
]

ciudad_buscada = input("Ciudad: ")

contador = 0

for cliente in clientes:
    if cliente["ciudad"] == ciudad_buscada:
        contador += 1

print("Número de clientes de", ciudad_buscada + ":", contador)
