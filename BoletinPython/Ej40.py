def aplicar_descuento(precio, descuento=0):
    return precio - (precio * descuento / 100)


# Pruebas
print(aplicar_descuento(100))
print(aplicar_descuento(100, 10))
print(aplicar_descuento(250, 20))