# Wiktor Sędzimir
# 
# Opis algorytmu:
# Ideą algorytmu jest zamiana grafu w postaci listy krawędzi na macierz jednocześnie dodając nowe krawędzie łączące
# planety znajdujące się koło osobliwości z kosztem przejścia przez taką krawędź wynoszącym 0. Następnie korzystamy z algorytmu 
# Dijkstry do znalezienia najkrótszej ścieżki pomiędzy wierzchołkami a i b. Algorytm ma złożoność O( V^2 ), ponieważ korzysta
# z algorytmu Dijkstry dla reprezentacji macierzowej.

from zad5testy import runtests
from queue import PriorityQueue

def edges_to_matrix(edges, V, S):
    nextToSingularity = [False]*V

    for vertex in S:
        nextToSingularity[vertex] = True

    INF = float("inf")
    matrix = [[INF for _ in range(V)] for _ in range(V)]

    for vertex, neighbour, cost in edges:
        matrix[vertex][neighbour] = cost
        matrix[neighbour][vertex] = cost

    for vertex in range(V):
        matrix[vertex][vertex] = 0
        if nextToSingularity[vertex]:
            for neighbour in S:
                matrix[vertex][neighbour] = 0

    return matrix

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje

    V = n
    G = edges_to_matrix(E, V, S)
    INF = float("inf")
    distances = [INF]*V
    distances[a] = 0
    relaxed = [False]*V

    for _ in range(V):
        vertexToRelax = None
        minDistance = INF

        for vertex in range(V):
            if not relaxed[vertex] and distances[vertex] < minDistance:
                vertexToRelax = vertex
                minDistance = distances[vertex]

        if minDistance == INF:
            break

        relaxed[vertexToRelax] = True

        for neighbour in range(V):
            cost = G[vertexToRelax][neighbour]
            if cost >= 0:
                if distances[vertexToRelax] + cost < distances[neighbour]:
                    distances[neighbour] = distances[vertexToRelax] + cost

    return distances[b] if distances[b] != float("inf") else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )