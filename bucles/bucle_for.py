# El ciclo FOR se ejecuta recorriendo elementos.
print()
Juegos = ["Dota 2","MK","Street Figther","Counter Strike"]
numeros = [10,20,30,40,50]
diccionario = {
   "nombre":"Lux",
   "apellido":"Dominion",
    "edad":"19",
    "estudiante":False
}

for juego in Juegos:
    print(juego)

print()
for numero in numeros:
    Resultado = numero * numero
    print(f"El Resultado de Multiplicar {numero}*{numero = }{Resultado}")

print()
print('hola' in 'hola amigos')

print()
for num in range(5):
    print(num)

print()
for num in range(5,15):
    print(num)


    for elemento in enumerate(numeros):
        indice = elemento[0]
        valor = elemento[1]
        print(f"El indice es: {indice} y el valor es: {valor}")

    for elemento in diccionario:
        print(f"La Clave del dato es: {elemento}")

    for elemento in diccionario.items():
        clave = elemento [0]
        valor = elemento [1]
        print(f"La Clave del dato es: '{clave}' y el valor es' {valor}'")

conjunto = {"Dominio de luz",30,True,"Comandos",23}

print()
for elemento in conjunto:
     if type(elemento) == str:
      print(elemento)
