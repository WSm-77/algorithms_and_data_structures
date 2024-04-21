# znaleźć ścieżkę pomiędzy wierzchołkami x i y, na której najmniejsza waga krawędzi jest jak największa

# algorytm pascala/kaskala ? 
# rodzina zbiorów rozłącznych

# sortujemy krawędzie po wagach a następnie ustalamy najmniejszą wagę jako wartość środkową z tej tablicy i dfs'em sprawdzamy czy 
# istnieje ścieżka zawierająca same wagi nie mniejsze niż ta środkowa wartość; następnie postępując zgodnie z ideą binary sercha 
# znajdujemy najmniejszą wagę 
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
    print(f"min weight: {minWeight}")
    print("path: ", end="")
    print(*path, sep=" -> ")