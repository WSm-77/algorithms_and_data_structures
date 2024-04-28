# Dana jest macierz K, gdzie element K[x][y] oznacza ile jednostek y otrzymujemy za jednostkę x; sprawdzić czy istnieje taka waluta
# dla której seria zamian powoduje, że mamy więcej pieniędzy na start

# rozwiązanie: zamieniamy wszystkie elementy z tablicy K na ich logarytmy; następnie wykonujemy algorytm Floyda-Warshalla
# przy czym szukamy najdłuższych dróg do danych wierzchołków (stąd zamiana znaku "<" na ">" w algorytmie)

from math import log2

def exchange(K):
    V = len(K)
    distances = [[log2(K[R][C]) for C in range(V)] for R in range(V)]

    for i in range(V):
        for vertex in range(V):
            for neighbour in range(V):
                if distances[vertex][i] + distances[i][neighbour] > distances[vertex][neighbour]:
                    distances[vertex][neighbour] = distances[vertex][i] + distances[i][neighbour]


    cycleStart = None
    for i in range(V):
        for vertex in range(V):
            for neighbour in range(V):
                if distances[vertex][i] + distances[i][neighbour] > distances[vertex][neighbour]:
                    cycleStart = neighbour
                    break

    return cycleStart

def get_cycle(K, beg):
    V = len(K)
    INF = float("inf")
    distances = [-INF]*V
    distances[beg] = 1
    parents = [None]*V

    # we use Bellman-Ford algorithm to get parents, because we know that cycle with negative sum exists
    for _ in range(V - 1):
        for vertex in range(V):
            for neighbour in range(V):
                if distances[vertex] * K[vertex][neighbour] > distances[neighbour]:
                    distances[neighbour] = distances[vertex] * K[vertex][neighbour]
                    parents[neighbour] = vertex

    cycle = [beg]
    ptr = parents[beg]
    while ptr != beg and ptr != None:
        cycle.append(ptr)
        ptr = parents[ptr]
    
    cycle.append(beg)
    cycle.reverse()
    
    return cycle

def calculate_profit(K, cycle):
    money = 1
    for i in range(len(cycle) - 1):
        money *= K[cycle[i]][cycle[i + 1]]
    
    return money - 1


def test(K):
    cycleStart = exchange(K)
    if cycleStart != None:
        print("to get profit you should exchange in this cycle:")
        cycle = get_cycle(K, cycleStart)
        print(*cycle, sep=" -> ")
        print(f"you will make {calculate_profit(K, cycle)}$ profit per cycle")
    else:
        print("you can't make profit")


if __name__ == "__main__":
    print("######### test 1 #########\n\n")

    K1 = [
        [1,   4,   2],
        [0.2, 1,   0.5],
        [0.5, 2, 1]
        ]
    
    test(K1)

    print("\n\n######### test 2 #########\n\n")

    K2 = [
        [1, 0.2,   0.1],
        [3, 1,     0.2],
        [9, 5,     1]
        ]
    
    test(K2)

    print("\n\n######### test 3 #########\n\n")

    K3 = [
        [1,  0.2, 0.1, 1],
        [3,  1,   0.2, 2],
        [9,  5,   1,   4],
        [1,  0.2, 0.1, 1]
        ]
    
    test(K3)
