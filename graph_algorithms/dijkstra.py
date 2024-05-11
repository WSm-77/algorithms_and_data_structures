# find shortest path from "beg" to every other vertex

from queue import PriorityQueue
import graphs

# G[vertex][neighbourIdx] = (neighbour, cost: vertex -> neighbour)
def dijkstra(G: list[list[tuple[int, int | float]]], beg):
    V = len(G)
    parent = [None]*V
    distance = [float("inf")]*V
    toCheck = PriorityQueue()
    toCheck.put((0, beg))
    distance[beg] = 0

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

def dijkstra_optimized(G: list[list[tuple[int, int | float]]], beg):
    INF = float("inf")
    V = len(G)
    parents = [None]*V
    distances = [INF]*V
    toCheck = PriorityQueue()
    toCheck.put((0, beg, None))
    relaxedCnt = 0

    while not toCheck.empty() and relaxedCnt < V:
        currentDistance, currentVertex, currentParent = toCheck.get()

        if currentDistance < distances[currentVertex]:

            # we update distance only during vertex relaxation
            distances[currentVertex] = currentDistance
            parents[currentVertex] = currentParent

            for neighbour, cost in G[currentVertex]:
                
                # check if we have already relaxed neighbour; if not, add it to priority queue
                if distances[neighbour] == INF:
                    toCheck.put((currentDistance + cost, neighbour, currentVertex))
    
    return distances, parents
    
def dijkstra_matrix(G: list[list[tuple[int, int | float]]], beg):
    V = len(G)
    INF = float("inf")
    distances = [INF]*V
    distances[beg] = 0
    parents = [None]*V
    relaxed = [False]*V

    # we have to relax all verticies only once
    for _ in range(V):

        # find not relaxed vertex with smalest distance to "beg"
        vertexToRelax = None
        minDistance = INF

        for vertex in range(V):
            if not relaxed[vertex] and distances[vertex] < minDistance:
                minDistance = distances[vertex]
                vertexToRelax = vertex
        
        # check if we found any candidate
        if minDistance == INF:
            break

        relaxed[vertexToRelax] = True

        for neighbour in range(V):
            cost = G[vertexToRelax][neighbour]

            # check if edge between vertexToRelax and neighbour exists
            if cost != INF:
                newDistance = distances[vertexToRelax] + cost
                if newDistance < distances[neighbour]:
                    distances[neighbour] = newDistance
                    parents[neighbour] = vertexToRelax

    return distances, parents

def test(start, testGraph):
    V = len(testGraph)
    distance, parents = dijkstra_optimized(testGraph, start)
    print("distances:")
    print(distance)
    for vertex in range(V):
        graphs.print_way(parents, vertex)

    print("\nchecking if distances for every dijkstra algorithms are the same...")
    testResult = "PASSED"
    for vertex in range(V):
        dist1, _ = dijkstra(testGraph, vertex)
        dist2, _ = dijkstra_optimized(testGraph, vertex)
        dist3, _ = dijkstra_matrix(graphs.list_to_weighted_matrix(testGraph), vertex)
        if not (dist1 == dist2 == dist3):
            testResult = "FAILED"
            break
    
    print("test result:", testResult)

if __name__ == "__main__":

    ########## test 1 ##########

    print("########## test 1 ##########\n\n")
    test(0, graphs.graph19_list_weights)


    ########## test 2 ##########

    print("\n\n########## test 2 ##########\n\n")
    test(0, graphs.graph20_list_weights)