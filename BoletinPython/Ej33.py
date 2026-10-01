password_correcta = "python123"

password = input("Introduce la contraseña: ")

while password != password_correcta:
    password = input("Contraseña incorrecta. Inténtalo de nuevo: ")

print("Acceso permitido")
