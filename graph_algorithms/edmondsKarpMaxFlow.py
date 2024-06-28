from collections import deque
import graphs

def get_number_of_verticies(E):
    V = 0
    for vertex, neighbour, _ in E:
        V = max(V, vertex, neighbour)
    return V + 1

def edges_to_matrix(E):
    V = get_number_of_verticies(E)
    matrix = [[0 for _ in range(V)] for _ in range(V)]

    for vertex, neighbour, cost in E:
        matrix[vertex][neighbour] = cost
        matrix[neighbour][vertex] = cost

    return matrix

def update_flow(flow, bottleneck, parents, target):
    vertex = target
    prevVertex = parents[vertex]

    while prevVertex != None:
        flow[prevVertex][vertex] += bottleneck
        flow[vertex][prevVertex] -= bottleneck
        vertex, prevVertex = prevVertex, parents[vertex]


def edmonds_karp(matrix, source, target):
    V = len(matrix)

    # flow[vertex][neighbour] represents how much water already flows from vertex 
    # to neighbour; if flow[vertex][neighbour] is negative it means that such
    # an amount of water already flows from neighbour to vertex
    flow = [[0 for _ in range(V)] for _ in range(V)]
    parents = [None]*V
    
    # because we will repeat BFS algorithm few times we use visitedId to differentiate 
    # in which instance of BFS we visited each vertex
    visitedId = 1
    visited = [0]*V

    INF = float("inf")
    maxFlow = 0

    while True:
        bottleneck = INF

        # tocheck = (vertex, bottleneck)
        toCheck = deque()
        toCheck.append((source, bottleneck))
        visited[source] = visitedId
        foundPath = False

        while toCheck:
            vertex, currBottleneck = toCheck.popleft()

            if vertex == target:
                foundPath = True
                bottleneck = currBottleneck
                break

            for neighbour in range(V):
                remaining = matrix[vertex][neighbour] - flow[vertex][neighbour]
                if visited[neighbour] != visitedId and remaining > 0:
                    visited[neighbour] = visitedId
                    parents[neighbour] = vertex
                    toCheck.append((neighbour, min(currBottleneck, remaining)))
        
        if not foundPath:
            break

        update_flow(flow, bottleneck, parents, target)
        visitedId += 1
        maxFlow += bottleneck
    
    return maxFlow

if __name__ == "__main__":

    print("######## test 1 ########\n\n")
    
    source = 0
    target = 3
    matrix = edges_to_matrix(graphs.graph30_edges)
    print(edmonds_karp(matrix, source, target))

    print("\n\n######## test 2 ########\n\n")

    source = 9
    target = 10
    matrix = edges_to_matrix(graphs.graph31_edges)
    print(edmonds_karp(matrix, source, target))