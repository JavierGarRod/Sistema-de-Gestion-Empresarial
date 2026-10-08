def calcular_iva(precio):
    return precio * 0.21


def calcular_descuento(precio, descuento):
    return precio * descuento / 100


def calcular_total(precio, descuento):
    precio_descuento = precio - calcular_descuento(precio, descuento)
    iva = calcular_iva(precio_descuento)

    return precio_descuento + iva