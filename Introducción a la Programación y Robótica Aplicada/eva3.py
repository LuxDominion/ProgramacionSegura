
def mostrar_mis_datos():
    print("Integrantes: Cesar Aedo y Benjamin Jaque")
    print("Area: Ciberseguridad")
    print("Rut: 22.042.363-8 y 20.794.662-1")
    print("Sección: AOL-ELE-ETDI01-C6")
    print("-------------------------")
    


def existe_RUT(rut):
    registrados = ["20794662-1", "22042363-8"]
    if rut in registrados:
        return True
    else:
        return False

def contraseña_valida(clave):
    if len(clave) >= 4:
        return True
    else:
        return False


def Registrar_datos():
    print("--- Registro de Datos ---")
    nombre = input("Nombre: ")
    apellido_p = input("Apellido Paterno: ")
    apellido_m = input("Apellido Materno: ")
    
    while True:
        rut = input("Ingrese RUT: ")
        if existe_RUT(rut):
            print("RUT validado.")
            break
        else:
            print("Error: El RUT no existe.")

    while True:
        clave = input("Crear contraseña: ")
        if contraseña_valida(clave):
            print("Cuenta creada exitosamente.")
            break
        else:
            print("Error: La clave debe tener 4 o más caracteres.")


def inicio():
    
    mostrar_mis_datos()
    
    print("Bienvenidos al sistema")
    print("------------------------      ")
    
    while True:
        Registrar_datos()
        
        
        opcion = input("\n¿Desea continuar ingresando? (Si/No): ")
        if opcion.lower() != "si":
            print("Saliendo del programa...")
            break

inicio()