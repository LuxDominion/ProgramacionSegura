from data.conexion import leer_datos
from data.scripts.scripts_menu import script_menu_asignaturas,script_menu_principal
from prettytable import PrettyTable
from auxiliares.mensajes import salir,nombre_aplicacion,volver,invalido
from auxiliares.version import version_actual
from negocio.negocio_asignaturas import mostrar_listado_asignaturas,agregar_asignatura

def menu_asignaturas():
    while True:
        opciones_asignaturas = leer_datos(script_menu_asignaturas)
        tabla_menu_asignatura = PrettyTable()
        tabla_menu_asignatura.field_names = ['N°','Opción']
        if opciones_asignaturas != None:
            for opcion_asignatura in opciones_asignaturas:
                tabla_menu_asignatura.add_row(
                    opcion_asignatura)  # type: ignore
            print(tabla_menu_asignatura)
            opcion_asignatura_usuario = input(
                f'Seleccione su opción [0-{len(opciones_asignaturas)-1}] :')

            if opcion_asignatura_usuario == '1':
                mostrar_listado_asignaturas()
            elif opcion_asignatura_usuario == '2':
                agregar_asignatura()
            elif opcion_asignatura_usuario == '3':
                pass
            elif opcion_asignatura_usuario == '4':
                pass
            elif opcion_asignatura_usuario == '0':
                print(volver)
                break
            else:
                print(invalido)

def menu_principal():
    print()
    print(f'{nombre_aplicacion} v.{version_actual}')
    while True:
        opciones_menu = leer_datos(script_menu_principal)
        tabla_menu = PrettyTable()
        tabla_menu.field_names = ['N°','Opción']
        if opciones_menu != None:
            for menu in opciones_menu:
                tabla_menu.add_row(menu)  # type: ignore
            print(tabla_menu)
            opcion_usuario = input(
                f'Seleccione su opción [0-{len(opciones_menu)-1}] :')

            if opcion_usuario == '1':
                menu_asignaturas()
            elif opcion_usuario == '2':
                pass
            elif opcion_usuario == '0':
                print(salir)
                break
            else:
                print(invalido)

menu_principal()