# Rozwiązanie:
# Aby sprawdzić czy delegacja (a, b) jest krytyczna musimy sprawdzić czy istnieje pośrednia droga pomiędzy a i b. W tym
# celu dla każdego wierzchołka wywołujemy algorytm BFS z kolejką zainicjalizowaną sąsiadami tego wierzchołka, których
# początkowo nie oznaczamy jako odwiedzonych. W ten sposób jeżeli ponownie dodamy jakiegoś sąsiada obecnie badanego
# wierzchołka, to wówczas zostanie on oznaczony jako odwiedzony, co będzie oznaczało, że istnieje jakaś pośrednia dorga
# do tego sąsiada.
#
# Analiza złożoności:
# O(EV + V^2) - dla każdego wierzchołka O(V) wykorzystujemy algorytm BFS o złożoności O(V + E) -> O(V * (V + E)) = O(EV + V^2)

from egz1Btesty import runtests
from math import inf as INF
from collections import deque


def create_graph(V, edges):
    graph = [[] for _ in range(V)]

    for vertex, neighbour in edges:
        graph[vertex].append(neighbour)

    return graph

def bfs(V, graph, sources):
    visited = [False for _ in range(V)]
    queue = deque(sources)

    while queue:
        vertex = queue.popleft()

        for neighbour in graph[vertex]:
            if visited[neighbour]:
                continue

            visited[neighbour] = True
            queue.append(neighbour)

    return visited

def critical(V, E):
    res = 0
    graph = create_graph(V, E)

    for vertex in range(V):
        visited = bfs(V, graph, graph[vertex])

        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                res += 1

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)
