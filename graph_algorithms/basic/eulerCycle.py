# find Euler cycle in graph

# only for non-directed graphs
def get_number_of_edges(G):
    V = len(G)
    E = 0
    for vertex in range(V):
        E += len(G[vertex])
    #end for
    return E//2

def is_connected(G):
    def dfs_visit(vertex):
        nonlocal G, visited, visitedCnt

        visited[vertex] = True
        visitedCnt += 1

        for neighbour in G[vertex]:
            if not visited[neighbour]:
                dfs_visit(neighbour)

    V = len(G)
    visited = [False]*V
    visitedCnt = 0

    dfs_visit(0)

    return visitedCnt == V

def is_eulerian(G) -> bool:
    V = len(G)
    for vertex in range(V):
        if len(G[vertex]) % 2 != 0:
            return False
    #end for

    return is_connected(G)

def find_euler_cycle(G) -> list[int]:
    def dfs_visit(vertex, prevVertex):
        nonlocal V, visitedEdges, eulerCycle, eulerCycleIdx

        for neighbourId in range(len(G[vertex])):
            neighbour = G[vertex][neighbourId]
            if neighbour == prevVertex:
                visitedEdges[vertex][neighbourId] = True
                break
        #end for
        for neighbourId in range(len(G[vertex])):
            neighbour = G[vertex][neighbourId]
            if not visitedEdges[vertex][neighbourId]:
                visitedEdges[vertex][neighbourId] = True
                dfs_visit(neighbour, vertex)
        #end for

        eulerCycle[eulerCycleIdx] = vertex
        eulerCycleIdx -= 1
    #end def

    V = len(G)
    E = get_number_of_edges(G)

    visitedEdges = [[False for _ in G[vertex]] for vertex in range(V)]
    eulerCycle = [0]*(E+1)
    eulerCycleIdx = E

    visitedEdges[0][0] = True
    dfs_visit(G[0][0], 0)

    # print(*visitedEdges, sep="\n")

    return eulerCycle


if __name__ == "__main__":

    ####### test 1 #######

    graph12 = [[1,2],
               [3,5,6,4,2,0],
               [0,1,3,4,5,6],
               [4,1,5,2],
               [5,1,2,3],
               [2,3,1,4],
               [1,2]]

    print("test1:")
    if is_eulerian(graph12):
        print("graph12 is Eulerian\nEuler Cycle:")
        print(find_euler_cycle(graph12))
    else:
        print("graph12 is not Eulerian")

    ###### test 2 #######

    graph13 = [[1,4],
               [0,2,4],
               [1,3],
               [2,4],
               [0,1,3]]

    print("\ntest2:")
    if is_eulerian(graph13):
        print("graph13 is Eulerian\nEuler Cycle:")
        print(find_euler_cycle(graph13))
    else:
        print("graph13 is not Eulerian")

    ###### test 3 #######

    graph14 = [[1,2,3,4],
               [0,2,3,4],
               [0,1,3,4],
               [0,1,2,4],
               [0,1,2,3]]

    print("\ntest3:")
    if is_eulerian(graph14):
        print("graph14 is Eulerian\nEuler Cycle:")
        print(find_euler_cycle(graph14))
    else:
        print("graph14 is not Eulerian")
