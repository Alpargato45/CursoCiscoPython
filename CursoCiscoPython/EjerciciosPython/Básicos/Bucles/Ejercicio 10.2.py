#10) Hacer un programa que muestre el siguiente dibujo.
#guardar en variables que usuario elige
filas = int(input("Numero de filas"))
columnas = int(input("Numero de columnas"))
for i in range(filas):
    for j in range(columnas):
        print("* ", end="")
    print()