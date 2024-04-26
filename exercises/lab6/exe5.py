# Problem stacji benzynowych na grafie:
#
# Pewien podróżnik chce przebyć trasę z punktu A do punktu B. Niestety jego samochód spala dokładnie jeden litr 
# paliwa na jeden kilometr trasy. W baku mieści się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, 
# gdzie wierzchołki to miasta a krawędzie to łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną
# jako licza naturalna). W każdym wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm 
# znajdujący trasę z punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.

# Rozwiązanie:
# Dla każdego wierzchołka wyznaczamy najmniejszy koszt dotarcia przy danej ilości paliwa. Każdy wierzchołek traktuejmy
# jako zbiór wierzchołków o liczności równej: pojemność baku paliwa + 1

from queue import PriorityQueue

def min_cost(G: list[list[int]], fuelPrice: list, fuelTankCapacity: int, beg: int, end: int, startFuel = 0):
    V = len(G)
    INF = float("inf")
    cost = [[INF for _ in range(fuelTankCapacity + 1)] for _ in range(V)]
    parent = [[None for _ in range(fuelTankCapacity + 1)] for _ in range(V)]
    toCheck = PriorityQueue()       # t[0] - cost, t[1] - fuel in fuel tank, t[2] - vertex/city 
    toCheck.put((0, startFuel, beg))
    for i in range(fuelTankCapacity + 1):
        cost[beg][i] = 0

    while not toCheck.empty():
        currentCost, currentFuelLevel, currentVertex = toCheck.get()

        if currentVertex == end:
            break

        for neighbour, distance in G[currentVertex]:
            for newFuelLevel in range(max(currentFuelLevel, distance), fuelTankCapacity + 1):
                fuelingCost = (newFuelLevel - currentFuelLevel)*fuelPrice[currentVertex]
                fuelLevelInNextCity = newFuelLevel - distance
                newCost = currentCost + fuelingCost
                if newCost < cost[neighbour][fuelLevelInNextCity]:
                    cost[neighbour][fuelLevelInNextCity] = newCost
                    parent[neighbour][fuelLevelInNextCity] = (currentVertex, currentFuelLevel)
                    toCheck.put((newCost, fuelLevelInNextCity, neighbour))
    # end while

    print_path(parent, end, cost, fuelPrice, 0)

    return cost[end][0]

def print_path(parent, vertex, cost, fuelPrice, fuelLevel):
    def rek(vertex, fuelLevel, prevCost):
        toSpend = prevCost - cost[vertex][fuelLevel]
        boughtFuelAmount = toSpend // fuelPrice[vertex]
        if parent[vertex][fuelLevel] == None:
            print(f"at {vertex} with {fuelLevel}l buy {boughtFuelAmount}l for {toSpend}$", end="")
        else:
            rek(*parent[vertex][fuelLevel], cost[vertex][fuelLevel])
            print(f"\nat {vertex} with {fuelLevel}l buy {boughtFuelAmount}l for {toSpend}$", end="")
    
    rek(vertex, fuelLevel, cost[vertex][fuelLevel])
    print()


if __name__ == "__main__":

    ####### test 1 #######

    graph23_list = [[(1, 5), (2, 7)],
                    [(0, 5), (2, 3)],
                    [(1, 3), (0, 7), (3, 4)],
                    [(2, 4), (4, 6)],
                    [(3, 6)]]
    
    fuelPrice = [8, 5, 3, 2, 1]
    fuelTankCapacity = 10
    beg = 0
    end = 4

    print("test1:")
    print(min_cost(graph23_list, fuelPrice, fuelTankCapacity, beg, end))

    ####### test 2 #######

    graph24_list = [[(1, 4), (7, 5), (6, 8)],
                    [(0, 4), (6, 6), (2, 15)],
                    [(1, 15), (5, 17), (4, 10), (3, 5)],
                    [(2, 5), (4, 18)],
                    [(8, 9), (5, 7), (2, 10), (3, 18)],
                    [(6, 12), (4, 7), (2, 17)],
                    [(0, 8), (7, 3), (1, 6), (5, 12)],
                    [(0, 5), (6, 3), (8, 20)],
                    [(7, 20), (4, 9)]]

    fuelPrice = [5, 7, 3, 5, 2, 1, 8, 10, 6]
    fuelTankCapacity = 14
    beg = 0
    end = 3

    print("\ntest2:")
    print(min_cost(graph24_list, fuelPrice, fuelTankCapacity, beg, end, 5))
        