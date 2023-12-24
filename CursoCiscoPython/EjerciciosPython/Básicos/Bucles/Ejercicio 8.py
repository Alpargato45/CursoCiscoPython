#8) Hacer un programa que cuente del 1 al 100 inclusive e imprima los números que son divisibles por 2 y por 5.
for numero in range(1, 101):
    if((numero % 2 == 0) and (numero % 5 == 0)):
        print(numero)