from Ej54 import calcular_iva, calcular_descuento, calcular_total

precio = 100
descuento = 10

print("IVA:", calcular_iva(precio), "€")
print("Descuento:", calcular_descuento(precio, descuento), "€")
print("Total:", calcular_total(precio, descuento), "€")