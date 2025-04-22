

def conversor(temperatura, inicio, fin):
    resultado = ""
    # Conversion de datos
    if inicio == "K":
        if fin == "C":
            resultado = temperatura - 273.15
        elif fin == "F":
            resultado = (temperatura - 273.15) * 9/5 + 32
        else:
            print("Escala Final Erronea")
    elif inicio == "C":
        if fin == "K":
            resultado = temperatura + 273.15
        elif fin == "F":
            resultado = temperatura * 9/5 + 32
        else:
            print("Escala Final Erronea")
    elif inicio == "F":
        if fin == "K":
            resultado = (temperatura - 32) * 5/9 + 273.15
        elif fin == "C":
            resultado = (temperatura - 32) * 5/9
        else:
            print("Escala Final Erronea")
    else:
        print("Escala de Inicio Erronea")

    print(resultado)          

temp = float(input("Ingrese La Temperatura Con la respectiva Unidad: "))
escala_inicial = input("Indique escala inicial: C, F o K: ")
escala_final = input("Indique escala final: C, F o K: ")

conversor(temp, escala_inicial, escala_final)