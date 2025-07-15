import mysql.connector
from auxiliares.data_conexion import servidor,puerto,usuario,base_datos,contrasena

conexion = mysql.connector.connect(
    host = servidor,
    port = puerto,
    user = usuario,
    database = base_datos,
    password = contrasena
)

cursor = conexion.cursor()

def ejecutar_consulta(consulta):
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

def insertar_datos(consulta, datos):
    cursor.execute(consulta, datos)
    id = cursor.lastrowid
    conexion.commit()
    cursor.close()
    conexion.close()
    

# cursor.execute('SELECT numero_opcion,opcion_menu FROM opciones_menu')
# resultado = cursor.fetchall()
# print(resultado)