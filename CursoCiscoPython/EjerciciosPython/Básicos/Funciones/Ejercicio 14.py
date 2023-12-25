#14)Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba
#centrado en pantalla (suponiendo una anchura de 80 columnas;
#Sin devolver valores
def EscribirCentrado(texto):
    ancho_pantalla = 80
    espacios_alrededor = (ancho_pantalla - len(texto)) // 2
    texto_centro = ' ' * espacios_alrededor + texto + ' ' * espacios_alrededor
    print(texto_centro)

EscribirCentrado("Texto Centrado")