from queue import PriorityQueue

def prim_list(G, root):
    V = len(G)
    INF = float("inf")
    parents = [None for _ in range(V)]
    weights = [INF for _ in range(V)]
    weights[root] = 0
    visited = [False for _ in range(V)]
    toCheck = PriorityQueue()
    toCheck.put((0, root))

    while not toCheck.empty():
        _, vertex = toCheck.get()

        if visited[vertex]:
            continue

        visited[vertex] = True

        for neighbour, weight in G[vertex]:
            if not visited[neighbour] and weight < weights[neighbour]:
                weights[neighbour] = weight
                parents[neighbour] = vertex
                toCheck.put((weight, neighbour))

    return parents_to_graph(parents, weights)

def parents_to_graph(parents, weights):
    V = len(parents)
    G = [[] for _ in range(V)]

    for vertex in range(V):
        parent = parents[vertex]
        if parent == None:
            continue

        G[parent].append((vertex, weights[vertex]))
        # G[vertex].append((parent, weights[vertex]))

    return G


if __name__ == "__main__":
    
    print("######### test 1 #########\n\n")

    graph19_list_weights = [[(1, 2), (2, 3), (3, 7), (4, 12)],
                        [(0, 2), (2, 4), (5, 2)],
                        [(0, 3), (1, 4), (4, 2), (5, 9), (6, 5)],
                        [(0, 7), (4, 5)],
                        [(0, 12), (2, 2), (3, 5), (6, 3)],
                        [(1, 2), (2, 9), (6, 1)],
                        [(2, 5), (4, 3), (5, 1)]]
    
    print("MST (list):")
    print(*prim_list(graph19_list_weights, 0), sep="\n")

    print("\n\n######### test 2 #########\n\n")

    graph20_list_weights = [[(1, 1), (2, 2)],
                        [(0, 1), (3, 3), (4, 2)],
                        [(0, 2), (3, 1), (6, 7)],
                        [(1, 3), (2, 1), (5, 2), (7, 3)],
                        [(1, 2), (7, 5)],
                        [(3, 3), (6, 1), (8, 8)],
                        [(2, 7), (5, 1), (8, 4)],
                        [(3, 3), (4, 5), (8, 1)],
                        [(5, 8), (6, 4), (7, 1)]]
    
    print("MST (list):")
    print(*prim_list(graph20_list_weights, 0), sep="\n")