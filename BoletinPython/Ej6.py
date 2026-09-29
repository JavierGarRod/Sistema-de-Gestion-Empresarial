precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad
iva = subtotal * 0.21
total = subtotal + iva

print(f"Subtotal: {subtotal:.2f} €")
print(f"IVA: {iva:.2f} €")
print(f"Total: {total:.2f} €")
