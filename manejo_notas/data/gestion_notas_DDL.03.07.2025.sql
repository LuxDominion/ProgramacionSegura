USE gestion_notas;

CREATE TABLE IF NOT EXISTS docentes(
    id INT NOT NULL AUTO_INCREMENT,
    rut_docente VARCHAR(12) NOT NULL UNIQUE,
    nombre_docente VARCHAR(250) NOT NULL,
    email_docente VARCHAR(250) NULL,

    CONSTRAINT pk_docente PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS asignaturas(
    id INT NOT NULL AUTO_INCREMENT,
    codigo_asignatura VARCHAR(12) NOT NULL,
    nombre_asignatura VARCHAR(250) NOT NULL,
    descripcion_asignatura VARCHAR(250) NULL,

    CONSTRAINT pk_asignaturas PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS docentes_asignaturas(
    id INT NOT NULL AUTO_INCREMENT,
    id_docente INT NOT NULL,
    id_asignatura INT NOT NULL,

    CONSTRAINT pk_docentes_asignaturas PRIMARY KEY (id),
    CONSTRAINT fk_docentes FOREIGN KEY (id_docente) REFERENCES docentes(id),
    CONSTRAINT fk_asignaturas FOREIGN KEY (id_asignatura) REFERENCES asignaturas(id)
);

CREATE TABLE IF NOT EXISTS opciones_menu(
    id INT NOT NULL AUTO_INCREMENT,
    opcion_menu VARCHAR(250) NOT NULL,
    numero_opcion VARCHAR(2) NOT NULL,
    tipo_menu INT NOT NULL,

    CONSTRAINT pk_opciones_menu PRIMARY KEY (id)
);