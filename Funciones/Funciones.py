#definir funcion saludar
def saludar(nombre):
    print(f"Buenos Dias Estimado(a) {nombre}")
    
nombre = input("Ingrese su nombre:")
saludar(nombre) 

#definir funcion sumar
def suma(a,b):
    resultado = a+b
    print(f"El Resultado de sumar {a} + {b} = {resultado}")

numero_1 = int(input("ingrese su Primer Numero"))
numero_2 = int(input("ingrese su segundo numero"))

#ejecutar funcion suma
suma(numero_1,numero_2)





# Ejercicio 

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
    else:
        if num_2 == 0:
            print("Operación indefinida...")
            return
        else:
            resultado = a / b
    print(f"El resultado de {a}{op}{b} = {resultado}")

# Ejecución función calculadora 
calculadora(num_1, num_2, operacion)
