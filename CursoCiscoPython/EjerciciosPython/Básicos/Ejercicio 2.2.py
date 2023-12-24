#2) Hacer un programa que solicite por teclado dos número y muestre la suma , la resta ,la multiplicación y la división de esos números
#en otras variables y con comprobación
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "No es posible realizar la división"

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", multiplicacion)
print("División: ", division)