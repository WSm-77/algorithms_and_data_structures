# Opis algorytmu:
# Zamieniamy otrzymaną tablicę na tablicę zawierającą wyłącznie punkty przesiadkowe, dla których mamy zapisane: dystans
# od punktu A (w tym algorytmie nie jest on wykorzystywany), liczbę punktów kontrolnych od ostataniego punktu przesiadkowego 
# oraz indeks w oryginalnej tablicy. Nowa talica jest posortowana po dystansach od punktu A. Następnie tworzymy dwie tablice:
# 1) marian[i][z] - minimalna liczba punktów kontrolnych, które jako kierowca minął Marian, przy założeniu że to Marian 
# wyjeżdża z i-tego punktu nie zmieniając się z Jackiem od "e" punktów 
# 2) jacek[i][z] - minimalna liczba punktów kontrolnych, które jako kierowca minął Marian, przy założeniu że to Jacek 
# wyjeżdża z i-tego punktu nie zmieniając się z Marianem od "e" punktów
# W ten sposób jesteśmy w stanie śledzić najlepszą trasę przejazdu. Trasę przejazdu odtworzymy korzystając z tablic 
# "marianParents" oraz "jacekParents", w których będziemy zapisywali przy jakim poziomie wyczerpania prowadził poprzedni 
# kierowca wyjeżdżając z poprzedniego punktu przesiadkowego (to kto prowadził będzie obliczane na podstawie poziomu wyczerpania).
# 
# Złożoność obliczeniowa:
# O(n log n) - posortowanie n punktów a następnie kilka liniowych przejść po tablicy

from kol2atesty import runtests

class SwitchPoint:
    def __init__(self, dist, controlPoints, idx) -> None:
        self.dist = dist
        self.controlPoints = controlPoints
        self.idx = idx

    def __repr__(self) -> str:
        return f"Sp(d:{self.dist},cp:{self.controlPoints},i:{self.idx})"

def create_switch_points_array(points):
    spArray = []
    controlPointsCnt = 0
    for idx, point in points:
        dist, isSp = point
        if isSp:
            spArray.append(SwitchPoint(dist, controlPointsCnt, idx))
            controlPointsCnt = 0
        else:
            controlPointsCnt += 1
    
    return spArray

def get_switch_points(spArray: list[SwitchPoint], marianParents, jacekParents, idx, withoutRest, isMarianDriver):
    switchArray = []
    parentsTab = marianParents
    alternateParentsTab = jacekParents
    if not isMarianDriver:
        parentsTab, alternateParentsTab = alternateParentsTab, parentsTab

    # miasto B traktujemy jak punkt przesiadkowy, ale nie może się on znaleźć w wynikowej tablicy 
    newIdx = idx - 1
    newWithoutRest = parentsTab[idx][withoutRest]

    if withoutRest <= newWithoutRest:
        parentsTab, alternateParentsTab = alternateParentsTab, parentsTab
    
    idx = newIdx
    withoutRest = newWithoutRest

    while idx >= 0:
        newIdx = idx - 1
        newWithoutRest = parentsTab[idx][withoutRest]

        if withoutRest <= newWithoutRest:
            switchArray.append(spArray[idx].idx)
            parentsTab, alternateParentsTab = alternateParentsTab, parentsTab
        
        idx = newIdx
        withoutRest = newWithoutRest
    
    switchArray.reverse()

    return switchArray

def drivers( P, B ):
    # tu prosze wpisac wlasna implementacje

    n = len(P)
    P = [(i, P[i]) for i in range(n)]

    P.sort(key=lambda x: x[1][0])

    P.append((n, (B, True)))

    spArray: list[SwitchPoint] = create_switch_points_array(P)
    spArrayLen = len(spArray)

    EXHAUSTMENT_LEVELS = 3
    INF = float("inf")
    marianParents = [[-1 for _ in range(EXHAUSTMENT_LEVELS)] for _ in range(spArrayLen)]
    marian = [[INF for _ in range(EXHAUSTMENT_LEVELS)] for _ in range(spArrayLen)]

    jacekParents = [[-1 for _ in range(EXHAUSTMENT_LEVELS)] for _ in range(spArrayLen)]
    jacek = [[INF for _ in range(EXHAUSTMENT_LEVELS)] for _ in range(spArrayLen)]

    jacek[0][1] = 0
    marian[0][0] = 0
    marianParents[0][0] = 0

    for i in range(1, spArrayLen):
        # zmieniają się; zmęczenie się resetuje
        for withoutRest in range(EXHAUSTMENT_LEVELS):
            if jacek[i - 1][withoutRest] < marian[i][0]:
                marianParents[i][0] = withoutRest
                marian[i][0] = jacek[i - 1][withoutRest]

            if marian[i - 1][withoutRest] + spArray[i].controlPoints < jacek[i][0]:
                jacekParents[i][0] = withoutRest
                jacek[i][0] = marian[i - 1][withoutRest] + spArray[i].controlPoints

        # kontynuują jazdę
        for withoutRest in range(1, EXHAUSTMENT_LEVELS):
            marianParents[i][withoutRest] = withoutRest - 1
            marian[i][withoutRest] = marian[i - 1][withoutRest - 1] + spArray[i].controlPoints

            jacekParents[i][withoutRest] = withoutRest - 1
            jacek[i][withoutRest] = jacek[i - 1][withoutRest - 1]

    minCp = INF
    isMarianLastDriver = None
    lastWithoutRest = None
    for withoutRest in range(EXHAUSTMENT_LEVELS):
        if marian[spArrayLen - 1][withoutRest] < minCp:
            minCp = marian[spArrayLen - 1][withoutRest]
            isMarianLastDriver = True
            lastWithoutRest = withoutRest
        if jacek[spArrayLen - 1][withoutRest] < minCp:
            minCp = jacek[spArrayLen - 1][withoutRest]
            isMarianLastDriver = False
            lastWithoutRest = withoutRest

    return get_switch_points(spArray, marianParents, jacekParents, spArrayLen - 1, lastWithoutRest, isMarianLastDriver)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )
# P = [(1, False), (3, False), (4, False), (6, False), (8, False), (9, False), (11, False), (13, False), (16, False), (17, False), (2, True), (5, True), (7, True), (10, True), (12, True), (14, True), (15, True), (18, True)]
# print(drivers(P, 20))
