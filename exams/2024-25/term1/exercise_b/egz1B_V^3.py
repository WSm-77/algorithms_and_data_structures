# Rozwiązanie:
# Aby sprawdzić czy delegacja (a, b) jest krytyczna musimy sprawdzić czy istnieje pośrednia droga pomiędzy a i b. W tym
# celu dla każdej krawędzi sprawdzamy czy istnieje droga pomiędzy jej początkiem a końcem nie wykorzystująca tej
# krawędzi. Robimy to korzstając z modyfikacji algorytmu Floyda-Warshalla, w której zamiast szukania najkrótszej ścieżki
# staramy się ją jak najbardziej przedłużać
#
# Analiza złożoności:
# O(V^3) - złożoność algorytmu Floyda-Warshalla

from egz1Btesty import runtests
from math import inf as INF


def create_graph(V, edges):
    graph = [[0 for _ in range(V)] for _ in range(V)]

    for vertex, neighbour in edges:
        graph[vertex][neighbour] = 1

    return graph

def critical(V, E):
    res = 0
    distances = create_graph(V, E)

    for through in range(V):
        for source in range(V):
            for target in range(V):
                if distances[source][through] == 0 or distances[through][target] == 0:
                    continue

                # use max() instead of min() to search for longer paths
                distances[source][target] = max(distances[source][through] + distances[through][target], distances[source][target])

    for vertex, neighbour in E:
        if distances[vertex][neighbour] == 1:
            res += 1

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)
