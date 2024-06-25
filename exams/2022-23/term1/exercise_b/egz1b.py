from egz1btesty import runtests

def planets( D, C, T, E ):
    # tu prosze wpisac wlasna implementacje

    n = len(D)
    INF = float("inf")

    f = [[INF for _ in range(E+1)] for _ in range(n)]

    # fueling at first planet
    for fuel in range(E+1):
        f[0][fuel] = fuel*C[0]
    
    # teleport form first planet
    nextPlanet, teleportCost = T[0]
    f[nextPlanet][0] = teleportCost

    for currPlanet in range(1, n):
        distToCurr = D[currPlanet] - D[currPlanet - 1]
        
        f[currPlanet][0] = min(f[currPlanet][0], f[currPlanet - 1][distToCurr])
        for prevFuel in range(distToCurr + 1, E+1):
            currFuel = prevFuel - distToCurr
            f[currPlanet][currFuel] = f[currPlanet - 1][prevFuel]

        # refueling
        for fuel in range(1, E+1):
            f[currPlanet][fuel] = min(f[currPlanet][fuel], f[currPlanet][fuel - 1] + C[currPlanet])

        nextPlanet, teleportCost = T[currPlanet]
        if nextPlanet != currPlanet:
            f[nextPlanet][0] = min(f[nextPlanet][0], f[currPlanet][0] + teleportCost)

    return min(f[n - 1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )

