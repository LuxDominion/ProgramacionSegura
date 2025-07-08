from data.asignaturas import asignaturas
from data.crear_data import crear_data
from data.conexion import ejecutar_consulta
from data.scripts.scripts_asignaturas import listado_asignaturas
from prettytable import PrettyTable
from auxiliares.mensajes import sin_datos

def cargar_listado_asignaturas():
    lista_asignaturas = ejecutar_consulta(listado_asignaturas)
    if listado_asignaturas != None:
        return lista_asignaturas

def mostrar_listado_asignaturas():
    print()
    print('Listado de Asignaturas')
    tabla_asignaturas = PrettyTable()
    tabla_asignaturas.field_names = ['Id','Código Asignatura','Nombre Asignatura']
    lista = cargar_listado_asignaturas()
    if lista != None:
        for asignatura in lista:
            tabla_asignaturas.add_row(asignatura) # type: ignore
        print(tabla_asignaturas)
    else:
        print(sin_datos)

# READ
def buscar_asignatura():
    busqueda = input('Ingrese asignatura a buscar: ')
    for asignatura in asignaturas:
        if busqueda.lower() in asignatura.lower():
            return asignatura

def indice_asignatura(busqueda):
    for i in range(len(asignaturas)):
        if busqueda.lower() in asignaturas[i].lower():
            return i

# # CREATE
# def agregar_asignatura():
#     mostrar_listado_asignaturas()
#     nueva_asignatura = input('Ingrese nueva asignatura: ')
#     asignaturas.append(nueva_asignatura.title())

#     crear_data('asignaturas.py','asignaturas',asignaturas)

#     mostrar_listado_asignaturas()

# # UPDATE  
# def actualizar_asignatura():
#     mostrar_listado_asignaturas()
#     busqueda = input('Ingrese asignatura a buscar: ')
#     indice = indice_asignatura(busqueda)
#     # nuevo_dato = input(f'Ingrese nuevo nombre para asignatura {asignaturas[indice]}: ')
#     # asignaturas[indice] = nuevo_dato

#     crear_data('asignaturas.py','asignaturas',asignaturas)
#     mostrar_listado_asignaturas()