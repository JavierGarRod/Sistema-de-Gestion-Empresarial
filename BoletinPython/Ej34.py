opcion = 0

while opcion != 3:
    print("1. Mostrar mensaje")
    print("2. Mostrar fecha ficticia")
    print("3. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Hola, bienvenido al programa")
    elif opcion == 2:
        print("Fecha: 01/01/2025")
    elif opcion == 3:
        print("Programa terminado")
    else:
        print("Opción no válida")
