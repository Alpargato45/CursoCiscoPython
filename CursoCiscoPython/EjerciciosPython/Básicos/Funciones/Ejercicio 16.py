#16)Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
#Crear un programa principal, que utilizando la función anterior, vaya pidiendo la
#temperatura máxima y mínima de cada día y vaya mostrando la media.
#El programa pedirá el número de días que se van a introducir.

def TemperaturaMedia(tMax,tMin):
    tMed = (tMax + tMin)/2
    return tMed

dias = int(input("Número de días a calcular: "))
for i in range(dias):
    tMax = float(input("Temperatura Máxima: "))
    tMin = float(input("Temperatura Mínima: "))
    print("Temperatura media de", tMax, "y", tMin,":", TemperaturaMedia(tMax,tMin))
