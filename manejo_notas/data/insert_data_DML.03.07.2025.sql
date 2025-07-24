USE gestion_notas;

INSERT INTO docentes (rut_docente,nombre_docente,email_docente) VALUES 
('12345678-5','Aquiles Baeza','aquiles.baeza@test.test'),
('12345678-4','Wendy Sulca','wendysulca@perucito.pe');

INSERT INTO asignaturas (codigo_asignatura,nombre_asignatura) VALUES
('BIO','Biología'),
('FIS','Física General'),
('QUI','Química Inorgánica');

INSERT INTO opciones_menu (opcion_menu,numero_opcion,tipo_menu) VALUES
('Gestión Asignaturas','1',1),
('Gestión Docentes','2',1),
('Salir','0',1),
('Listado Asignaturas','1',2),
('Agregar Asignatura','2',2),
('Editar Asignaturas','3',2),
('Eliminar Asignatura','4',2),
('Salir','0',2),
('Listado Docentes','1',3),
('Agregar Docente','2',3),
('Editar Docente','3',3),
('Eliminar Docente','4',3),
('Salir','0',3);