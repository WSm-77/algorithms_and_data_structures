# Zadanie 7. (sklejanie odcinków) Dany jest ciąg przedziałów postaci [a,,b,]. Dwa przedziały można skleić jeśli mają dokładnie 
# jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
# 1. Problem stwierdzenia, czy da się uzyskać przedział [a, b] przez sklejanie odcinków.
# 2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b].
# 3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków.

# AD 2) (dla liczb rzeczywistych)
# O(n + n*span + span^2), gdzie n - liczba, przedziałów, span jest równy wielkości przedziału <a,b>
# Definiujemy funkcję f(i,b,e) - najmniejszy koszt otrzymania przedziału <b,e> poprzez sklejenie "i" pierwszych przedziałów.
# W praktyce będziemy przechowywać informację o najmniejszym koszcie stworzenia przedziału <b,e> i na bierząco aktualizować wartości
# w naszej tablicy w kolejnych iteracjach pętli. Z uwagi na to, że tym razem mamy doczynienia z liczbami rzeczywistymi, to należy
# najpierw zmapować te wartości rzeczywiste na wartości całkowite, a później analogicznie do podpunktu pierwszego rozwiązujemy zadanie.

def binary_search(tab, beg, end, val):
    while beg <= end:
        mid = (beg + end) // 2
        if tab[mid] < val:
            beg = mid + 1
        else:
            end = mid - 1
    
    return beg

def filter_intervals(intervals, targetInterval):
    beg, end = targetInterval
    return [[interval, cost] for interval, cost in intervals if beg <= interval[0] and interval[1] <= end]

def map_intervals(intervals: list):
    n = len(intervals)
    intervalMap = []
    values = []

    for i in range(n):
        intervalBeg, intervalEnd = intervals[i][0]
        values.append(intervalBeg)
        values.append(intervalEnd)

    values.sort()
    intervalMap.append(values[0])

    for i in range(1, len(values)):
        val = values[i]
        if intervalMap[-1] != val:
            intervalMap.append(val)
    
    return intervalMap

def real_to_intigers_intervals(intervals, intervalsMap):
    intervalsLen = len(intervals)
    mapLen = len(intervalsMap)

    for i in range(intervalsLen):
        intervalBeg, intervalEnd = intervals[i][0]
        newIntervalBeg = binary_search(intervalsMap, 0, mapLen, intervalBeg)
        newIntervalEnd = binary_search(intervalsMap, 0, mapLen, intervalEnd)
        intervals[i][0][0] = newIntervalBeg
        intervals[i][0][1] = newIntervalEnd

# intervals[i] = [interval, cost] = [[intervalBeg, intervalEnd], cost]
def min_merging_cost(intervals: list[list[list[float] | float]], targetInterval: list[float, float]) -> float:
    ############# filtering and mapping #############

    # get rid of unnecessary intervlas
    intervals = filter_intervals(intervals, targetInterval)

    # map real values to integer values
    intervalsMap = map_intervals(intervals)
    mapLen = len(intervalsMap)

    # change real values in original intervals array to their mapped integer values
    real_to_intigers_intervals(intervals, intervalsMap)

    ############# main part of algorithm #############

    # sort intervlas by their ends
    intervals.sort(key=lambda x: x[0][1])

    # prepare matrix for storing function values
    INF = float("inf")
    targetIntervalBeg = binary_search(intervalsMap, 0, mapLen - 1, targetInterval[0])
    targetIntervalEnd = binary_search(intervalsMap, 0, mapLen - 1, targetInterval[1])
    span = targetIntervalEnd - targetIntervalBeg + 1
    minCosts = [[INF for _ in range(span)] for _ in range(span)]

    for interval, cost in intervals:
        beg, end = interval
        minCosts[beg][end] = min(minCosts[beg][end], cost)

        for prevBeg in range(beg - 1, -1, -1):
            if minCosts[prevBeg][beg] != INF:
                minCosts[prevBeg][end] = min(minCosts[prevBeg][end], minCosts[prevBeg][beg] + cost)

    return minCosts[targetIntervalBeg][targetIntervalEnd]

def test(intervals, targetInterval):
    global testId
    testId += 1
    print(f"\n\n######## test {testId} ########\n\n")
    for interval, cost in sorted(intervals, key=lambda x: x[0][0]):
        print(f"interval: <{interval[0]}, {interval[1]}>, cost: {cost}")
    minCost = min_merging_cost(intervals, targetInterval)
    print(f"\nmin cost of createing  <{targetInterval[0]}, {targetInterval[1]}> interval: {round(minCost, 1)}")

if __name__ == "__main__":
    testId = 0
    targetInterval = [3.5, 9.3]
    intervals = [[[1.2, 5.6], 8.0], [[1.2, 7.8], 7.0], [[3.5, 5.6], 2.3], [[5.6, 7.8], 100.0],
           [[6.6, 9.3], 5.1], [[7.8, 9.3], 2.0]]

    # Answer: <3.5, 5.6> + <5.6, 7.8> + <7.8, 9.3> = 2.3 + 100.0 + 2.0 = 104.3
    test(intervals, targetInterval)
    
    targetInterval = [3.5, 9.3]
    intervals = [[[1.2, 5.6], 8.0], [[1.2, 7.8], 7.0], [[3.5, 5.6], 2.3], [[5.6, 7.8], 100.0], 
           [[5.6, 6.6], 8.5], [[6.6, 9.3], 5.1], [[7.8, 9.3], 2.0]]
    
    # Answer: <3.5, 5.6> + <5.6, 6.6> + <6.6, 9.3> = 2.3 + 8.5 + 5.1 = 15.9
    test(intervals, targetInterval)

    intervals = [[[1.2, 5.6], 8.0], [[5.6, 9.3], 8.7], [[-7.9, 1.2], 7.3], [[1.2, 3.5], 5.0], 
                 [[1.2, 7.8], 7.0], [[3.5, 5.6], 2.3], [[5.6, 7.8], 12.3], [[5.6, 6.6], 8.5],
                 [[6.6, 9.3], 5.1], [[7.8, 9.3], 2.0]]

    # Answer: <-7.9, 1.2> + <1.2, 3.5> + <3.5, 5.6> = 7.3 + 5.0 + 2.3 = 14.6
    # Note:
    # We can also create this interval by marging <-7.9, 1.2> + <1.2, 5.6>
    # but we got higher cost: 7.3 + 8.0 = 15.3
    targetInterval = [-7.9, 5.6]
    test(intervals, targetInterval)

    intervals = [[[1.2, 5.6], 8.0], [[5.6, 9.3], 8.7], [[-7.9, 1.2], 7.3], [[1.2, 3.5], 5.0], 
                 [[1.2, 7.8], 7.0], [[3.5, 5.6], 2.3], [[5.6, 7.8], 12.3], [[5.6, 6.6], 8.5],
                 [[6.6, 9.3], 5.1], [[7.8, 9.3], 2.0]]

    # Answer: <-7.9, 1.2> + <1.2, 7.8> + <7.8, 9.3> = 7.3 + 7.0 + 2.0 = 16.3
    # Note:
    # We have mulptile ways to create this interval, but this is the cheapest
    targetInterval = [-7.9, 9.3]
    test(intervals, targetInterval)
    

