def es_seguro(tablero, fila, columna):
    # Verificar si no hay otra reina en la misma columna
    for i in range(fila):
        if tablero[i] == columna or \
           tablero[i] - i == columna - fila or \
           tablero[i] + i == columna + fila:
            return False
    return True

def resolver_reinas(fila, tablero, soluciones):
    # Si ya tenemos todas las reinas
    if fila == len(tablero):
        soluciones.append(tablero[:])  # Guardamos una solución
        return
    
    # Intentar colocar una reina en cada columna de la fila actual
    for columna in range(len(tablero)):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna  # Colocamos la reina
            resolver_reinas(fila + 1, tablero, soluciones)  # Recursión para la siguiente fila
            tablero[fila] = -1  # Retroceso

def mostrar_soluciones(soluciones):
    for solucion in soluciones:
        for fila in solucion:
            print(' '.join('Q' if i == fila else '.' for i in range(len(solucion))))
        print()

def resolver():
    # Inicializamos el tablero de 7x7 con todas las casillas vacías
    tablero = [-1] * 7  # -1 indica que no hay reina en esa fila
    soluciones = []  # Lista para almacenar las soluciones
    resolver_reinas(0, tablero, soluciones)
    mostrar_soluciones(soluciones)

# Ejecutar el algoritmo
resolver()
