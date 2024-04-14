def dfs(G: list[list[int]]):
    def dfs_visit(vertex):
        nonlocal G, V, visited, visitTime, processTime, time

        visited[vertex] = True
        time += 1
        visitTime[vertex] = time
        for neighbour in G[vertex]:
            if not visited[neighbour]:
                dfs_visit(neighbour)
        #end for

        time += 1
        processTime[vertex] = time
    #end def

    V = len(G)
    visited = [False]*V
    visitTime = [-1]*V
    processTime = [-1]*V
    time = 0


    for vertex in range(V):
        if not visited[vertex]:
            dfs_visit(vertex)
    
    return visited, visitTime, processTime

if __name__ == "__main__":
    graph1 = [[1,2],
             [4],
             [3,5],
             [4],
             [5],
             [6],
             [7],
             []]
    
    print("graph 1:")
    visited, visitTime, processTime = dfs(graph1)
    print(visited)
    print(visitTime)
    print(processTime, end="\n\n")

    graph2 = [[1,2],
            [],
            [],
            [6],
            [],
            [3,4],
            [5]]
    
    print("graph 2:")
    visited, visitTime, processTime = dfs(graph2)
    print(visited)
    print(visitTime)
    print(processTime, end="\n\n")

    graph3 = [[4],
            [4,6],
            [4,5],
            [5],
            [0,1,2],
            [2,3],
            [1]]

    print("graph 3:")
    visited, visitTime, processTime = dfs(graph3)
    print(visited)
    print(visitTime)
    print(processTime, end="\n\n")