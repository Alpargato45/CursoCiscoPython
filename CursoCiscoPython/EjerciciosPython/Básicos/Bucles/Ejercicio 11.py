#11) Hacer un programa donde se muestre el siguiente dibujo
filas = 5
columnas = 5

for i in range(filas):
    if i == 0 or i == (filas-1):
        print("* " * columnas)
    else:
        print("*" + " " * (columnas * 2 - 3) + "*")