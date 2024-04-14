from collections import deque


def bfs(G, v):
    V = len(G)
    distance = [0]*V
    visited = [False]*V
    parent = [None]*V
    toCheck = deque()
    toCheck.append(v)
    
    while len(toCheck) > 0:
        currVertex = toCheck.pop()
        visited[currVertex] = True
        for neighbour in G[currVertex]:
            if not visited[neighbour]:
                toCheck.append(neighbour)
                parent[neighbour] = currVertex
                distance[neighbour] = distance[currVertex] + 1
    
    return visited, distance, parent

def print_way(parentsTab, vertex):
    def rek(vertex):
        nonlocal parentsTab
        if parentsTab[vertex] == None:
            print(f"{vertex}", end="")
        else:
            rek(parentsTab[vertex])
            print(f" -> {vertex}", end="")
    
    rek(vertex)
    print()

if __name__ == "__main__":
    graph1 = [[1,2],
             [4],
             [3,5],
             [4],
             [5],
             [6],
             [7],
             []]
    
    visited, distance, parentsTab = bfs(graph1, 0)
    print(visited)
    print(distance)
    print(parentsTab)
    for vertex in range(len(graph1)):
        print_way(parentsTab, vertex)