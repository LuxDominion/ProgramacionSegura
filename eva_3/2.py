entrada = input("Escribe varios numeros separados por coma porfavor estimado baley(ej: 5,6,7): ")

numeros = entrada.split(",")
lista = []
for n in numeros:
    lista.append(float(n))

suma = 0
for num in lista:
    suma += num
media = suma / len(lista)

suma_dif = 0
for num in lista:
    diferencia = num - media
    suma_dif += diferencia * diferencia
varianza = suma_dif / len(lista)

desviacion = varianza ** 0.5

# Paso 6: Mostrar los resultados
print("Media:", round(media, 2))
print("Varianza:", round(varianza, 2))
print("Desviación típica:", round(desviacion, 2))
