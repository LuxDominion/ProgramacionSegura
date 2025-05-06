#Capitalize() hace que el texto solo la primera palabra tenga mayuscula
#Upper() Pone todas las Letras en Mayuscula
#Lower() Pone todas las Letras en Minusculas
#Title() Pone las primeras letras con Mayuscula
nombre = "lux"
apellido = "dominium"
nombre_completo = nombre + apellido

nombre_mayusculas = nombre.upper()
apellido_mayusculas = apellido.upper()

nombre_minusculas = nombre_mayusculas.lower()
apellido_minusculas = apellido_mayusculas.lower() 

nombre_titulo = nombre.title()
apellido_titulo = apellido.title()

print(nombre_completo.endswith("u"))

print(f"Hola Admirable y Maravilloso {nombre} {apellido}")
print(f"Nombre y Apellido en Mayusculas: {nombre_mayusculas} {apellido_mayusculas}")
print(f"Nombre y Apellido en Minusculas: {nombre_minusculas} {apellido_minusculas}")
print(f"Nombre y Apellido como Titulo: {nombre_titulo} {apellido_titulo}")