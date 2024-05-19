# Wiktor Sędzimir
#
# Opis algorytmu:
# Algorytm polega na potraktowaniu przedziałów jako wierzchołków pewnego nieskierowanego grafu, w którym krawędź pomiędzy
# dwoma wirzchołkiami istnieje tylko wtedy gdy dane przedziały mają dokładnie jeden punkt wspólny. Następnie w takim grafie
# korzystamy dwukrotnie z algorytmu dfs, aby określić do których wierzchołków zadanego grafu możemy dotrzeć startując od 
# wierzchołków, dla których początek przedziału stanowi liczba x, a następnie startując od wierzchołków, dla których koniec
# przedziału stanowi liczba y. Aby osiągnąć złożoność O(n log n), nie tworzymy grafu, tylko na bieżąco szukamy połączeń
# pomiędzy werzchołkami korzystając z binary searcha.


from zad1testy import runtests

class TabElem:
    def __init__(self, intervalStart, intervalEnd, idx) -> None:
        self.intervalStart = intervalStart
        self.intervalEnd = intervalEnd
        self.idx = idx

    def __repr__(self) -> str:
        return f"elem({self.intervalStart}, {self.intervalEnd}, {self.idx})"

def binary_search(tab: list, elem, key):
    beg = 0
    end = len(tab) - 1

    while beg <= end:
        mid = (beg + end) // 2
        if key(tab[mid]) < elem:
            beg = mid + 1
        else:
            end = mid - 1

    return beg

def intuse( I, x, y ):
    """tu prosze wpisac wlasna implementacje"""
    def dfs_from_start(currentIndex: int):
        nonlocal I, xVisited, n, x, y
        xVisited[I[currentIndex].idx] = True

        if I[currentIndex].intervalEnd > y:
            return

        neighbourIdx = binary_search(I, I[currentIndex].intervalEnd, lambda x: x.intervalStart)

        while neighbourIdx < n and I[neighbourIdx].intervalStart == I[currentIndex].intervalEnd:
            if not xVisited[I[neighbourIdx].idx]:
                dfs_from_start(neighbourIdx)
            neighbourIdx += 1
        #end while
    #end def

    def dfs_from_end(currentIndex: int):
        nonlocal I, yVisited, n, x, y
        yVisited[I[currentIndex].idx] = True

        if I[currentIndex].intervalStart < x:
            return

        neighbourIdx = binary_search(I, I[currentIndex].intervalStart, lambda x: x.intervalEnd)

        while neighbourIdx < n and I[neighbourIdx].intervalEnd == I[currentIndex].intervalStart:
            if not yVisited[I[neighbourIdx].idx]:
                dfs_from_end(neighbourIdx)
            neighbourIdx += 1
        #end while
    #end def

    n = len(I)
    I = [TabElem(*I[i], i) for i in range(n)]

    # reachable verticies from x
    I.sort(key=lambda x: x.intervalStart)
    beg = binary_search(I, x, lambda x: x.intervalStart)
    xVisited = [False for _ in range(n)]


    while beg < n and I[beg].intervalStart == x:
        if not xVisited[I[beg].idx]:
            dfs_from_start(beg)
        beg += 1
    #end while

    # reachable verticies from y
    I.sort(key=lambda x: x.intervalEnd)

    end = binary_search(I, y, lambda x: x.intervalEnd)
    yVisited = [False for _ in range(n)]

    while end < n and I[end].intervalEnd == y:
        if not yVisited[I[end].idx]:
            dfs_from_end(end)
        end += 1
    #end while

    return [i for i in range(n) if xVisited[i] and yVisited[i]]
    
runtests( intuse )

