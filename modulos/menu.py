import cuadrilatero
import circuferencia

def menu_principal():
    print()
    print("Calculo de Funciones Geometricas")
    print("1: Perimetro")
    print("2: Area")
    print("3: Volumen")
    print("0: Salir")
    print()

def sub_menu():
    print()
    print("¿Para que figura Geometrica?")
    print("1: Cuadrilatero" )
    print("2: Circuferencia")
    print("0: Salir")
    print()

def programa_principal():
    while True:
    opcion = input("Seleccione su opcion (0-3):")

    if opcion == "1":
        sub_menu()opcion_sub_menu = input("Seleccione su Opcion (0-3): ")
        if opcion_sub_menu == "1"
        ancho = input("Ingrese el Ancho")
        largo = input("Ingrese su Largo")
        print(funciones.cuadrilatero.perimetro(radio))
    elif opcion_sub_menu == "0":
        return
    else:
        print("Opcion Invalida!")
    elif opcion == "2":
        pass
    elif opcion == "3": 
        pass
    elif opcion == "0":
        print("saliendo del sistema...")
        break
    else:
        print("Opcion Fallida...")

