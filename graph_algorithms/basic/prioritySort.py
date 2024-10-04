def priority_sort(G):
    def dfs_visit(vertex):
        nonlocal G, visited, priority, prioTabIdx

        visited[vertex] = True
        for neighbour in G[vertex]:
            if not visited[neighbour]:
                dfs_visit(neighbour)
        #end for
        priority[prioTabIdx] = vertex
        prioTabIdx -= 1
    #end def

    V = len(G)
    visited = [False]*V
    priority = [None]*V
    prioTabIdx = V - 1
    for vertex in range(V):
        if not visited[vertex]:
            dfs_visit(vertex)

    return priority

if __name__ == "__main__":

    ######### test 1 #########

    print("test1:")
    graph1 = [[1,2],
            [4],
            [3,5],
            [4],
            [5],
            [6],
            [7],
            []]

    priority = priority_sort(graph1)
    print(priority)

    ######### test 2 #########

    print("\ntest2:")
    graph10 = [[1,2,4],
               [3,5],
               [5,6],
               [6],
               [6,7],
               [8],
               [],
               [],
               [7]]

    priority = priority_sort(graph10)
    print(priority)
