from kol2btesty import runtests
import heapq

class Parking:
    def __init__(self, distance, cost) -> None:
        self.distance = distance
        self.cost = cost

    def __repr__(self) -> str:
        return f"P({self.distance}, {self.cost})"
    
def get_min_cost_and_update_heap(heap, prevDistance):
        mini = heap[0]
        miniCost, miniDistance = mini

        while heap:
            if miniDistance >= prevDistance:
                break
            else:
                heapq.heappop(heap)
                mini = heap[0]
                miniCost, miniDistance = mini
        
        return miniCost

def min_cost( O, C, T, L ):
    # tu prosze wpisac wlasna implementacje

    n = len(O)

    if L <= T:
        return 0

    parkingTab = [Parking(O[i], C[i]) for i in range(n)]
    parkingTab.append(Parking(L, 0))
    parkingTab.append(Parking(0, 0))

    parkingTab.sort(key=lambda x: x.distance)

    n = len(parkingTab)

    # minimalny koszt dotarcia do i-tego parkingu
    f = [None for _ in range(n)]

    # minimalny koszt dotarcia do i-tego parkingu bez korzystania z wyjątku
    g = [None for _ in range(n)]

    # minimalny koszt dotarcia do i-tego parkingu korzystając z wyjątku w ostatnim ruchu
    h = [None for _ in range(n)]

    gHeap = []
    hHeap = []
    fHeap = []

    i = 0
    while i < n and parkingTab[i].distance <= T:
        f[i] = g[i] = h[i] = 0
        gHeap.append((parkingTab[i].cost, parkingTab[i].distance))
        hHeap.append((parkingTab[i].cost, parkingTab[i].distance))
        fHeap.append((parkingTab[i].cost, parkingTab[i].distance))
        i += 1

    heapq.heapify(gHeap)
    heapq.heapify(hHeap)
    heapq.heapify(fHeap)

    for parkingIdx in range(i, n):
        prevDistance = parkingTab[parkingIdx].distance - T
        prevDistanceException = parkingTab[parkingIdx].distance - 2*T

        g[parkingIdx] = get_min_cost_and_update_heap(gHeap, prevDistance)
        h[parkingIdx] = get_min_cost_and_update_heap(hHeap, prevDistanceException)
        f[parkingIdx] = min(get_min_cost_and_update_heap(fHeap, prevDistance), h[parkingIdx])

        heapq.heappush(gHeap, (g[parkingIdx] + parkingTab[parkingIdx].cost, parkingTab[parkingIdx].distance))
        heapq.heappush(hHeap, (g[parkingIdx] + parkingTab[parkingIdx].cost, parkingTab[parkingIdx].distance))
        heapq.heappush(fHeap, (f[parkingIdx] + parkingTab[parkingIdx].cost, parkingTab[parkingIdx].distance))

    return f[-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
