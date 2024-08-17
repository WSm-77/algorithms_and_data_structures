# Opis algorytmu:
# Zauważmy, że nasza trasa zawsze będzie miała stałą liczbę odwiedzony wierzchołków oraz krawędzi (odwiedzimy w sumie
# 5 wierzchołków i przejdziemy po 4 krawędziach). W tym rozwiązaniu będziemy zapisywać minimalną odległość, do każdego
# wierzchołka z wierzchołka "source", przy założeniu, że był on i-tym odwiedzonym wierzchołkiem. Informacje te będziemy
# zapisywać w tablicy distance[vertex][i]. Rozwiązaniem jest minimalna odległość od wierzchołka "source" do wierzchołka
# "target", przy założeniu, że jest on 4-tym odwiedzonym wierzchołkiem (indeksujemy oczywiście od 0).

from egzP1btesty import runtests
from queue import PriorityQueue

def get_number_of_verticies(edges):
    V = 0
    for vertex, neighbour, _ in edges:
        V = max(V, vertex, neighbour)
    return V + 1

def edges_to_graph(edges):
    V = get_number_of_verticies(edges)
    graph = [[] for _ in range(V)]

    for vertex, neighobur, cost in edges:
        graph[vertex].append((neighobur, cost))
        graph[neighobur].append((vertex, cost))

    return graph

def turysta( G, D, L ):
    #tutaj proszę wpisać własną implementację
    source = D
    target = L

    graph = edges_to_graph(G)
    V = len(graph)
    INF = float("inf")

    # distance[vertex][visitedIdx] - distance from source to vertex it is visitedIdx-th vertex visited
    distances = [[INF for _ in range(5)] for _ in range(V)]
    distances[source][0] = 0
    toCheck = PriorityQueue()
    toCheck.put((0, source, 0))

    while not toCheck.empty():
        currDist, vertex, visitedIdx = toCheck.get()

        if currDist > distances[vertex][visitedIdx]:
            continue

        if visitedIdx == 4:
            if vertex == target:
                break
            else:
                continue

        for neighbour, cost in graph[vertex]:
            newVisitedIdx = visitedIdx + 1
            newDist = currDist + cost
            if neighbour != source and newDist < distances[neighbour][newVisitedIdx]:
                distances[neighbour][newVisitedIdx] = newDist
                toCheck.put((newDist, neighbour, newVisitedIdx))

    return distances[target][4]

runtests ( turysta )
