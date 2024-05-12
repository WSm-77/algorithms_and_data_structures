
# Zadanie 5. (autostrady) W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta siecią autostrad,
# tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na którym leży państwo jest płaski położenie każdego
# z miast opisują dwie liczby x, y, a odległość w linii prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem
# len = sqrt((x1 − x2)^2 + (y1 − y2)^2). Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej. Ponieważ zbliżają
# się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie i jako cel postanowiono zminimalizować czas pomiędzy otwarciem
# pierwszej i ostatniej autostrady. Czas budowy autostrady wyrażony w dniach wynosi [len] (sufit z długości autostrady wyrażonej w km).
# Proszę zaproponować algorytm wyznaczający minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady.

# Wykonujemy algortym kraskala dla grafu pełnego, następnie usuwamy krawędź o minimalnym koszcie i znowu wykonujemy algorytm krasksala.
# Powtarzamy proces usuwania krawędzi i w ten sposób znajdziemy szukane drzewo.

from math import sqrt, ceil

class FindUnion:
    def __init__(self, V):
        self.representants = [i for i in range(V)]
        self.ranks = [0 for _ in range(V)]

    def find(self, ele):
        if self.representants[ele] != ele:
            self.representants[ele] = self.find(self.representants[ele])

        return self.representants[ele]

    def union(self, ele1, ele2):
        repr1 = self.find(ele1)
        repr2 = self.find(ele2)

        if repr1 == repr2:
            return

        if self.ranks[repr1] < self.ranks[repr2]:
            self.representants[repr1] = repr2
        else:
            self.representants[repr2] = repr1
            if self.ranks[repr1] == self.ranks[repr2]:
                self.ranks[repr1] += 1

    def reset(self):
        V = len(self.representants)

        for vertex in range(V):
            self.representants[vertex] = vertex
            self.ranks[vertex] = 0

    def __repr__(self) -> str:
        return f"FindUnion({self.representants})"
# FindUnion

def cities_to_graph(cities):
    V = len(cities)

    G = [[] for _ in range(V)]

    for vertex in range(V):
        x1, x2 = cities[vertex]
        for neighbour in range(vertex + 1, V):
            y1, y2 = cities[neighbour]
            d = ceil(sqrt((x1 - x2)**2 + (y1 - y2)**2))
            G[vertex].append((neighbour, d))
            G[neighbour].append((vertex, d))

    return G

def print_graph(graph):
    V = len(graph)
    for vertex in range(V):
        print(f"# {vertex}", end="")
        for neighbour, cost in graph[vertex]:
            print(f" ({neighbour}, ", end="")
            print("%.2f" % cost, end=")")
        print()

def cities_to_edges(cities):
    V = len(cities)

    edges = []

    for vertex in range(V - 1):
        x1, y1 = cities[vertex]
        for neighbour in range(vertex + 1, V):
            x2, y2 = cities[neighbour]
            time = ceil(sqrt((x1 - x2)**2 + (y1 - y2)**2))
            edges.append((vertex, neighbour, time))

    return edges

def highway(cities: list[tuple[int, int]]) -> int:
    INF = float("inf")
    V = len(cities)
    highways = cities_to_edges(cities)
    E = len(highways)
    highways.sort(key=lambda x: x[2])
    minSpan = INF
    MST = []
    sets = FindUnion(V)

    for i in range(E - V + 2):
        sets.reset()
        minCost = highways[i][2]
        maxCost = minCost
        edgesInTree = 0
        currentTree = []
        for j in range(i, E):
            vertex, neighbour, cost = highways[j]
            if sets.find(vertex) != sets.find(neighbour):
                maxCost = cost
                sets.union(vertex, neighbour)
                edgesInTree += 1
                currentTree.append((vertex, neighbour, cost))

        # check if we can create a tree
        if edgesInTree != V - 1:
            break

        newSpan = maxCost - minCost

        if newSpan < minSpan:
            MST = currentTree
            minSpan = newSpan

    return minSpan, MST

if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    cities = [(4, 4), (2, 3), (4.5, 0), (0, 0), (1, -1), (3, -2), (2, -4), (-1, 2), (-2, -2), (-4, 4), (-5, 0)]
    minSpan, MST = highway(cities)
    print(f"minSpan: {minSpan}")
    print(f"MST: {MST}")

    print("\n\n######## test 2 ########\n\n")

    cities = [(5, 5), (3, -5), (0, 3), (-5, 0)]
    minSpan, MST = highway(cities)
    print(f"minSpan: {minSpan}")
    print(f"MST: {MST}")