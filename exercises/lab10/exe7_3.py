# Zadanie 7. (sklejanie odcinków) Dany jest ciąg przedziałów postaci [a,,b,]. Dwa przedziały można skleić jeśli mają dokładnie 
# jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
# 1. Problem stwierdzenia, czy da się uzyskać przedział [a, b] przez sklejanie odcinków.
# 2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b].
# 3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków.

# AD 3) (dla liczb rzeczywistych) 
# Rozwiązanie:
# Najpierw mapujemy wartości na wartości z zakresu 0 ~ 2*n - 1, gdzie n jest liczbą przedziałów. Dla tak przygotowanych danych
# wiemy, że największy przedział jaki możemy stworzyć to <0, 2*n-1> (po skorzystaniu z mapy wartości będziemy mogli w łatwy 
# sposób odtworzyć pierwotne krańce przedziału). Definiujemy funkcję f(i,b,e) - minimalna liczba odcinków potrzebna do stworzenia
# przedziału <b,e> wykorzystując i przedziałów o najmniejszej wartości "e" (jeżeli stworzenie takiego przedziału nie jest możliwe
# to funkcja ta przyjmuje wartość wynoszącą nieskończoność). 

def binary_search(tab, beg, end, val):
    while beg <= end:
        mid = (beg + end) // 2
        if tab[mid] < val:
            beg = mid + 1
        else:
            end = mid - 1
    return beg

def real_to_integer_map(values: list[float]):
    valuesLen = len(values)
    values.sort()

    integerMap = [values[0]]

    for i in range(1, valuesLen):
        if values[i] != integerMap[-1]:
            integerMap.append(values[i])

    return integerMap

def map_interavals(intervals: list[list[float]], integerMap: list[float]):
    intervalsLen = len(intervals)
    mapLen = len(integerMap)

    for i in range(intervalsLen):
        intervals[i][0] = binary_search(integerMap, 0, mapLen - 1, intervals[i][0])
        intervals[i][1] = binary_search(integerMap, 0, mapLen - 1, intervals[i][1])

def largest_interval(intervals: list[list[float]], k: int):
    ########## mapping ##########

    values = []
    for interval in intervals:
        values.append(interval[0])
        values.append(interval[1])

    integerMap = real_to_integer_map(values)
    map_interavals(intervals, integerMap)
    
    ########## main ##########

    # sort by end of interval
    intervals.sort(key=lambda x: x[1])
    
    INF = float("inf")
    span = len(integerMap)
    f = [[INF for _ in range(span)] for _ in range(span)]

    maxInterval = [0,0]
    maxIntervalSize = 0

    for interval in intervals:
        beg, end = interval
        f[beg][end] = 1

        # remember to map integer values to real values from original tab
        currentIntervalSize = integerMap[end] - integerMap[beg]
        if maxIntervalSize < currentIntervalSize:
            maxInterval[0] = integerMap[beg]
            maxInterval[1] = integerMap[end]
            maxIntervalSize = currentIntervalSize

        # check if we can create interval <prevBeg, end> by merging <prevBeg, beg> with <beg,end>
        for prevBeg in range(beg - 1, -1, -1):
            if f[prevBeg][beg] + 1 < f[prevBeg][end]:
                f[prevBeg][end] = f[prevBeg][beg] + 1
                currentIntervalSize = integerMap[end] - integerMap[prevBeg]
                if maxIntervalSize < currentIntervalSize and f[prevBeg][end] <= k:
                    maxInterval[0] = integerMap[prevBeg]
                    maxInterval[1] = integerMap[end]
                    maxIntervalSize = currentIntervalSize

    return maxInterval

def test(intervals, k):
    global testId
    print(f"\n\n######## test {testId} ########\n\n")
    print("intervals:")
    for interval in sorted(intervals):
        print(f"<{interval[0]}, {interval[1]}>")
    
    maxInterval = largest_interval(intervals, k)
    print(f"\nlargest interval that can be created by merging at most {k} intervals:")
    print(f"<{maxInterval[0]}, {maxInterval[1]}>")

if __name__ == "__main__":
    testId = 0
    intervals = [[1.2, 5.6], [5.6, 9.3], [-7.9, 1.2], [1.2, 3.5], [1.2, 7.8], [3.5, 5.6], [5.6, 7.8], 
                 [5.6, 6.6], [6.6, 9.3], [7.8, 9.3]]
    
    for k in range(1, 5):
        testId += 1
        testIntervals = [interval[:] for interval in intervals]  
        test(testIntervals, k)

