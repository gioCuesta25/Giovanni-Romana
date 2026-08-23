suma = 0
contador = 1

while contador <= 5:
    calificacion = float(input(f"Ingresa la calificación {contador}: "))
    suma += calificacion
    contador += 1

promedio = suma / 5

print("Promedio final:", promedio)

if promedio >= 60:
    print("Aprobado")
elif promedio >= 40:
    print("En recuperación")
else:
    print("Reprobado")
