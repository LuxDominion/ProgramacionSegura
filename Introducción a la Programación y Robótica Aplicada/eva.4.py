from collections import deque
import time

# DEFINICIÓN DEL ENTORNO
ALMACEN = [
    [0, 0, 0, 1, 0],
    [0, 2, 0, 1, 3],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 4]
]

INICIO = (1, 1)           # Posición inicial del robot
ZONA_ENTREGA = (4, 4)     # Posición de la zona de despacho

# FUNCIONES DE NAVEGACIÓN Y CONTROL
def buscar_paquete(almacen):
    # Escanea el almacén buscando el paquete
    for f in range(len(almacen)):
        for c in range(len(almacen[0])):
            if almacen[f][c] == 3:
                return (f, c)
    return None

def buscar_camino(origen, destino, almacen):
    # Algoritmo de búsqueda para evadir obstáculos
    filas = len(almacen)
    columnas = len(almacen[0])
    cola_rutas = deque([(origen, [origen])])
    visitados = {origen}
    
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Arriba, abajo, izquierda, derecha
    
    while cola_rutas:
        actual, camino = cola_rutas.popleft()
        
        if actual == destino:
            return camino
            
        for df, dc in movimientos:
            nueva_f, nueva_c = actual[0] + df, actual[1] + dc
            
            # Verificar límites y que no sea un obstáculo
            if (0 <= nueva_f < filas and 0 <= nueva_c < columnas and 
                almacen[nueva_f][nueva_c] != 1 and (nueva_f, nueva_c) not in visitados):
                
                visitados.add((nueva_f, nueva_c))
                cola_rutas.append(((nueva_f, nueva_c), camino + [(nueva_f, nueva_c)]))
                
    return None

def mover_robot(camino):
    for paso in camino:
        print(f"Robot moviéndose a coordenada: {paso}")
        time.sleep(1) # Simulación de tiempo de desplazamiento

# FUNCIÓN PRINCIPAL DE EJECUCIÓN LOGÍSTICA
def principal():
    global INICIO
    
    while True:
        posicion_paquete = buscar_paquete(ALMACEN)
        
        if posicion_paquete:
            print(f"\nPaquete detectado en: {posicion_paquete}")
            camino_hacia_paquete = buscar_camino(INICIO, posicion_paquete, ALMACEN)
            
            if camino_hacia_paquete:
                print("Ruta hacia el paquete calculada. Iniciando movimiento...")
                mover_robot(camino_hacia_paquete)
                
                print("Paquete recogido.")
                ALMACEN[posicion_paquete[0]][posicion_paquete[1]] = 0 # La estantería queda vacía
                
                camino_hacia_entrega = buscar_camino(posicion_paquete, ZONA_ENTREGA, ALMACEN)
                
                if camino_hacia_entrega:
                    print("Ruta hacia la zona de entrega calculada. Iniciando movimiento...")
                    mover_robot(camino_hacia_entrega)
                    print("Paquete entregado en la zona de despacho.")
                    INICIO = ZONA_ENTREGA # El robot se queda en la zona de entrega esperando
                else:
                    print("Alerta: No se pudo encontrar un camino seguro a la zona de entrega.")
                    break
            else:
                print("Alerta: El paquete está bloqueado por obstáculos, no se puede acceder.")
                break
        else:
            print("\n Operación finalizada: Todos los paquetes han sido entregados con éxito.")
            break

# Iniciar el sistema
principal()