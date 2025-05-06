import math

Numeros = [2,4,6,8,10,12]
decimal = 69.4269

print(f"El Numero Mayor de la Lista {Numeros} es {max(Numeros)}")
print(f"El Numero Menor de la lista {Numeros} es {min(Numeros)}")

print(f"Redondear decimal {decimal} = {round(decimal)}")
print(f"Redondear el Decimal {decimal} a 2 decimales = {round(decimal)}")
print(f"Truncar el decimal {decimal} = {math.trunc(decimal)}")
print(f"Valor absoluto de -45 = {math.fabs(-45)}")
print(f"Raiz cuadrada de 25= {math.sqrt(25)}")
print(f"Dumatoria de los numeros {Numeros} = {math.fsum(Numeros)}")