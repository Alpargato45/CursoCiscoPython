#19)Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha
#función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
def Circunferencia(r):
    pi = 3.14
    perimetro = (2*pi)*r
    area = pi * r**2
    print("Perímetro:",perimetro,"Área:",area)

radio = int(input("Radio de la circunferencia: "))
Circunferencia(radio)