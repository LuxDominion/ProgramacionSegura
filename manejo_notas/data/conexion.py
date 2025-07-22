import mysql.connector
from mysql.connector import Error
from auxiliares.data_conexion import servidor,puerto,usuario,base_datos,contrasena

def generar_conexion():
    try:
        conexion = mysql.connector.connect(
            host=servidor,
            port=puerto,
            user=usuario,
            database=base_datos,
            password=contrasena
        )
        if conexion.is_connected():
            return conexion
    except mysql.connector.Error as error_conexion:
        print(f'Error de conexión: {error_conexion}')
    else:
        conexion.close()

def leer_datos(consulta):
    conexion = generar_conexion()
    if conexion and conexion.is_connected():
        cursor = conexion.cursor()
        if cursor != None:
            try:
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                cursor.close()
                return resultado
            except Error as error_ejecucion:
                print(f'Ha ocurrido un error: {error_ejecucion.msg}')
            finally:
                cursor.close()
                conexion.close()
        else:
            print('Ha ocurrido un error de comunicación')

def insertar_datos(consulta, datos):
    conexion = generar_conexion()
    if conexion and conexion.is_connected():
        cursor = conexion.cursor()
        if cursor != None:
            try:
                cursor.execute(consulta, datos)
                conexion.commit()
                id = cursor.lastrowid
            except Error as error_ejecucion:
                print(f'Ha ocurrido un error: {error_ejecucion.msg}')
            finally:
                cursor.close()
                conexion.close()
        else:
            print('Ha ocurrido un error de comunicación')
        
# cursor.execute('SELECT numero_opcion,opcion_menu FROM opciones_menu')
# resultado = cursor.fetchall()
# print(resultado)

# COSAS
# conexion = mysql.connector.connect(
#     host = servidor,
#     port = puerto,
#     user = usuario,
#     database = base_datos,
#     password = contrasena
# )

# cursor = conexion.cursor()

# def ejecutar_consulta(consulta):
#     cursor.execute(consulta)
#     resultado = cursor.fetchall()
#     return resultado
