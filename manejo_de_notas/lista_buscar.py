lista_asignaturas = ['Biologia','Quimica','Fisica']
#Comandorted muestra la lista en orden alfabetico

def mostrar_listado_asignaturas():
   print()
   print('Lista de Asignaturas')
   print('====================')
   contador = 0
   for asignatura in sorted (lista_asignaturas):
    contador += 1 
    print(f'{contador}.-{asignatura}')

mostrar_listado_asignaturas()

# frase = input('Ingrese una frase: ')
# busqueda = input('Ingrese texto a buscar: ')
# if busqueda in frase:
#     print(f'{busqueda} Encontrada!')
# else:
#     print(f'{busqueda} No encontrada!')

def buscar_asignatura():
  busqueda = input('Ingrese asignatura a buscar. ')
  for asignatura in lista_asignaturas:
    if busqueda.lower() in asignatura.lower():
      return asignatura

def agregar_asignatura():
   mostrar_listado_asignaturas
   nueva_asignatura = input('Ingrese Nueva Asignatura: ')
   lista_asignaturas.append(nueva_asignatura.title()) 
   mostrar_listado_asignaturas()

def actualizar_asignatura():
  mostrar_listado_asignaturas()
  busqueda = input('Ingrese asignatura a buscar: ')
  for i in range(len(lista_asignaturas)):
    if busqueda.lower() in lista_asignaturas[i].lower():
      nuevo_dato = input(f'Ingrese nuevo nombre para asignatura {lista_asignaturas[i]} ')
      lista_asignaturas[i] = nuevo_dato
    mostrar_listado_asignaturas()

actualizar_asignatura()