edad = input("¿Cuántos años tienes? ")

es_numero = True
for caracter in edad:
    if caracter not in "0123456789":
        es_numero = False
        break

if es_numero:
    edad_num = int(edad)
    if edad_num >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
else:
    print("Error: Debes ingresar solo números enteros")