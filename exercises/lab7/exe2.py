# Znaleźć najkrótsze ścieżki wychodzące z jednego wierzchołka w DAG'u

# Rozwiązanie: sortujemy topologicznie a następnie relaksujemy w kolejności wskazanej przez sortowanie topologiczne

def modified_topological_sort(G, beg):
    def dfs_visit(vertex):
        nonlocal G, V, topologicalySorted, visited
        visited[vertex] = True
        for  neighbour, _ in G[vertex]:
            if not visited[neighbour]:
                dfs_visit(neighbour)
        topologicalySorted.append(vertex)
    #end def

    V = len(G)
    visited = [False]*V
    topologicalySorted = []

    dfs_visit(beg)
    topologicalySorted.reverse()

    return topologicalySorted

def shortest_path_in_DAG(G, beg):
    INF = float("inf")
    V = len(G)
    topologicalySorted = modified_topological_sort(G, beg)
    parents = [None]*V
    distances = [INF]*V
    distances[beg] = 0

    for vertex in topologicalySorted:
        for neighbour, cost in G[vertex]:
            newDistance = distances[vertex] + cost
            if newDistance < distances[neighbour]:
                distances[neighbour] = newDistance
                parents[neighbour] = vertex

    return distances, parents

def print_path(parents, vertex):
    path = []
    while vertex != None:
        path.append(vertex)
        vertex = parents[vertex]
    path.reverse()
    print(*path, sep=" -> ")

def test(G, beg):
    V = len(G)
    distances, parents = shortest_path_in_DAG(G, beg)
    for vertex in range(V):
        if parents[vertex] != None:
            print(f"\ndistance to vertex {vertex}: \n{distances[vertex]}")
            print("path:")
            print_path(parents, vertex)

if __name__ == "__main__":

    ####### test 1 #######

    graph1_list_weights = [[(1, 3), (2, 4)],
                           [(4, 5)],
                           [(3, 1),(5, 3)],
                           [(4, 2)],
                           [(5, 6)],
                           [(6, 1)],
                           [(7, 2)],
                           []]
    
    print("####### test 1 #######\n")
    test(graph1_list_weights, 0)

    ####### test 2 #######

    graph17_list_weights = [[(1, 1),(3, 3),(7, 4)],
                            [(2, 2)],
                            [(3, 7),(5, 5),(8, 2)],
                            [(4, 3),(6, 1)],
                            [(5, 3)],
                            [(6, 6),(7, 5),(8, 4)],
                            [(7, 7)],
                            [(8, 3),(9, 1)],
                            [(9, 2)],
                            [(10, 1)],
                            []]
    
    print("\n\n####### test 2 #######\n")
    test(graph17_list_weights, 0)
    