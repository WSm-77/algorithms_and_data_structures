import sys
sys.path.insert(0, "../")
import graphs

INF = float("inf")

def push_relable(graph, source, target):
    def elevate():
        nonlocal graph, source, target, flow, vertexLevel, vertexOverflow
        elevated = False
        for vertex in range(V):
            if vertex == source or vertex == target or vertexOverflow == 0:
                continue

            minNeighbourLevel = INF
            canBeElevated = True
            for neighbour in range(V):
                if graph[vertex][neighbour] == 0:
                    continue

                minNeighbourLevel = min(minNeighbourLevel, vertexLevel[neighbour])
                if minNeighbourLevel < vertexLevel[vertex]:
                    canBeElevated = False
                    break

            if canBeElevated:
                vertexLevel[vertex] = minNeighbourLevel + 1
                elevated = True
                break

        return elevated
    # end def
    def pour():
        nonlocal graph, source, target, flow, vertexLevel, vertexOverflow
        poured = False
        for vertex in range(V):
            if vertexOverflow[vertex] == 0 or vertex == target or vertex == source:
                continue
            for neighbour in range(V):
                bandwidth = graph[vertex][neighbour] - flow[vertex][neighbour]
                if bandwidth == 0 or vertexLevel[vertex] != vertexLevel[neighbour] + 1:
                    continue

                pouredAmount = min(bandwidth, vertexOverflow[vertex])
                vertexOverflow[neighbour] += pouredAmount
                vertexOverflow[vertex] -= pouredAmount
                flow[vertex][neighbour] += pouredAmount
                flow[neighbour][vertex] -= pouredAmount
                poured = True

            if poured:
                break

        return poured
    #end def

    V = len(graph)
    vertexLevel = [0 for _ in range(V)]
    vertexOverflow = [0 for _ in range(V)]
    flow = [[0 for _ in range(V)] for _ in range(V)]

    # initialize level and overflow
    vertexLevel[source] = V
    for sourceNeighbour in range(V):
        edgeFlow = graph[source][sourceNeighbour]
        if edgeFlow > 0:
            vertexOverflow[sourceNeighbour] = edgeFlow
            flow[source][sourceNeighbour] = edgeFlow
            flow[sourceNeighbour][source] = -edgeFlow

    # find max flow
    while elevate() or pour():
        pass

    # print(vertexLevel)
    # print()
    # print(vertexOverflow)
    # print()
    # print_matrix(flow)

    return vertexOverflow[target]


def edges_to_matrix(E):
    V = graphs.get_number_of_verticies(E)
    matrix = [[0 for _ in range(V)] for _ in range(V)]

    for vertex, neighbour, cost in E:
        matrix[vertex][neighbour] = cost
        matrix[neighbour][vertex] = cost

    return matrix

def print_matrix(matrix):
    print(*matrix, sep="\n")

if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    source = 0
    target = 3
    matrix = edges_to_matrix(graphs.graph32_edges)
    print(push_relable(matrix, source, target))

    print("\n\n######## test 2 ########\n\n")

    source = 0
    target = 3
    matrix = edges_to_matrix(graphs.graph30_edges)
    print(push_relable(matrix, source, target))

    print("\n\n######## test 3 ########\n\n")

    source = 9
    target = 10
    matrix = edges_to_matrix(graphs.graph31_edges)
    print(push_relable(matrix, source, target))
