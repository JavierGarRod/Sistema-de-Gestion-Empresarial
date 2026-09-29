producto = input("Producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

total = precio * cantidad

print()
print("Producto:", producto)
print(f"Precio: {precio:.2f} €")
print("Cantidad:", cantidad)
print(f"Total: {total:.2f} €")
