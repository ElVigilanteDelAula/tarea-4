
grafo = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3},
    'C': {'D': 1},
    'D': {'E': 5},
    'E': {}
}

def busquedaDFS(grafo, nodoInicial):
    # Inicializar la distanciaancia de todos los nodos a infinito
    distancia = {node: float('inf') for node in grafo}
    # Establecer la distanciaancia del nodo inicial a 0
    distancia[nodoInicial] = 0
    
    # Crear una pila para almacenar los nodos a visitar
    pilaNodoAVisitar = [nodoInicial]
    
    # Realizar DFS
    while pilaNodoAVisitar:
        nodoActual = pilaNodoAVisitar.pop()
        # Explorar los vecinos del nodo actual
        for nodoVecino, peso in grafo[nodoActual].items():
            # Calcular la distanciaancia al vecino a través del nodo actual
            nuevaDistancia = distancia[nodoActual] + peso
            # Actualizar la distanciaancia si es más corta que la actual
            if nuevaDistancia < distancia[nodoVecino]:
                distancia[nodoVecino] = nuevaDistancia
                pilaNodoAVisitar.append(nodoVecino)
    
    # Devolver el diccionario de distanciaancias
    return distancia


nodoInicial = 'A'
distancias = busquedaDFS(grafo, nodoInicial)
print(distancias)