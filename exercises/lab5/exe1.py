# Sprawdzić czy graf jest dwudzielny (macierz asocjacji).   PL
# Check if graph is bipartite (association matrix)          ENG

from collections import deque

def is_bipartite(G):
    def bfs(vertex):
        nonlocal G, V, visited, color, parent
        currentColor = True
        toVisit = deque()
        toVisit.append(vertex)
        while len(toVisit) > 0:
            currentVertex = toVisit.popleft()
            visited[currentVertex] = True

            # our color is different than our parents color
            currentColor = not color[parent[currentVertex]]
            color[currentVertex] = currentColor
            for neighbour in range(V):

                # checking if the edge exists
                if G[currentVertex][neighbour] == 1:
                    if visited[neighbour]:

                        # if our neighbour got the same color, we know that this graph is not bipartite
                        if color[neighbour] == currentColor:
                            return False
                    else:
                        parent[neighbour] = currentVertex
                        toVisit.append(neighbour)
            #end while
        return True
    #end def

    V = len(G)
    visited = [False]*V
    parent = [0]*V
    color = [False]*V       # eg. False - red, True - green

    # checking for every connected component
    for vertex in range(V):
        if not visited[vertex]:
            if not bfs(vertex):
                return False
            
    return True


    


if __name__ == "__main__":
    graph4 = [
        #0 1 2 3 4 5 6
        [0,0,0,0,1,0,0], #0
        [0,0,0,0,1,1,1], #1
        [0,0,0,0,1,1,0], #2
        [0,0,0,0,0,1,0], #3
        [1,1,1,0,0,0,0], #4
        [0,1,1,1,0,0,0], #5
        [0,1,0,0,0,0,0]  #6
             ]
    
    print(is_bipartite(graph4))
    
    graph5 = [[0,1,0],
             [1,0,1],
             [0,1,0]]
    
    print(is_bipartite(graph5))

    graph6 = [
        #0,1,2,3,4,5,6
        [0,1,0,0,1,0,0], #0
        [1,0,0,0,1,1,1], #1
        [0,0,0,0,1,1,0], #2
        [0,0,0,0,0,1,0], #3
        [1,1,1,0,0,0,0], #4
        [0,1,1,1,0,0,0], #5
        [0,1,0,0,0,0,0]  #6
             ]
    
    print(is_bipartite(graph6))