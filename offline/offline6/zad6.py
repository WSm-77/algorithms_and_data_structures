from zad6testy import runtests

# definicja stałej globalnej
INF = float("inf")

def find_not_visited_min_distance(distances, visited, V):
    minDistance = INF
    minVertex = None
    usedBootsInPreviousJump = 0

    for vertex in range(V):
        if not visited[vertex][0] and distances[vertex][0] < minDistance:
            minDistance = distances[vertex][0]
            minVertex = vertex
            usedBootsInPreviousJump = 0

        if not visited[vertex][1] and distances[vertex][1] < minDistance:
            minDistance = distances[vertex][1]
            minVertex = vertex
            usedBootsInPreviousJump = 1
    
    return minDistance, minVertex, usedBootsInPreviousJump

def jumper( G, s, w ):
    # tu prosze wpisac wlasna implementacje

    V = len(G)

    # distances[i][0] - dystans przebyty do i-tego wierzchołka bez używania dwumilowych butów w poprzednim skoku
    # distances[i][1] - dystans przebyty do i-tego wierzchołka z użyciem dwumilowych butów w poprzednim skoku
    distances = [[INF, INF] for _ in range(V)]
    visited = [[False, False] for _ in range(V)]
    distances[s][0] = 0
    distances[s][1] = 0
    visited[s][1] = True

    print(*G, sep = "\n")

    # wykonujemy tę pętlę 2*V - 1 razy, ponieważ musimy uzupełnić wszystkie elementy tablicy ditances z wyjątkiem distances[s][1]
    for _ in range(2*V - 1):
        currentDistance, minVertex, usedBootsInPreviousJump = find_not_visited_min_distance(distances, visited, V)

        if currentDistance == INF:
            break

        visited[minVertex][usedBootsInPreviousJump] = True

        for neighbour in range(V):
            travelCost = G[minVertex][neighbour]

            if travelCost > 0 and currentDistance + travelCost < distances[neighbour][0]:
                distances[neighbour][0] = currentDistance + travelCost
            
            # boots usage
            if not usedBootsInPreviousJump:
                for neighbourOfNeighbour in range(V):
                    travelCost = max(travelCost, G[neighbour][neighbourOfNeighbour])

                    if G[neighbour][neighbourOfNeighbour] > 0 and currentDistance + travelCost < distances[neighbourOfNeighbour][1]:
                        distances[neighbourOfNeighbour][1] = currentDistance + travelCost
    
    print(distances)
    print(visited)


    return min(distances[w][0], distances[w][1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = False )