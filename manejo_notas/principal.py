from data.conexion import leer_datos
from data.scripts.scripts_menu import script_menu_asignaturas,script_menu_principal
from prettytable import PrettyTable
from auxiliares.mensajes import salir,nombre_aplicacion,volver,invalido
from auxiliares.version import version_actual
from negocio.negocio_asignaturas import mostrar_listado_asignaturas,agregar_asignatura,editar_asignatura,eliminar_asignatura
from data.scripts.scripts_menu_docentes import script_menu_docentes
from negocio.negocio_docentes import mostrar_listado_docentes,agregar_docente,editar_docente,eliminar_docente


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
                editar_asignatura()
            elif opcion_asignatura_usuario == '4':
                eliminar_asignatura()
            elif opcion_asignatura_usuario == '0':
                print(volver)
                break
            else:
                print(invalido)


def menu_docentes():
    while True:
        opciones_docentes = leer_datos(script_menu_docentes)
        tabla_menu_docente = PrettyTable()
        tabla_menu_docente.field_names = ['N°','Opción'] # pipe
        if opciones_docentes != None:
            for opcion_docente in opciones_docentes:
                tabla_menu_docente.add_row(opcion_docente)  # type: ignore
            print(tabla_menu_docente)
            opcion_docente_usuario = input(
                f'Seleccione su opción [0-{len(opciones_docentes)-1}] :')

            if opcion_docente_usuario == '1':
                mostrar_listado_docentes()
            elif opcion_docente_usuario == '2':
                agregar_docente()
            elif opcion_docente_usuario == '3':
                editar_docente()
            elif opcion_docente_usuario == '4':
                eliminar_docente()
            elif opcion_docente_usuario == '0':
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
                menu_docentes()
            elif opcion_usuario == '0':
                print(salir)
                break
            else:
                print(invalido)

menu_principal()