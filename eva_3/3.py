resultados_estudiantes = [
    ['Aquiles Baeza', 4.5, 5.5, 7.0, 5.3],
    ['Wendy Sulca', 4.3, 4.5, 5.2, 5.3],
    ['Delfín Quispe', 3.9, 4.8, 5.5, 5.0],
    ['Armando Casas', 2.8, 4.0, 5.5, 6.1]
]

for estudiante in resultados_estudiantes:
    nombre = estudiante[0]             
    notas = estudiante[1:]             
    promedio = sum(notas) / len(notas)
    print(nombre, "-", notas, "- Promedio:", round(promedio,))
