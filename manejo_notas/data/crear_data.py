import os

def crear_data(nombre_archivo,nombre_lista,lista_datos):
    ruta_relativa = os.path.join('manejo_notas/data', nombre_archivo)
    ruta_absoluta = os.path.abspath(ruta_relativa)
    ruta_real = os.path.realpath(ruta_absoluta)
    archivo_final = open(ruta_real,'w+')
    archivo_final.write(f'{nombre_lista}={lista_datos}')
    archivo_final.close()