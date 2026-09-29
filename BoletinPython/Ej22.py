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
        "ciudad": "Madrid"
    }
]

for cliente in clientes:
    print("Nombre:", cliente["nombre"])
    print("Email:", cliente["email"])
    print("Ciudad:", cliente["ciudad"])
    print()
