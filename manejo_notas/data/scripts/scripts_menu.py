script_menu_principal = '''
    SELECT numero_opcion,opcion_menu 
    FROM opciones_menu
    WHERE tipo_menu = 1
    AND habilitado = 1
    ORDER BY id_opcion_menu
'''

script_menu_asignaturas = '''
    SELECT numero_opcion,opcion_menu
    FROM opciones_menu
    WHERE tipo_menu = 2
    AND habilitado = 1
    ORDER BY id_opcion_menu
'''