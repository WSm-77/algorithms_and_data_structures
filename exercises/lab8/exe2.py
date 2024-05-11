# Jak w grafie skierowanym znaleźć cykl o minimalnej wadze

# Wykonujemy algortym Floyda-Warshalla, a następnie dla każdej pary wierzchołków dodajemy odległości od A -> B oraz B -> A
# Dla grafów nieskierowanych, można dla każdej krawędzi znaleźć ścieżkę pomiędzy jej dwoma końcami, która nie zawiera tej
# krawędzi (stworzyć graf niezawierający tej krawędzi a następnie wykonać algorytm Dijkstry).

def floyd_warshall(G):
    V = len(G)
    distances = [[G[R][C] for C in range(V)] for R in range(V)]
    parents = [[None for _ in range(V)] for _ in range(V)]

    for i in range(V):
        for vertex in range(V):
            for neighbour in range(V):
                newDistance = distances[vertex][i] + distances[i][neighbour]
                if newDistance < distances[vertex][neighbour]:
                    distances[vertex][neighbour] = newDistance
                    parents[vertex][neighbour] = i

    return distances, parents

def get_cycle(parents, cycleStart, cycleThrough):
    def get_path(path: list, beg, end):
        through = parents[beg][end]

        if through is None:
            path.append(beg)
        else:
            get_path(path, beg, through)
            get_path(path, through, end)
    #end def

    path1 = []
    path2 = []
    get_path(path1, cycleStart, cycleThrough)
    get_path(path2, cycleThrough, cycleStart)

    return path1 + path2 + [cycleStart]

def find_min_cost_cycle(G):
    V = len(G)

    distances, parents = floyd_warshall(G)

    cycleStart, cycleThrough, cycleMinCost = None, None, float("inf")

    for vertex1 in range(V):
        for vertex2 in range(V):
            if vertex1 == vertex2:
                continue

            cycleCost = distances[vertex1][vertex2] + distances[vertex2][vertex1]
            if cycleCost < cycleMinCost:
                cycleStart, cycleThrough, cycleMinCost = vertex1, vertex2, cycleCost

    cycle = None

    # check if such a cycle exists
    if cycleStart != None:
        cycle = get_cycle(parents, cycleStart, cycleThrough)

    return cycleMinCost, cycle

def test(testGraph):
    cycleMinCost, cycle = find_min_cost_cycle(testGraph)
    print(f"cycle minimal cost: {cycleMinCost}")
    print("cycle:", end=" ")
    print(*cycle, sep=" -> ")

if __name__ == "__main__":

    print("########### test 1 ###########\n\n")

    inf = float("inf")

    graph21_matrix_weights_modified = [[0, inf, inf, inf, inf, inf, inf, 2, inf, inf, inf],
                                       [inf, 0, inf, inf, inf, 1, inf, inf, inf, 4, inf],
                                       [inf, inf, 0, 3, inf, inf, inf, inf, inf, inf, inf],
                                       [inf, inf, inf, 0, 2, inf, inf, inf, inf, inf, inf],
                                       [inf, inf, 2, inf, 0, 1, inf, inf, inf, inf, inf],
                                       [inf, inf, 5, inf, inf, 0, inf, inf, inf, inf, inf],
                                       [inf, inf, 4, inf, inf, inf, 0, inf, inf, inf, 4],
                                       [inf, 5, inf, inf, inf, inf, inf, 0, inf, inf, inf],
                                       [inf, inf, inf, 1, inf, inf, 3, inf, 0, inf, inf],
                                       [2, inf, inf, inf, inf, inf, inf, inf, inf, 0, inf],
                                       [inf, inf, inf, inf, inf, inf, inf, inf, 5, 4, 0]]

    test(graph21_matrix_weights_modified)


    print("\n\n########### test 2 ###########\n\n")

    graph21_matrix_weights_modified[3][4] = 10
    test(graph21_matrix_weights_modified)

    print("\n\n########### test 3 ###########\n\n")

    graph21_matrix_weights_modified[6][10] = 10
    test(graph21_matrix_weights_modified)
