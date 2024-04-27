import graphs

def floyd_warshall(G: list[list[int]]):
    V = len(G)
    INF = float("inf")
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

def get_path(parents, beg, end):
    path = []
    def rek(beg, end):
        if parents[beg][end] is None:
            path.append(beg)
            return
        rek(beg, parents[beg][end])
        rek(parents[beg][end], end)

    rek(beg, end)
    path.append(end)

    return path

def test(graphList):
    graphMatrix = graphs.list_to_weighted_matrix(graphList)
    distances, parents = floyd_warshall(graphMatrix)
    print("distances:")
    print(*distances, sep="\n")
    print("parents:")
    print(*parents, sep="\n")
    compare_to_dijkstra(graphList, distances, parents)


from dijkstra import dijkstra

def compare_to_dijkstra(graphList, distancesFloyd, parentsFloyd):
    print("\nchecking if distances are the same for Floyd-Warshall and Dijkstra algorithms...")
    V = len(graphList)
    distancesDijkstra = []
    parentsDijkstra = []

    for vertex in range(V):
        distance, parent = dijkstra(graphList, vertex)
        distancesDijkstra.append(distance)
        parentsDijkstra.append(parent)

    sameDistances = True

    for beg in range(V):
        for end in range(V):
            if beg == end:
                continue

            if distancesFloyd[beg][end] != distancesDijkstra[beg][end]:
                sameDistances = False
                print(f"distances from {beg} to {end} differ")
                pathFloyd = get_path(parentsFloyd, beg, end)
                pathDijkstra = graphs.get_way(parentsDijkstra[beg], end)
                if pathFloyd != pathDijkstra:
                    print(f"paths from {beg} to {end} differ")
                    print(*pathFloyd, sep=" -> ")
                    print(*pathDijkstra, sep=" -> ")
    
    print("test result: ", end="")
    if sameDistances:
        print("PASSED")
    else:
        print("FAILED")



if __name__ == "__main__":
    ####### test 1 #######

    print("####### test 1 #######\n\n")
    testGraphList = graphs.graph19_list_weights
    test(testGraphList)

    ####### test 2 #######

    print("\n\n####### test 2 #######\n\n")
    testGraphList = graphs.graph20_list_weights
    test(testGraphList)