# find Hamilton's path in DAG

# odp: sortujemy topologicznie a następnie sprawdzamy czy pomiędzy każdą parą sąsiednich wierzchołków po posortowaniu znajduje się krawędź

def topological_sort(G):
    def dfs_visit(vertex):
        nonlocal G, V, sortIdx

        visited[vertex] = True

        for neighbour in G[vertex]:
            if not visited[neighbour]:
                dfs_visit(neighbour)
        #end for

        topologicalSort[sortIdx] = vertex
        sortIdx -= 1

    #end def

    V = len(G)
    visited = [False]*V
    topologicalSort = [None]*V
    sortIdx = V - 1

    for vertex in range(V):
        if not visited[vertex]:
            dfs_visit(vertex)
    #end for

    return topologicalSort

def hamilton_path(G):
    topologicalySorted = topological_sort(G)

    isHamiltonPath = True

    for i in range(len(topologicalySorted) - 1):
        vertex, neighbour = topologicalySorted[i], topologicalySorted[i + 1]

        if neighbour not in G[vertex]:
            isHamiltonPath = False
            break
        #end if
    #end for

    return (isHamiltonPath, topologicalySorted)

if __name__ == "__main__":

    ############# test 1 #############

    print("test1")

    graph17_list = [[1,3,7],
                    [2],
                    [3,5,8],
                    [4,6],
                    [5],
                    [6,7,8],
                    [7],
                    [8,9],
                    [9],
                    [10],
                    []]
    
    isHamiltonian, path = hamilton_path(graph17_list)
    if isHamiltonian:
        print(f"this graph is hamiltonian\nhamilton's path: {path}")
    else:
        print("this graph is not hamiltonian")

    ############# test 2 #############

    print("\ntest2")

    graph18_list = [[1,2,4],
            [3,5],
            [5,6],
            [6],
            [6,7],
            [8],
            [5,8],
            [],
            [7]]

    isHamiltonian, path = hamilton_path(graph18_list)
    if isHamiltonian:
        print(f"this graph is hamiltonian\nhamilton's path: {path}")
    else:
        print("this graph is not hamiltonian")