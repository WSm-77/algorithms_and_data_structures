# sprawdzić czy istnieje krawędź w grafie nieskierowanym, której usunięcie spowoduje zwiększenie najkrótszej ścieżki pomiędzy dwoma wierzchołkami
# (x, y) lub ta ścieżka przestanie istnieć

# przeszukujemy od x do y zapisując najkrótsze ścieżki do każdego wierzchołka; następnie przechodzimy od x do y znowu znajdując najkrótsze ścieżki
# i dodając te odległości do tablicy zawierającej odległości z pierwszego przeszukania; jeżeli ta suma jest równa odległości od x do y, 
# to wierzchołek ten leży na jednej z najkrótszej ścieżek
# w otrzymanym podgrafie znajdujemy most

from collections import deque

def bfs(G, vertex):
    V = len(G)
    visited = [False]*V
    toVisit = deque()
    toVisit.append(vertex)
    visited[vertex] = True
    distance = [0]*V

    while toVisit:
        vertex = toVisit.popleft()
        # print(vertex, end=" ")

        for neighbour in G[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                toVisit.append(neighbour)
                distance[neighbour] = distance[vertex] + 1
        # end for
    #end while

    # print()

    return distance

def does_protract_path(G, beg, end):
    V = len(G)
    distance = bfs(G, beg)
    shortestPathLen = distance[end]
    distance2 = bfs(G, end)
    subGraph = [False]*V

    for vertex in range(V):
        distance[vertex] += distance2[vertex]
        subGraph[vertex] = distance[vertex] == shortestPathLen
    #end for

    visited = [False]*V
    toCheck = deque()
    toCheck.append(beg)
    visited[beg] = True

    while toCheck:
        vertex = toCheck.popleft()
        isOnlyVertexWithCurrentDistance = len(toCheck) == 0
        for neighbour in G[vertex]:
            if not visited[neighbour] and subGraph[neighbour]:
                visited[neighbour] = True
                toCheck.append(neighbour)
        #end for

        if len(toCheck) == 1 and isOnlyVertexWithCurrentDistance:
            return (vertex, toCheck.popleft())
    #end while

    return None



if __name__ == "__main__":

    graph6_list = [[1, 4],
                   [0, 4, 5, 6],
                   [4, 5],
                   [5],
                   [0, 1, 2],
                   [1, 2, 3],
                   [1]]
    
    x = 0
    y = 3
    print(f"path form {x} to {y}")
    print(f"{does_protract_path(graph6_list, x, y)}")

    x = 4
    y = 5
    print(f"path form {x} to {y}")
    print(f"{does_protract_path(graph6_list, x, y)}")



    