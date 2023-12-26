#22)Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:
#Se divide el número mayor entre el menor. Si la división es exacta, el divisor es el MCD.
#Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta
#forma hasta obtener una división exacta, siendo el último divisor el MCD. Crea un programa principal que lea dos números enteros y muestre el MCD.

def MCD(num1,num2):
    if(num1>num2):
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1
    resto = mayor % menor
    if (resto == 0):
        return menor
    else:
        divisor = int(menor / resto)
        return MCD(mayor,divisor)

numero1 = int(input("Primer Número: "))
numero2 = int(input("Segundo Número: "))
print("MCD de", numero1, "y", numero2, ":", MCD(numero1,numero2))