asignaturas = ["Matematicas", "Fisica"]
notas = []
for asignatura in asignaturas:
    nota = input("que nota has sacado en " + asignatura + "?")
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + "has sacado" + notas[i])