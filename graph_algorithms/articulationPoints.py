# Find bridges in graph

import graphs

def articulation_points(G):
    def dfs_visit(vertex):
        nonlocal G, V, visited, low, parent, visitTime, time, articulationPoints

        visited[vertex] = True
        time += 1
        visitTime[vertex] = time
        low[vertex] = time

        for neighbour in G[vertex]:
            if not visited[neighbour]:
                parent[neighbour] = vertex
                dfs_visit(neighbour)
                low[vertex] = min(low[vertex], low[neighbour])
            elif neighbour != parent[vertex]:
                # Note: backwords edge
                low[vertex] = min(low[vertex], visitTime[neighbour])
            #end if
        #end for

        if low[vertex] == visitTime[vertex] and parent[vertex] != None:
            articulationPoints.append((parent[vertex], vertex))
    #end def

    V = len(G)
    visited = [False]*V

    # Note: low(v) = min(visitTime[v], min(visitTime[next vertex of backwordsEdge]), min(childs low) )
    low = [None]*V
    parent = [None]*V
    visitTime = [0]*V
    time = 0
    articulationPoints = []

    for vertex in range(V):
        if not visited[vertex]:
            dfs_visit(vertex)

    return articulationPoints


if __name__ == "__main__":

    ########### test 1 ###########
    
    articulationPoints = articulation_points(graphs.graph4_list)
    print(articulationPoints)

    ########### test 2 ###########
    
    articulationPoints = articulation_points(graphs.graph16_list)
    print(articulationPoints)