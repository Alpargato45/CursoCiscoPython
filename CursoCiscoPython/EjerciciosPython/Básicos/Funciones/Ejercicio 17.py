#17)Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra.
#Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

def ConvertirEspaciado(texto):
    resultado = ""
    for caracter in texto:
        resultado += caracter + " "
    return resultado.strip()

# Programa principal
texto = input("Ingrese un texto: ")
resultado = ConvertirEspaciado(texto)

print("Texto original:", texto)
print("Texto con espacio adicional:", resultado)
