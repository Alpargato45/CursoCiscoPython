#15)Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es
#múltiplo del otro. Crea una función EsMultiplo que reciba
#los dos números, y devuelve si el primero es múltiplo del segundo.

def EsMultiplo(n1,n2):
    if(n2%n1==0):
        print(n1, "es múltiplo de",n2)
    else:
        print(n1, "no es múltiplo de",n2)

numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))

EsMultiplo(numero1,numero2)
EsMultiplo(numero2,numero1)