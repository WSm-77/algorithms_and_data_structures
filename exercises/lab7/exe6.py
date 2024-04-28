# Dwóch kierowców (Bob i Alicja)
# Przemieszczamy się z miasta A do miasta B; kierowcy jadą na zmianę; jeden kierowca (Alicja) wybiera trasę oraz kto prowadzi jako pierwszy;
# wyznaczyć taką trasę oraz powiedzieć, który kierowca ma prowadzić, aby wybierający jechał jak najkrócej

# rozwiązanie: zamieniamy ten graf tak, aby zastąpić każdy wierzchołek dwoma: 0 - do wierzchołka przyjechała Alicja,
# 1 - do wierzchołka przyjechał Bob; następnie krawędzie zamieniamy na dwie w podobny sposób

from queue import PriorityQueue

ALICE = 0
BOB = 1

def two_dreviers(G, beg, end):
    V = len(G)
    INF = float("inf")
    distances = [[INF, INF] for _ in range(V)]
    parents = [[None, None] for _ in range(V)]
    # distances[beg][0] = distances[beg][1] = 0
    # 0 - distance, 1 - who is driving while entering city/vertex, 2 - vertex, 3 - parent
    toCheck = PriorityQueue()
    toCheck.put((0, BOB, beg, None))
    toCheck.put((0, ALICE, beg, None))
    visitedCnt = 0

    while not toCheck.empty():
        currentDistance, driver, vertex, currentParent = toCheck.get()
        # print(currentDistance, driver, vertex, currentParent)

        if currentDistance < distances[vertex][driver]:
            parents[vertex][driver] = (currentParent, driver)
            distances[vertex][driver] = currentDistance
            visitedCnt += 1

            if vertex == end:
                break

            correction = 0
            nextDriver = BOB

            if driver == BOB:
                nextDriver = ALICE
                correction = 1

            for neighbour, cost in G[vertex]:
                if distances[neighbour][nextDriver] == INF:
                    toCheck.put((currentDistance + correction*cost, nextDriver, neighbour, vertex))

    path, driver = None, None
    if distances[end][ALICE] < distances[end][BOB]:
        path, driver = get_path_and_driver(parents, ALICE, end)
    else:
        path, driver = get_path_and_driver(parents, BOB, end)

    driverStr = "Alice"
    if driver == BOB:
        driverStr = "Bob"

    return path, driverStr

def get_path_and_driver(parents, lastDriver, end):
    path = [(end, lastDriver)]
    ptr, driver = parents[end][lastDriver]
    driver = int(not driver)

    while ptr != None:
        path.append((ptr, driver))
        ptr, driver = parents[ptr][driver]
        driver = int(not driver)
    # end while
    path.reverse()

    return path, driver

def get_distance_from_vertex_to_neighbour(G, vertex, neighbour):
    distance = 0
    V = len(G)
    for neighbourIdx in range(V):
        if G[vertex][neighbourIdx][0] == neighbour:
            distance = G[vertex][neighbourIdx][1]
            break
    
    return distance

def print_path(G, path: list[tuple[int, int]]):
    for i in range(len(path) - 1):
        driver = "Alice"
        if path[i][1] == ALICE:
            driver = "Bob"
        vertex = path[i][0]
        neighbour = path[i + 1][0]
        print(f"{driver} drives {get_distance_from_vertex_to_neighbour(G, vertex, neighbour)} km from {vertex} to {neighbour}")

def test(testGraph, beg, end):
    path, driver = two_dreviers(testGraph, beg, end)
    print(f"{driver} starts")
    print_path(testGraph, path)

if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    graph27_list_weights = [[(1, 10)],
                            [(0, 10), (2, 1), (3, 1), (4, 10)],
                            [(1, 1), (3, 1)],
                            [(2, 1), (1, 1)],
                            [(1, 10)]]
    
    test(graph27_list_weights, 0, 4)

    print("\n\n######## test 2 ########\n\n")

    graph20_list_weights = [[(1, 1), (2, 2)],
                            [(0, 1), (3, 3), (4, 2)],
                            [(0, 2), (3, 1), (6, 7)],
                            [(1, 3), (2, 1), (5, 2), (7, 3)],
                            [(1, 2), (7, 5)],
                            [(3, 3), (6, 1), (8, 8)],
                            [(2, 7), (5, 1), (8, 4)],
                            [(3, 3), (4, 5), (8, 1)],
                            [(5, 8), (6, 4), (7, 1)]]
    
    test(graph20_list_weights, 0, 6)

    print("\n\n######## test 3 ########\n\n")

    test(graph20_list_weights, 0, 8)




