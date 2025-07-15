import mysql.connector
from auxiliares.data_conexion import servidor,puerto,usuario,base_datos,contrasena

def generar_conexion():
    try:
        conexion = mysql.connector.connect(
           host = servidor,
           port = puerto,
           user = usuario,
           database = base_datos,
           password = contrasena
         )
        if conexion.is_connected():
            return conexion
    except mysql.connector.error as error_conexion:
        print(f'Error al conectar a la base de datos: {error_conexion}')
        conexion = print(f'Error al conectar a la base de datos:{error_conexion}')


def leer_datos(consulta):
    conexion = generar_conexion()
    if conexion and conexion.is_connected():
      cursor = conexion.cursor()
      if cursor != None: 
         cursor.execute(consulta)
         resultado = cursor.fetchall()
         cursor.close()
         return resultado
    else:
     print('Ha ocurrido un error de comunicacion')
    conexion.close()

def insertar_datos(consulta, datos):
    conexion = generar_conexion()
    if conexion and conexion.is_connected():
      cursor = conexion.cursor()
      if cursor != None: 
         cursor.execute(consulta, datos)
         conexion.commit()
         resultado = cursor.lastrowid()
         cursor.close()
         return resultado
    else:
     print('Ha ocurrido un error de comunicacion')
    conexion.close()

# cursor.execute('SELECT numero_opcion,opcion_menu FROM opciones_menu')
# resultado = cursor.fetchall()
# print(resultado)