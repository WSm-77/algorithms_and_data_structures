# find shortest path from "vertex" to every other vertex

from queue import PriorityQueue
import graphs

def print_way(parent, vertex):
    def rek(vertex):
        nonlocal parent
        if parent[vertex] == None:
            print(f"{vertex}", end="")
            return
        
        rek(parent[vertex])
        print(f" -> {vertex}", end="")
    #end def
    
    rek(vertex)
    print()

# G[vertex][neighbourIdx] = (neighbour, cost: vertex -> neighbour)
def dijkstra(G: list[list[tuple[int, int]]], vertex):
    V = len(G)
    parent = [None]*V
    distance = [float("inf")]*V
    toCheck = PriorityQueue()
    toCheck.put((0, vertex))
    distance[vertex] = 0

    while not toCheck.empty():
        currDistance, currVertex = toCheck.get()
        if distance[currVertex] < currDistance:
            continue
        #end if

        for neighbour, cost in G[currVertex]:
            if distance[currVertex] + cost < distance[neighbour]:
                parent[neighbour] = currVertex
                distance[neighbour] = distance[currVertex] + cost
                toCheck.put((distance[neighbour], neighbour))
            #end if
        #end for
    #end while

    return distance, parent

if __name__ == "__main__":

    ########## test 1 ##########
    
    print("test1:")
    start = 0
    testGraph = graphs.graph19_list_weights
    distance, parent = dijkstra(testGraph, start)
    print(distance)
    for vertex in range(len(testGraph)):
        print_way(parent, vertex)


    ########## test 2 ##########
    
    print("\ntest2:")
    start = 0
    testGraph = graphs.graph20_list_weights
    distance, parent = dijkstra(testGraph, start)
    print(distance)
    for vertex in range(len(testGraph)):
        print_way(parent, vertex)