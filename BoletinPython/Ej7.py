precio_original = float(input("Precio original: "))
porcentaje_descuento = float(input("Descuento: "))

importe_descontado = precio_original * porcentaje_descuento / 100
precio_final = precio_original - importe_descontado

print()
print(f"Importe descontado: {importe_descontado:.2f} €")
print(f"Precio final: {precio_final:.2f} €")
