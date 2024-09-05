from egz2btesty import runtests
from collections import deque

def get_number_of_verticies(edges):
    V = 0
    for vertex, neighbour, _, _ in edges:
        V = max(V, vertex, neighbour)
    return V + 1

def create_graph(edges):
    # graph[vertex][neighbourIdx] = (neighbour, disance, type)
    V = get_number_of_verticies(edges)
    graph = [[] for _ in range(V)]

    for vertex, neighbour, distance, type in edges:
        graph[vertex].append((neighbour, distance, type))
        graph[neighbour].append((vertex, distance, type))

    return graph

def tory_amos( E, A, B ):
    # tu prosze wpisac wlasna implementacje
    INF = float("inf")

    graph = create_graph(E)
    V = len(graph)

    # times[vertex][enterRailType] - minimal travel time if we enter station 'vertex' from rail
    # with type 'enterRailType'
    times = [[INF for _ in range(2)] for _ in range(V)]
    times[A][0] = 0
    times[A][1] = 0
    visited = [[False for _ in range(2)] for _ in range(V)]
    visited[A][0] = True
    visited[A][1] = True

    # toCheck - cnt, time, vertex, prev rail type
    toCheck = deque()

    for neighbour, distance, railType in graph[A]:
        toCheck.append((distance - 1, distance, neighbour, railType))

    while toCheck:
        cnt, time, vertex, prevRailType = toCheck.popleft()
        if 0 < cnt:
            toCheck.append((cnt - 1, time, vertex, prevRailType))
        else:
            prevRailTypeIdx = int(prevRailType == 'I')

            if visited[vertex][prevRailTypeIdx]:
                continue

            visited[vertex][prevRailTypeIdx] = True
            times[vertex][prevRailTypeIdx] = time

            if vertex == B:
                break

            for neighbour, distance, railType in graph[vertex]:
                railTypeIdx = int(railType == 'I')
                if not visited[neighbour][railTypeIdx]:
                    travelTime = distance
                    if prevRailType != railType:
                        travelTime += 20
                    else:
                        if railType == 'I':
                            travelTime += 5
                        else:
                            travelTime += 10
                    newTime = time + travelTime

                    if newTime < times[neighbour][railTypeIdx]:
                        toCheck.append((travelTime - 1, newTime, neighbour, railType))

    return min(times[B])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
