# znaleźć ścieżkę pomiędzy wierzchołkami x i y, na której najmniejsza waga krawędzi jest jak największa

############
# sposób 1 #
############

# sortujemy krawędzie po wagach a następnie łączymy ze sobą wierzchołki pomiędzy którymi znajduje się krawędź o aktualnie
# największej wadze; po każdym dodaniu krawędzi sprawdzamy czy wierzchołki x i y są ze sobą połączone; jeżeli tak, to zwracamy
# ostatnią dodaną wagę
# Złożoność: O(E logE) ~ O(E log V^2) ~ O(E log V)

import sys

sys.path.insert(0, "../../typical_algorithms")
from disjointSets import DisjointSet

def get_path(G, sets: DisjointSet, beg, end, weight):
    def dfs_visit(vertex):
        nonlocal G, V, sets, inSubGraph, end, path, weight
        if vertex == end:
            return True
        
        visited[vertex] = True

        for neighbour, currWeight in G[vertex]:
            if inSubGraph[neighbour] and not visited[neighbour] and currWeight >= weight:
                path.append(neighbour)
                if dfs_visit(neighbour):
                    return True
                #end if
                path.pop()
            #end if
        #end for

        return False
    #end def

    V = len(G)
    begRepr = sets.find(beg)
    inSubGraph = [begRepr == sets.find(i) for i in range(V)]
    visited = [False]*V
    path = [beg]

    dfs_visit(beg)

    return path

def list_to_edges(G,V):
    edges = []

    for vertex in range(V):
        for neighbourIdx in range(len(G[vertex])):
            neighbour, weight = G[vertex][neighbourIdx]

            edges.append((min(vertex, neighbour), max(neighbour, vertex), weight))
        # end for
    #end for
    return edges

def max_minimal_weight(G, beg, end):
    V = len(G)

    sets = DisjointSet(V)
    edges = list_to_edges(G, V)
    edges.sort(key = lambda x: x[2], reverse = True)

    result = 0

    for vertex, neighbour, weight in edges:
        # print(vertex, neighbour, weight)
        sets.union(vertex, neighbour)
        result = weight
        if sets.in_same_set(beg, end):
            return (result, get_path(G, sets, beg, end, result))
    # end for

    print("smth gone wrong...")
    return (result, [])

############
# sposób 2 #
############

# Korzystamy z algorytmu Dijikstry, jednakże tym razem zamiast sprawdzać minimalny koszt dotarcia do wierzchołka sprawezamy
# maksymalną wagę minimalnej krawędzi; z kolejki priorytetowej wyjmujemy więc wierzchołki, dla których aktualna maksymalna waga
# minimalnej krawędzi jest jak największa 

from queue import PriorityQueue

def print_path(parent, destination):
    def rek(vertex):
        nonlocal parent
        if parent[vertex] == None:
            print(f"{vertex}", end="")
        else:
            rek(parent[vertex])
            print(f" -> {vertex}", end="")
    #end def
    rek(destination)
    print()

# Note: we use negative values while adding to PriorityQueue to make it return elements with lowest priority
def max_minimal_weight2(G, beg, end):
    INF = float("inf")
    V = len(G)
    maxMinWeight = [0]*V
    parent = [None]*V
    toCheck = PriorityQueue()
    toCheck.put((-INF, beg))
    maxMinWeight[beg] = INF

    while not toCheck.empty():
        currentMaxMinWeight, vertex = toCheck.get()
        currentMaxMinWeight = -currentMaxMinWeight

        if vertex == end:
            break

        for neighbour, weight in G[vertex]:
            newMaxMinWeight = min(currentMaxMinWeight, weight)
            if newMaxMinWeight > maxMinWeight[neighbour]:
                maxMinWeight[neighbour] = newMaxMinWeight
                toCheck.put((-newMaxMinWeight, neighbour))
                parent[neighbour] = vertex
        #end for
    #end while

    return maxMinWeight[end], parent


if __name__ == "__main__":
    graph19_list_weights_modified = [[(1, 2), (2, 3), (3, 7), (4, 12)],
                                     [(0, 2), (2, 4), (5, 2)],
                                     [(0, 3), (1, 4), (4, 2), (5, 9), (6, 5)],
                                     [(0, 7), (4, 5)],
                                     [(2, 2), (3, 5), (6, 4)],
                                     [(2, 9), (6, 1)],
                                     [(2, 5), (4, 4), (5, 1)]]
    
    
    beg = 0
    end = 5
    minWeight, path = max_minimal_weight(graph19_list_weights_modified, beg, end)
    print("solution 1:")
    print(f"min weight: {minWeight}")
    print("path: ", end="")
    print(*path, sep=" -> ")

    print("\nsolution 2:")
    minWeight, parent = max_minimal_weight2(graph19_list_weights_modified, beg, end)
    print(f"min weight: {minWeight}")
    print_path(parent, end)