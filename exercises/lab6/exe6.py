
# Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami. Każde miasto jest otoczone
# murem i ma tylko dwie bramy północną i południową. Z każdej bramy prowadzi dokładnie jedna droga do jednej oazy
# (ale do danej oazy może dochodzić dowolnie wiele dróg; oazy mogą też być połączone drogami między sobą). Prawo
# Algocji wymaga, że jeśli ktoś wjechał do miasta jedną bramą, to musi go opuścić drugą. Szach Algocji postanowił
# wysłać gońca, który w każdym mieście kraju odczyta zakaz formułowania zadań "o szachownicy" (obraza majestatu).
# Szach chce, żeby goniec odwiedził każde miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą
# z oaz). Goniec wyjeżdża ze stolicji Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę
# przedstawić algorytm, który stwierdza czy odpowiednia trasa gońca istnieje.

# Rozwiązanie:
# Ponieważ miasta mają dokładnie dwa połączenia do dwóch oaz to możemy potraktować miasta jako krawędzie w naszym
# grafie. Ponieważ pomiędzy oazami możemy przechodzić tyle razy ile chcemy to możemy złączyć skupiska połączonych oaz
# w jedną oazę, która będzie naszym wierzhołkiem. Nasz problem sprowadza się wówczas do stwierdzenia czy dany graf
# jest eulerowski.

from collections import deque

def get_number_of_verticies(edges):
    V = 0
    for vertex, neighbour in edges:
        V = max(V, vertex, neighbour)
    return V + 1

def edges_to_graph(edges, V):
    graph = [[] for _ in range(V)]

    for vertex, neighbour in edges:
        graph[vertex].append(neighbour)
        graph[neighbour].append(vertex)

    return graph

def merge_oasis(graph, isCity: list[bool]):
    V = len(graph)
    oldToNewVertexIdx = [None for _ in range(V)]
    newIdx = 0

    toCheck = deque()

    for vertex in range(V):
        # check if vertex is an oasis and hasn't been visited
        if not isCity[vertex] and oldToNewVertexIdx[vertex] == None:
            toCheck.append(vertex)
            oldToNewVertexIdx[vertex] = newIdx
            while toCheck:
                v = toCheck.popleft()

                for neighbour in graph[v]:

                    # check if neighbour is oasis and it hasn't been visited
                    if not isCity[neighbour] and oldToNewVertexIdx[neighbour] == None:
                        oldToNewVertexIdx[neighbour] = newIdx
                        toCheck.append(neighbour)
                #end for
            #end while
            newIdx += 1
        #end if
    #end for

    # Note: newIdx is equal to number of verticies after merge
    return newIdx, oldToNewVertexIdx

def create_new_graph(oldGraph, newV, oldToNewVertexIdx):
    oldV = len(oldGraph)
    newGraph = [[] for _ in range(newV)]

    for oldVertex in range(oldV):

        # check if oldVertex an oasis, if not then we skip it for now
        if oldToNewVertexIdx[oldVertex] == None:
            continue

        newVertex = oldToNewVertexIdx[oldVertex]

        # print("\n###############")
        # print(f"oldVertex: {oldVertex}, newVertex: {newVertex}\n")

        for oldNeighbour in oldGraph[oldVertex]:
            # check if oldNeighbour is a city
            if oldToNewVertexIdx[oldNeighbour] != None:
                continue

            # find second vertex of this edge (second neighbour of city)
            # we know that every city has exactly 2 neighbours (and both of them are oasis)
            oldNeighbourOfCity = oldGraph[oldNeighbour][0] if oldGraph[oldNeighbour][0] != oldVertex else oldGraph[oldNeighbour][1]

            newNeighbour = oldToNewVertexIdx[oldNeighbourOfCity]

            # print(f"oldNeighbour: {oldNeighbour}, oldNeighbourOfCity: {oldNeighbourOfCity}, newNeighbour: {newNeighbour}")

            # we don't have to add loops (edge from vertex to itself e.g. (1,1), (2,2), (v,v)...) to our graph
            if newVertex != newNeighbour:
                newGraph[newVertex].append(newNeighbour)

    return newGraph

def runner(edges, cities) -> bool:
    V = get_number_of_verticies(edges)
    isCity = [False for _ in range(V)]

    for city in cities:
        isCity[city] = True

    oldGraph = edges_to_graph(edges, V)
    newV, oldToNewVertexIdx = merge_oasis(oldGraph, isCity)

    newGraph = create_new_graph(oldGraph, newV, oldToNewVertexIdx)

    # now we only have to check if graph is Eulerian
    for vertex in range(newV):
        if len(newGraph[vertex]) % 2 != 0:
            return False

    return True


if __name__ == "__main__":
    graph28_edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 5), (4, 7), (5, 9), (3, 9), (1, 7), (0, 7), (7, 10), (10, 11),
                    (1, 6), (6, 8)]
    cities = [0, 2, 9, 4, 10, 6]
    print(runner(graph28_edges, cities))

    edges = graph28_edges + [(8, 12), (11, 12)]
    cities = cities + [12]
    print(runner(edges, cities))

    graph29_edges = [(0, 1), (1, 2), (0, 10), (2, 9), (2, 14), (2, 3), (3, 8), (8, 14), (9, 14), (10, 9), (3, 4),
                    (8, 7), (7, 4), (14, 7), (4, 5), (7, 6), (6, 5), (14, 6), (9, 12), (12, 14), (10, 11),
                    (15, 6), (11, 17), (13, 17), (13, 16), (15, 16)]
    cities = [1, 11, 13, 12, 15, 5]
    print(runner(graph29_edges, cities))
