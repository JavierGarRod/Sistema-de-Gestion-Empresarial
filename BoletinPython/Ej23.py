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

email_buscado = input("Introduce el email: ")

encontrado = False

for cliente in clientes:
    if cliente["email"] == email_buscado:
        print("Cliente encontrado:")
        print("Nombre:", cliente["nombre"])
        print("Ciudad:", cliente["ciudad"])
        encontrado = True
        break

if not encontrado:
    print("No existe ningún cliente con ese email.")
