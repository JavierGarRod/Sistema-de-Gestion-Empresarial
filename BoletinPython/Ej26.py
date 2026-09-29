clientes_tienda_a = {"Ana", "Luis", "Marta", "Carlos"}
clientes_tienda_b = {"Marta", "Carlos", "Lucía"}

# 1. Todos los clientes
todos = clientes_tienda_a | clientes_tienda_b

# 2. Clientes que están en ambas tiendas
comunes = clientes_tienda_a & clientes_tienda_b

# 3. Clientes únicamente de la tienda A
solo_a = clientes_tienda_a - clientes_tienda_b

print("Todos los clientes:", todos)
print("Clientes en ambas tiendas:", comunes)
print("Clientes únicamente de A:", solo_a)
