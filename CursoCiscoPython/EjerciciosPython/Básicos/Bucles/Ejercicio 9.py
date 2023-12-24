#9) Hacer un programa que imprima una tabla de multiplicar del 2 al 9 . Cada uno debe
#mostrar sus valores multiplicados del 1 al 9 inclusive
for tabla in range(2,10):
    print("TABLA DEL", tabla)
    for numero in range(1,10):
        print(tabla, "por", numero, ":", tabla*numero)