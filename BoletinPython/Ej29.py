importe = float(input("Introduce el importe de la compra: "))
vip = input("¿El cliente es VIP? (si/no): ")

if vip == "si":
    descuento = importe * 0.10
elif importe > 100:
    descuento = importe * 0.05
else:
    descuento = 0

importe_final = importe - descuento

print("Importe final:", importe_final, "€")
