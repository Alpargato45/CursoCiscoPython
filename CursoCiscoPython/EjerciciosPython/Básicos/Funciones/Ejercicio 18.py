#18)Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
#Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def CalcularMaxMin(lista):
    if not lista:
        return None, None
    min = lista[0]
    max = lista[0]
    for num in lista:
        if num > max:
            max = num
        elif num < min:
            min = num
    return max,min

numeros = []

seguir = True
while(seguir == True):
    num = input("Pon un número: ")
    numeros.append(num)
    respuesta = input("Pulsa N para parar, cualquier otro carácter para seguir:").upper()
    if (respuesta == "N"):
        seguir = False
    else:
        seguir = True
maximo,minimo = CalcularMaxMin(numeros)
print("Número máximo:", maximo)
print("Número mínimo:", minimo)