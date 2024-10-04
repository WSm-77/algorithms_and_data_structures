import sys
sys.path.insert(0, "../")
import graphs

def bellman_ford(edges, V, start):
    INF = float("inf")
    parents = [None]*V
    distances = [INF]*V
    distances[start] = 0

    for _ in range(V - 1):
        for vertex, neighbour, cost in edges:
            newDistance = distances[vertex] + cost
            if newDistance < distances[neighbour]:
                distances[neighbour] = newDistance
                parents[neighbour] = vertex

    existsNegativeSumCycle = False
    negativeSumCycle = []

    for vertex, neighbour, cost in edges:
        if distances[vertex] + cost < distances[neighbour]:
            existsNegativeSumCycle = True
            negativeSumCycle = get_negative_sum_cycle(parents, neighbour)
            break

    return existsNegativeSumCycle, distances, parents, negativeSumCycle


def get_negative_sum_cycle(parents, start):
    cycle = [start]
    ptr = parents[start]
    while ptr != start:
        cycle.append(ptr)
        ptr = parents[ptr]
    #end while
    cycle.append(start)

    return cycle

def test(start, testGraph):
    V = graphs.get_number_of_verticies(testGraph)
    existsNegativeSumCycle, distance, parents, negativeSumCycle = bellman_ford(testGraph, V, start)
    print(f"does exist cycle with negative sum? {existsNegativeSumCycle}")
    if not negativeSumCycle:
        print(f"distances: {distance}")
        for vertex in range(V):
            graphs.print_way(parents, vertex)
    else:
        print("cycle with negative sum:")
        print(*negativeSumCycle, sep=" -> ")


if __name__ == "__main__":
    ########## test 1 ##########

    print("test1:")
    test(0, graphs.graph19_edges_weights)

    ########## test 2 ##########

    print("\ntest2:")
    test(0, graphs.graph20_edges_weights)

    ########## test 3 ##########

    print("\ntest3:")
    test(0, graphs.list_to_weighted_edges(graphs.graph19_list_weights_modified2))
