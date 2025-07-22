listado_asignaturas = '''
    SELECT id,codigo_asignatura,nombre_asignatura,descripcion_asignatura
    FROM asignaturas
    WHERE habilitado = 1
'''