# Wiktor Sędzimir
# 
# Opis algorytmu:
# Ideą algorytmu jest zamiana grafu w postaci listy krawędzi na listę sąsiedztwa i następnie dodanie dodatkowych krawędzi łączących
# planety znajdujące się koło osobliwości z kosztem przejścia przez taką krawędź wynoszącym 0. Następnie korzystamy z algorytmu 
# Dijkstry do znalezienia najkrótszej ścieżki pomiędzy wierzchołkami a i b. Algorytm ma złożoność O( V^2 log V ), ponieważ dodanie
# kolejnych krawędzi może spowodować powstanie grafu pełnego, w którym liczba krawędzi jest rzędu V^2, natomiast złożoność czasowa
# algorymu Dijkstry jest rzędu E log V.

from zad5testy import runtests
from queue import PriorityQueue

# dodaje krawędzie pomiędzy osobliwościami
def edges_to_graph(E, V, S):
    graph = [[] for _ in range(V)]

    # graf pierwotny
    for vertex, neighbour, cost in E:
        graph[vertex].append((neighbour, cost))
        graph[neighbour].append((vertex, cost))

    nextToSingularity = [False]*V
    for vertex in S:
        nextToSingularity[vertex] = True

    # graf z uwzględnieniem krawędzi pomiędzy osobliwościami
    for vertex in range(V):
        if nextToSingularity[vertex]:
            for neighbour in S:
                if neighbour == vertex:
                    continue

                graph[vertex].append((neighbour, 0))
            #end for
    #end for

    return graph

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje

    V = n

    G = edges_to_graph(E, V, S)
    distances = [float("inf")]*V
    toVisit = PriorityQueue()
    toVisit.put((0, a))
    distances[a] = 0

    while not toVisit.empty():
        distance, vertex = toVisit.get()
        if distance > distances[vertex]:
            continue

        for neighbour, cost in G[vertex]:
            if distance + cost < distances[neighbour]:
                distances[neighbour] = distance + cost
                toVisit.put((distances[neighbour], neighbour))
            #end if
        #end for

    return distances[b] if distances[b] != float("inf") else None
    # return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )