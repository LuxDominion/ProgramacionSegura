# Ejercicio 1
# Definir función saludar 
def saludar(nombre):
    print(f"Buen día estimado(a) {nombre}")

nombre = input("Ingresa su nombre: ")
# Ejecutar función saludar
saludar(nombre)

# Ejercicio 2
# Definir función sumar
def suma(a,b):
    resultado = a + b
    print(f"El resultado de sumar {a} + {b} = {resultado}")

numero_1 = int(input("Ingrese su primer número:"))
numero_2 = int(input("Ingrese su segundo número:"))
# Ejecutar función suma
suma(numero_1,numero_2)

# Ejercicio 3

num_1 = int(input("Ingrese su primer número: "))
num_2 = int(input("Ingrese su segundo número: "))
operacion =  input("Ingrese su operación: ")

# Definir función calculadora
def calculadora(a,b,op):
    resultado = 0

    if op == "+":
        resultado = a + b
    elif op == "*":
        resultado = a * b
    elif op == "-":
        resultado = a - b
    elif op == "/":
        if num_2 == 0:
            print("Operación indefinida...")
            return
        else:
            resultado = a / b
    print(f"El resultado de {a}{op}{b} = {resultado}")

# Ejecución función calculadora 
calculadora(num_1, num_2, operacion)

#Ejercicio4
#Definicion de variables
lado = float(input("Ingrese su Medida de su Lado"))
print(f"El Area de su cuadrado de lado {a}= {a*a}")

area_cuadrado(lado)