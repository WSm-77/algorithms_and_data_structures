from kol2btesty import runtests

class Parking:
    def __init__(self, distance, cost) -> None:
        self.distance = distance
        self.cost = cost

    def __repr__(self) -> str:
        return f"P({self.distance}, {self.cost})"

def min_cost( O, C, T, L ):
    # tu prosze wpisac wlasna implementacje

    n = len(O)
    INF = float("inf")

    if L <= T:
        return 0

    parkingTab = [Parking(O[i], C[i]) for i in range(n)]
    parkingTab.append(Parking(L, 0))
    parkingTab.sort(key=lambda x: x.distance)

    n = len(parkingTab)

    # minimalny koszt dotarcia do i-tego parkingu
    f = [None for _ in range(n)]

    # minimalny koszt dotarcia do i-tego parkingu bez korzystania z wyjątku
    g = [None for _ in range(n)]

    # minimalny koszt dotarcia do i-tego parkingu korzystając z wyjątku w ostatnim ruchu
    h = [None for _ in range(n)]

    i = 0
    while i < n and parkingTab[i].distance <= T:
        f[i] = g[i] = h[i] = 0
        i += 1

    for parkingIdx in range(i, n):
        prevParkingIdx = parkingIdx - 1

        # parkings in range {1,..,T}
        prevDistance = parkingTab[parkingIdx].distance - T
        gMini = INF
        hMini = INF
        fMini = INF
        while 0 <= prevParkingIdx and  parkingTab[prevParkingIdx].distance >= prevDistance:
            gMini = min(gMini, g[prevParkingIdx] + parkingTab[prevParkingIdx].cost)
            hMini = min(hMini, g[prevParkingIdx] + parkingTab[prevParkingIdx].cost)
            fMini = min(fMini, f[prevParkingIdx] + parkingTab[prevParkingIdx].cost)
            prevParkingIdx -= 1
        g[parkingIdx] = gMini

        # parkings in range {T,..,2T}
        prevDistance = parkingTab[parkingIdx].distance - 2*T
        if prevDistance < 0:
            hMini = 0
        else:
            while 0 <= prevParkingIdx and parkingTab[prevParkingIdx].distance >= prevDistance:
                hMini = min(hMini, g[prevParkingIdx] + parkingTab[prevParkingIdx].cost)
                prevParkingIdx -= 1
        
        h[parkingIdx] = hMini
        f[parkingIdx] = min(fMini, hMini)

    return f[-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
