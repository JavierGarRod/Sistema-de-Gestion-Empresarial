productos = ["Teclado", "Ratón", "Monitor"]

# 1. Añadir Webcam
productos.append("Webcam")

# 2. Añadir Altavoces
productos.append("Altavoces")

# 3. Eliminar Ratón
productos.remove("Ratón")

# 4. Cambiar Monitor
productos[1] = "Monitor 27 pulgadas"

# 5. Mostrar la lista final
print(productos)
