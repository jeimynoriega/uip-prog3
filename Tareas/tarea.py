chance = 0

minutos = 0

while chance < 6:

    tiempo_min = int(input("Ingrese el tiempo en minutos: "))

    chance +=1

    if tiempo_min / 60:

        minutos = 60 - tiempo_min % 60

        dias = 24 - tiempo_min % 24

        horas = 8 - tiempo_min % 8
