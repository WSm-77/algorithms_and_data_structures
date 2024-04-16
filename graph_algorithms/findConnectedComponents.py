def reverse_edges(G):
    V = len(G)
    revG = [[] for _ in range(V)]

    for vertex in range(V):
        for neighbour in G[vertex]:
            revG[neighbour].append(vertex)

    return revG

def find_connected_component(G) -> list[list[int]]:
    def dfs_visit1(vertex):
        nonlocal G, V, visited, processedVerteicesTab

        visited[vertex] = True

        for neighbour in G[vertex]:
            if not visited[neighbour]:
                dfs_visit1(neighbour)

        #end for
        processedVerteicesTab.append(vertex)
    #end def

    def dfs_visit2(vertex):
        nonlocal revG, visited, connectedComponents, conCompIdx

        visited[vertex] = True
        connectedComponents[conCompIdx].append(vertex)

        for neighbour in revG[vertex]:
            if not visited[neighbour]:
                dfs_visit2(neighbour)
        #end for
    #end def

    V = len(G)
    visited = [False]*V
    processedVerteicesTab: list[int] = []
    
    for vertex in range(V):
        if not visited[vertex]:
            dfs_visit1(vertex)

    revG = reverse_edges(G)

    connectedComponents: list[list[int]] = []
    conCompIdx = 0
    visited = [False for _ in range(V)]

    for i in range(V - 1, -1, -1):
        vertex = processedVerteicesTab[i]
        if not visited[vertex]:
            connectedComponents.append([])
            dfs_visit2(vertex)
            conCompIdx += 1
    #end for

    return connectedComponents

if __name__ == "__main__":

    ########## test 1 ##########

    graph11 = [[1,5],
               [2],
               [3],
               [4],
               [0],
               [6],
               [7],
               [8],
               [9],
               [10],
               [5]]
    
    print("test1:")
    print(find_connected_component(graph11))

    ########## test 2 ##########

    graph2 = [[1,2],
        [],
        [],
        [6],
        [],
        [3,4],
        [5]]

    print("test2:")
    print(find_connected_component(graph2))