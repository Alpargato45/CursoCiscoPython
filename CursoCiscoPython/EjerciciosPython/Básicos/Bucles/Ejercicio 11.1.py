#11) Hacer un programa donde se muestre el siguiente dibujo
#Elige el usuario
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

for i in range(filas):
    if i == 0 or i == (filas-1):
        print("* " * columnas)
    else:
        print("*" + " " * (columnas * 2 - 3) + "*")