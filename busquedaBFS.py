from queue import PriorityQueue

grafo = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3},
    'C': {'D': 1},
    'D': {'E': 5},
    'E': {}
}

def busquedaBFS(grafo, nodoInicial):
    # Inicializar la distanciaancia de todos los nodos a infinito
    distancia = {node: float('inf') for node in grafo}
    # Establecer la distanciaancia del nodo inicial a 0
    distancia[nodoInicial] = 0
    
    # Crear una cola de prioridad para almacenar los nodos a visitar
    colaNodosAVisitar = PriorityQueue()
    colaNodosAVisitar.put((0, nodoInicial))  # Tupla de (distanciaancia, nodo)
    
    # Realizar BFS
    while not colaNodosAVisitar.empty():
        distanciaAlNodo, nodoActual = colaNodosAVisitar.get()
        # Verificar si se encontró una distanciaancia más corta a este nodo
        if distanciaAlNodo > distancia[nodoActual]:
            continue
        # Explorar los vecinos del nodo actual
        for nodoVecino, peso in grafo[nodoActual].items():
            # Calcular la distanciaancia al vecino a través del nodo actual
            nuevaDistancia = distancia[nodoActual] + peso
            # Actualizar la distanciaancia si es más corta que la actual
            if nuevaDistancia < distancia[nodoVecino]:
                distancia[nodoVecino] = nuevaDistancia
                colaNodosAVisitar.put((nuevaDistancia, nodoVecino))
    
    # Devolver el diccionario de distanciaancias
    return distancia

nodoInicial = 'A'
distancia = busquedaBFS(grafo, nodoInicial)
print(distancia)
