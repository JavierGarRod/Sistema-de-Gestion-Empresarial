clientes = []


def añadir_cliente():
    nombre = input("Nombre: ")
    correo = input("Correo electrónico: ")
    telefono = input("Teléfono: ")

    cliente = {
        "nombre": nombre,
        "correo": correo,
        "telefono": telefono
    }

    clientes.append(cliente)
    print("Cliente añadido correctamente.")


def mostrar_clientes():
    if len(clientes) == 0:
        print("No hay clientes registrados.")
    else:
        print("\n--- LISTA DE CLIENTES ---")

        for i, cliente in enumerate(clientes, start=1):
            print(f"\nCliente {i}")
            print("Nombre:", cliente["nombre"])
            print("Correo:", cliente["correo"])
            print("Teléfono:", cliente["telefono"])


def buscar_cliente():
    nombre_buscar = input("Introduce el nombre del cliente: ")

    encontrado = False

    for cliente in clientes:
        if cliente["nombre"].lower() == nombre_buscar.lower():
            print("\nCliente encontrado:")
            print("Nombre:", cliente["nombre"])
            print("Correo:", cliente["correo"])
            print("Teléfono:", cliente["telefono"])
            encontrado = True

    if not encontrado:
        print("Cliente no encontrado.")


def eliminar_cliente():
    nombre_eliminar = input("Introduce el nombre del cliente que quieres eliminar: ")

    for cliente in clientes:
        if cliente["nombre"].lower() == nombre_eliminar.lower():
            clientes.remove(cliente)
            print("Cliente eliminado correctamente.")
            return

    print("Cliente no encontrado.")


# MENÚ PRINCIPAL
while True:
    print("\n===== GESTIÓN DE CLIENTES =====")
    print("1. Añadir cliente")
    print("2. Mostrar clientes")
    print("3. Buscar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        añadir_cliente()

    elif opcion == "2":
        mostrar_clientes()

    elif opcion == "3":
        buscar_cliente()

    elif opcion == "4":
        eliminar_cliente()

    elif opcion == "5":
        print("Programa finalizado.")
        False

    else:
        print("Opción no válida.")
