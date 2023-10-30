hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

minutos_totales = hour * 60 + mins + dura
hour_final = minutos_totales // 60
mins_final = minutos_totales % 60

hour_final = hour_final % 24

print("La hora final es: ", hour_final, ":", mins_final, sep="")