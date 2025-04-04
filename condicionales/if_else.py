# condicionales
print("ingrese su edad:")
edad= input()
edad_int = int(edad)

if edad_int >= 18:
    print("Ud. es mayor de edad")
else:
    print("Ud. es Menor de edad")

# AB: El grupo de mayor ingreso, con un promedio de $4.386.000
# C1a: Clase media acomodada, con un promedio de $2.070.000
# C1b: clase media emergente, con un promedio de $1.374.000
# C2: Clase media tipica, con un promedio de 810.000
# C3: Clase media baja 
# D: Vulnerables, con un promedio de $562.000
# E: pobres, con un promedio de $324.000

sueldo = input("Ingrese su sueldo: ")

while (sueldo.isdigit()==False):
    sueldo = input("Vuelva a ingresar su sueldo: ")

sueldo = int(sueldo)

if sueldo >= 6452000:
    print("Tu grupo socioeconomico es AB (Grupo de mayor ingreso).")
elif sueldo >= 27390000:
    print("Tu grupo socioeconomico es C1a (Grupo de clase media acomodada).")
elif sueldo >= 1986000:
    print("Tu grupo socioeconomico es C1b (Grupo de clase media emergente).")
elif sueldo >= 1360000:
    print("Tu grupo socioeconomico es C2 (Grupo de clase media tipica).")
elif sueldo >= 899000:
    print("Tu grupo socioeconomico es C3 (Grupo de clase media baja).")
elif sueldo >= 562000:
    print("Tu grupo socioeconomico es D (Grupo de clase vulnerable).")
elif sueldo >= 324000 or sueldo < 324000:
    print("Tu grupo socioeconomico es E (Grupo de clase pobre).")