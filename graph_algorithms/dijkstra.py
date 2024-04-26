# find shortest path from "vertex" to every other vertex

from queue import PriorityQueue
import graphs

# G[vertex][neighbourIdx] = (neighbour, cost: vertex -> neighbour)
def dijkstra(G: list[list[tuple[int, int]]], vertex):
    V = len(G)
    parent = [None]*V
    distance = [float("inf")]*V
    toCheck = PriorityQueue()
    toCheck.put((0, vertex))
    distance[vertex] = 0

    while not toCheck.empty():
        currentDistance, currVertex = toCheck.get()
        if currentDistance > distance[currVertex]:
            continue

        for neighbour, cost in G[currVertex]:
            if distance[currVertex] + cost < distance[neighbour]:
                parent[neighbour] = currVertex
                distance[neighbour] = distance[currVertex] + cost
                toCheck.put((distance[neighbour] ,neighbour))
            #end if
        #end for
    #end while

    return distance, parent

def test(start, testGraph):
    distance, parent = dijkstra(testGraph, start)
    print(distance)
    for vertex in range(len(testGraph)):
        graphs.print_way(parent, vertex)

if __name__ == "__main__":

    ########## test 1 ##########

    print("test1:")
    test(0, graphs.graph19_list_weights)


    ########## test 2 ##########

    print("\ntest2:")
    test(0, graphs.graph20_list_weights)