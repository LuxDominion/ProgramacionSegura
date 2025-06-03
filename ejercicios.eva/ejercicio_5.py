while True:
    entrada = input("Ingrese un número entero positivo: ")
    
    if entrada.isdigit() and int(entrada) > 0:
        numero = int(entrada)
        break
    else:
        print("Error: Debe ingresar un número entero positivo. Intente nuevamente.")

print("Cuenta regresiva desde", numero, "hasta 0:")
print(", ".join(str(i) for i in range(numero, -1, -1)))