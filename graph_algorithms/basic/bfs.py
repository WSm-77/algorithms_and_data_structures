from collections import deque
import sys
sys.path.insert(0, "../")
import graphs

def bfs(G, vertex):
    V = len(G)
    distance = [0]*V
    visited = [False]*V
    parent = [None]*V
    toCheck = deque()
    toCheck.append(vertex)
    visited[vertex] = True

    while len(toCheck) > 0:
        vertex = toCheck.popleft()
        # print(f"vertex: {vertex}")
        for neighbour in G[vertex]:
            if not visited[neighbour]:
                toCheck.append(neighbour)
                visited[neighbour] = True
                parent[neighbour] = vertex
                distance[neighbour] = distance[vertex] + 1

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

    ########## test 1 ##########

    print("test1:")
    visited, distance, parentsTab = bfs(graphs.graph1_list, 0)
    print(visited)
    print(distance)
    print(parentsTab)
    for vertex in range(len(graphs.graph1_list)):
        print_way(parentsTab, vertex)

    ########## test 2 ##########

    print("\ntest2:")
    visited, distance, parentsTab = bfs(graphs.graph18_list, 0)
    print(visited)
    print(distance)
    print(parentsTab)
    for vertex in range(len(graphs.graph18_list)):
        print_way(parentsTab, vertex)
