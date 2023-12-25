#21)Crear una función recursiva que permita calcular el factorial de un número. Realiza un
#programa principal donde se lea un entero y se muestre el resultado del factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular el factorial: "))
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
