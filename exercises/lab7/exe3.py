# Znaleźć "najlepszy korzeń" w drzewie, czyli wierzchołek, dla którego odległość do najdalszego wierzchołka jest jak najmniejsza

# Rozwiązanie: wybieramy dowolny wierzchołek; dla niego znajdujemy najdalszy wierzhołek (ten wierzchołek na pewno będzie 
# jednym z końców najdłuższej ścieżki); następnie znajdujemy najdłuższą ścieżkę wychodzącą ze znalezionego wierzchołka
# pozostaje znaleźć środek tej ścieżki

def farthest_vertex(tree, beg):
    def dfs_visit(vertex, distance):
        # nonlocal maxDistance, farthestVertex
        nonlocal visited, maxDistance, farthestVertex
        visited[vertex] = True

        for neighbour, cost in tree[vertex]:
            if not visited[neighbour]:
                newDistance = distance + cost
                if newDistance > maxDistance:
                    maxDistance = newDistance
                    farthestVertex = neighbour

                parents[neighbour] = (vertex, cost)
                dfs_visit(neighbour, newDistance)
    # end def


    V = len(tree)
    visited = [False]*V
    maxDistance = 0
    farthestVertex = 0
    parents = [None]*V
    dfs_visit(beg, 0)

    return farthestVertex, maxDistance, parents

def best_root(tree: list[list[int]]):
    V = len(tree)
    longestPathBeg, _, _ = farthest_vertex(tree, 0)
    longestPathEnd, distance, parents = farthest_vertex(tree, longestPathBeg)

    currentDistance = 0
    bestRoot = longestPathEnd
    currentCost = 0
    prev = None
    while 2*currentDistance < distance:
        prev = bestRoot
        bestRoot, currentCost = parents[bestRoot]
        currentDistance += currentCost
    #end while
    if distance - currentDistance + currentCost < currentDistance:
        bestRoot = prev

    return bestRoot

def test(testGraph):
    print(f"{best_root(testGraph)} is best root")

if __name__ == "__main__":
    print("########## test 1 ##########\n\n")

    graph25_list_weights = [[(1, 4)],
                            [(0, 4), (2, 3), (3, 2)],
                            [(1, 3)],
                            [(1, 2), (4, 4), (5, 5)],
                            [(3, 4)],
                            [(3, 5)]]
    
    test(graph25_list_weights)

    print("\n\n########## test 2 ##########\n\n")
    
    graph26_list_weights = [[(1, 1)],
                            [(0, 1), (3, 2)],
                            [(3, 3)],
                            [(1, 2), (2, 3), (7, 2)],
                            [(5, 2)],
                            [(7, 3), (4, 2), (6, 4)],
                            [(5, 4)],
                            [(3, 2), (5, 3), (8, 4)],
                            [(7, 4), (10, 3), (11, 6)],
                            [(10, 2)],
                            [(8, 3), (9, 2)],
                            [(8, 6)]]
    
    test(graph26_list_weights)

    print("\n\n########## test 3 ##########\n\n")

    graph26_list_weights_modified = [[(1, 1)],
                                     [(0, 1), (3, 2)],
                                     [(3, 3)],
                                     [(1, 2), (2, 3), (7, 2)],
                                     [(5, 2)],
                                     [(7, 3), (4, 2), (6, 4)],
                                     [(5, 4)],
                                     [(3, 2), (5, 3), (8, 4)],
                                     [(7, 4), (10, 20), (11, 6)],
                                     [(10, 2)],
                                     [(8, 20), (9, 2)],
                                     [(8, 6)]]
    
    test(graph26_list_weights)
