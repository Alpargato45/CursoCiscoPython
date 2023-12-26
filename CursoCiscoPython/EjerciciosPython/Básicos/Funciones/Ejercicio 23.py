#23 Escribir dos funciones que permitan calcular: La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#La cantidad de horas, minutos y segundos de un tiempo dado en segundos. Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a
#segundos, convertir a horas,minutos y segundos o salir del programa.

def PasarASegundos(h,min,seg):
    segFinales = (h*3600) + (min*60) + seg
    return segFinales

def PasarAHoras(seg):

    min = seg // 60
    hora = min // 60
    seg = seg % 60
    min = min%60
    print(hora, "Horas,", min, "Minutos y", seg, "Segundos")

menu = 0
while(menu != 3):
    menu = 0
    print("1. Pasar de Segundos a Horas y Minutos")
    print("2. Pasar de Horas a Segundos")
    print("3. Salir")
    while(menu <1 or menu > 3):
        menu = int(input("Elige tu opción: "))
    if(menu == 1):
        h = int(input("Horas: "))
        min = int(input("Minutos: "))
        seg = int(input("Segundos: "))
        print(h, "Horas,", min, "Minutos y ", seg, "Segundos son:", PasarASegundos(h,min,seg), "Segundos")
    elif(menu == 2):
        seg = int(input("Segundos: "))
        seg = abs(seg)
        PasarAHoras(seg)