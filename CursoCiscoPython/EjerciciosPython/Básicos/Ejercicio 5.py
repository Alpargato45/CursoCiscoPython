#5) Hacer un programa que solicite un color por teclado e imprima “Puede pasar “ si el
#color ingresado es verde , “Precaución “ si es amarillo , “No pasar “ si es rojo o “Color
#inválido” si es cualquier otro.
color = input("Elige un color: ")
if (color == "verde"):
    print("Puede pasar")
elif(color == "amarillo"):
    print("Precaución")
elif(color == "rojo"):
    print("No pasar")
else:
    print("Color inválido")