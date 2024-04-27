# szukamy ścieżek od wierzchołka "beg", dla których iloczyn wag krawędzi jest jak najmniejszy

# UWAGA: jeżeli istniałby cykl o iloczynie mniejszym od 1 to nie ma rozwiązania (tak jak dla cyklów o ujemnej wadze w algorytmie
# Dijkstry)

# rozwiązanie: zamieniamy wszystkie wagi na ich logarytmy a następnie wykonujemy algorytm Bellmana-Forda

from math import log2

def list_to_weighted_edges(G):
    V = len(G)
    edges = []

    for vertex in range(V):
        for neighbour, cost in G[vertex]:
            edges.append([vertex, neighbour, cost])

    return edges

def get_number_of_verticies(edges):
    V = 0
    for edge in edges:
        V = max(V, edge[0], edge[1])
    
    return V + 1

def smallest_weights_product(edges, beg):
    INF = float("inf")
    V = get_number_of_verticies(edges)
    distances = [INF]*V
    parents = [None]*V
    distances[beg] = 0

    for i in range(len(edges)):
        edges[i][2] = log2(edges[i][2])

    for _ in range(V - 1):
        for vertex, neighbour, cost in edges:
            if distances[vertex] + cost < distances[neighbour]:
                distances[neighbour] = distances[vertex] + cost
                parents[neighbour] = vertex

    existsNegativeCycle, negativeCycleElement = False, None
    for vertex, neighbour, cost in edges:
        if distances[vertex] + cost < distances[neighbour]:
            existsNegativeCycle, negativeCycleElement = True, neighbour
            break

    for i in range(V):
        distances[i] = 2**distances[i]

    return existsNegativeCycle, negativeCycleElement, parents, distances

def get_way(parents, vertex):
    way = []
    while vertex != None:
        way.append(vertex)
        vertex = parents[vertex]
    
    way.reverse()
    return way

def get_cycle(parents, start):
    V = len(parents)
    visited = [False]*V

    while not visited[start]:
        visited[start] = True
        start = parents[start]

    cycle = [start]
    ptr = parents[start]
    while ptr != start:
        cycle.append(ptr)
        ptr = parents[ptr]

    cycle.append(start)
    cycle.reverse()

    return cycle

def test(testGraph, beg):
    V = get_number_of_verticies(testGraph)
    existsNegativeCycle, negativeCycleStart, parents, distances = smallest_weights_product(testGraph, beg)
    print("distances:")
    print(distances)
    if not existsNegativeCycle:
        for end in range(V):
            print(*get_way(parents, end), sep=" -> ")
    else:
        print("negative cycle detected!!!")
        print(*get_cycle(parents, negativeCycleStart), sep=" -> ")


if __name__ == "__main__":
    ########## test 1 ##########

    graph19_list_weights_modified3 = [[(1, 2), (2, 3), (3, 7), (4, 12)],
                                      [(0, 2), (2, 0.5), (5, 2)],
                                      [(0, 3), (1, 0.5), (4, 2), (5, 0.5), (6, 0.5)],
                                      [(0, 7), (4, 5)],
                                      [(0, 12), (2, 2), (3, 5), (6, 3)],
                                      [(1, 2), (2, 9), (6, 1)],
                                      [(2, 0.5), (4, 3), (5, 1)]]
    
    print("########## test 1 ##########\n\n")
    testGraph = list_to_weighted_edges(graph19_list_weights_modified3)
    test(testGraph, 0)
    
    ########## test 2 ##########

    graph19_list_weights_modified4 = [[(1, 2), (2, 3), (3, 7)],
                                      [(2, 0.5), (5, 2)],
                                      [(4, 2), (5, 2), (6, 0.5)],
                                      [],
                                      [(0, 12), (3, 5), (6, 3)],
                                      [(6, 1)],
                                      []]
    
    print("\n\n########## test 2 ##########\n\n")
    testGraph = list_to_weighted_edges(graph19_list_weights_modified4)
    test(testGraph, 0)