# Rozwiązanie:
# Aby sprawdzić czy delegacja (a, b) jest krytyczna musimy sprawdzić czy istnieje pośrednia droga pomiędzy a i b. W tym
# celu dla każdej krawędzi sprawdzamy czy istnieje droga pomiędzy jej początkiem a końcem nie wykorzystująca tej 
# krawędzi. Robimy to korzstając z algorytmu BFS z dodatkowym warunkiem sprawdzającym czy przypadkiem nie korzystamy 
# z zabronionej krawędzi.
# 
# Analiza złożoności:
# O(EV + E^2) - dla każdej krawędzi O(E) wykorzystujemy algorytm BFS o złożoności O(V + E) -> O(E * (V + E)) = O(EV + E^2) 

from egz1Btesty import runtests
from math import inf as INF
from collections import deque


def create_graph(V, edges):
    graph = [[] for _ in range(V)]

    for vertex, neighbour in edges:
        graph[vertex].append(neighbour)

    return graph

def is_critical(graph, edge_start, edge_end):
    V = len(graph)
    queue = deque()
    visited = [False for _ in range(V)]
    visited[edge_start] = True

    queue.append(edge_start)

    while queue:
        vertex = queue.popleft()
        if vertex == edge_end:
            return False

        for neighbour in graph[vertex]:
            if (vertex == edge_start and neighbour == edge_end) or visited[neighbour]:
                continue

            queue.append(neighbour)
            visited[neighbour] = True

    return True

def critical(V, E):
    res = []
    graph = create_graph(V, E)
    for edge_start, edge_end in E:
        
        if is_critical(graph, edge_start, edge_end):
            res.append((edge_start, edge_end))

    return len(res)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)    
