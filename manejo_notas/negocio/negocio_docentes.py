from data.conexion import leer_datos, insertar_datos
from prettytable import PrettyTable


def mostrar_listado_docentes():
    print('\nListado de Docentes')
    consulta = '''
        SELECT id, rut_docente, nombre_docente, email_docente FROM docentes WHERE habilitado=1 ORDER BY id
    '''
    resultado = leer_datos(consulta)
    tabla_docentes = PrettyTable()
    tabla_docentes.field_names = ['Id', 'RUT', 'Nombre', 'Email']
    if resultado:
        for docente in resultado:
            tabla_docentes.add_row(docente)
        print(tabla_docentes)
    else:
        print('No hay docentes registrados.')


# CREATE
def agregar_docente():
    rut = input('Ingrese RUT del docente: ').strip()
    nombre = input('Ingrese nombre del docente: ').strip()
    email = input('Ingrese email del docente: ').strip()
    consulta = '''
        INSERT INTO docentes (rut_docente, nombre_docente, email_docente, habilitado) VALUES (%s, %s, %s, 1)
    '''
    valores = (rut, nombre, email)
    if rut and nombre:
        insertar_datos(consulta, valores)
        print(f'Docente "{nombre}" agregado correctamente.')
    else:
        print('Datos insuficientes.')
    mostrar_listado_docentes()

# UPDATE
def editar_docente():
    mostrar_listado_docentes()
    try:
        id_docente = int(input('Ingrese el ID del docente a editar: '))
    except ValueError:
        print('ID inválido.') # pipe
        return
    nuevo_rut = input('Ingrese el nuevo RUT del docente: ').strip()
    nuevo_nombre = input('Ingrese el nuevo nombre del docente: ').strip()
    nuevo_email = input('Ingrese el nuevo email del docente: ').strip()
    consulta = '''
        UPDATE docentes SET rut_docente=%s, nombre_docente=%s, email_docente=%s WHERE id=%s
    '''
    valores = (nuevo_rut, nuevo_nombre, nuevo_email, id_docente)
    if nuevo_rut and nuevo_nombre:
        insertar_datos(consulta, valores)
        print('Docente editado correctamente.')
    else:
        print('Datos insuficientes para editar.')
    mostrar_listado_docentes()

# DELETE
def eliminar_docente():
    mostrar_listado_docentes()
    try:
        id_docente = int(input('Ingrese el ID del docente a eliminar: '))
    except ValueError:
        print('ID inválido.')
        return
    consulta = '''
        DELETE FROM docentes WHERE id=%s
    '''
    valores = (id_docente,)
    insertar_datos(consulta, valores)
    print('Docente eliminado correctamente.')
    mostrar_listado_docentes()