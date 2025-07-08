def area_circulo(radio):
    pi = 3.1416
    area = pi * radio * radio
    return area

def volumen_cilindro(radio, altura):
    volumen = area_circulo(radio) * altura
    return volumen

radio = float(input("Ingresa el radio del círculo: "))
altura = float(input("Ingresa la altura del cilindro: "))

print("Área del círculo:", area_circulo(radio))
print("Volumen del cilindro:", volumen_cilindro(radio, altura))
