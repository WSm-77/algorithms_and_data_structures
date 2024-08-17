# Wiktor Sędzimir
# 
# Opis algorytmu:
# Dla każdego wierzchołka rozważamy minimalny dystans, który należy przebyć, aby znaleźć się w danym wierzchołku,
# przy uwzględnieniu, czy do wirzchołka wchodzimy wykorzystując dwumilowe buty czy też nie (rozróżniamy to w tablicy
# distances). Do kolejki priorytetowej dodajemy dodatkowe informacje o poprzednim koszcie podróży, dystansie poprzedniego
# wierzchołka oraz czy do dotarcia do poprzedniego wierzchołka skorzystano z butów, po to aby móc rozważać kiedy warto
# użyć dwumilowych butów. Algorytm ma złożoność O(E log V), ponieważ korzysta z algorymu dijkstry dla reprezentacji 
# wykorzystującje listę sąsiedztwa.

from zad6testy import runtests
from queue import PriorityQueue

# definicja stałej globalnej
INF = float("inf")

def matrix_to_list(G):
    V = len(G)
    graph = [[] for _ in range(V)]

    for vertex in range(V):
        for neighbour in range(V):
            cost = G[vertex][neighbour]
            if cost > 0:
                graph[vertex].append((neighbour, cost))

    return graph

def jumper( G, s, w ):
    # tu prosze wpisac wlasna implementacje

    V = len(G)

    # distances[i][0] - dystans przebyty do i-tego wierzchołka bez używania dwumilowych butów w poprzednim skoku
    # distances[i][1] - dystans przebyty do i-tego wierzchołka z użyciem dwumilowych butów w poprzednim skoku
    distances = [[INF, INF] for _ in range(V)]
    distances[s][1] = 0
    toCheck = PriorityQueue()
    toCheck.put((0, s, 0, INF, INF, 1))

    G = matrix_to_list(G)

    while not toCheck.empty():
        currentDistance, minVertex, bootsUsage, prevDistance, prevCost, prevBootsUsage = toCheck.get()

        if currentDistance < distances[minVertex][bootsUsage]:
            distances[minVertex][bootsUsage] = currentDistance
            for neighbourIdx in range(len(G[minVertex])):
                neighbour, travelCost = G[minVertex][neighbourIdx]
                newDistance = currentDistance + travelCost
                if newDistance < distances[neighbour][0]:
                    toCheck.put((newDistance, neighbour, 0, currentDistance, travelCost, bootsUsage))

        if not bootsUsage and not prevBootsUsage:
            for neighbourIdx in range(len(G[minVertex])):
                neighbour, travelCost = G[minVertex][neighbourIdx]
                bootsTravelCost = max(travelCost, prevCost)
                bootsNewDistance = prevDistance + bootsTravelCost
                if bootsNewDistance < distances[neighbour][1]:
                    toCheck.put((bootsNewDistance, neighbour, 1, INF, INF, 0))


    return min(distances[w][0], distances[w][1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )