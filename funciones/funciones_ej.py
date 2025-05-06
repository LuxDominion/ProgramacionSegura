def suma(a,b):
    result = a+b
    print(f"el resultado de la suma es: {result}")

def resta(a,b):
    result = a-b
    print(f"el resultado de la resta es: {result}")

def mult(a,b):
    result = a*b
    print(f"el resultado de la multiplicacion es: {result}")

def divi(a,b):
    result = a/b
    print(f"el resultado de la division es: {result}")

print("1) Suma\n2) Resta\n3) Multiplicacion\n4) Division")

select = input("Ingrese una opcion: ")
a = ""
b = ""

cont = False

while cont == False:
    if select.isdigit() == False:
        select = input("Ingrese una opcion: ")
    else:
        select = int(select)
        if select == 1 or select == 2 or select == 3 or select == 4:
            cont = True
        else:
            select = ""

while a.isdigit() == False:
    a = input("Ingrese el primer numero: ")

while b.isdigit() == False:
    b = input("Ingrese el segundo numero: ")

a = int(a)
b = int(b)

if select == 1:
    suma(a,b)
elif select == 2:
    resta(a,b)
elif select == 3:
    mult(a,b)
elif select == 4:
    divi(a,b)