# Colecciones de datos 

# LISTAS, colecciones ordenadas de datos o elementos  mutables
lista = ["6xenty", 18, True]
print(lista)
print(type(lista))

print([34,36,37])
print(type([34,36,37]))

print(lista[1])
lista[1] = 24
print(lista)

# DICCIONARIOS, colecciones ordenadas de pares datos o elementos mutables 
diccionario = {'nombre':'6xenty','edad':18,'es_profesor':True}
print(diccionario)
print(type(diccionario))
print(diccionario['edad']) 
diccionario['edad'] = 69
print(diccionario)

# CONJUNTOS, colección desordenada de elementos 
conjunto = {"6xenty", 18, True}
print(conjunto)
print(type(conjunto))

conjunto.add(65)
print(conjunto)
conjunto.pop()
print(conjunto)
conjunto.pop()
print(conjunto)

# TUPLA , colección INMUTABLE de elementos
tupla = ("6xenty", 18, True)
print(tupla)
print(type(tupla))

#tupla[2]=32 
print(tupla[2])