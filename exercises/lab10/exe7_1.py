# Zadanie 7. (sklejanie odcinków) Dany jest ciąg przedziałów postaci [a,,b,]. Dwa przedziały można skleić jeśli mają dokładnie 
# jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
# 1. Problem stwierdzenia, czy da się uzyskać przedział [a, b] przez sklejanie odcinków.
# 2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b].
# 3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków.

# AD 1.1) (tylko dla liczb całkowitych) 
# O(n + n*span + span^2), gdzie n - liczba, przedziałów, span jest równy wielkości przedziału <a,b>
# Definiujemy funkcję f(i,b,e) - możliwe jest otrzymanie przedziału <b,e> poprzez sklejenie "i" pierwszych przedziałów.
# W praktyce będziemy przechowywać informację czy można stworzyć przedział <b,e> i na bierząco aktualizować wartości
# w naszej tablicy w kolejnych iteracjach pętli.

def filter_intervals(intervals: list[tuple[int, int]], targetInterval: tuple[int, int]) -> list[tuple[int, int]]:
    beg, end = targetInterval
    return [interval for interval in intervals if interval[0] >= beg and interval[1] <= end]

def is_interval_creatable(intervals: list[tuple[int, int]], targetInterval: tuple[int, int]) -> bool:
    intervals = filter_intervals(intervals, targetInterval)
    n = len(intervals)

    # we scale our data to consider only intervlas <0,e-b> instead of <b,e> for easier data management
    span = targetInterval[1] - targetInterval[0] + 1
    correction = targetInterval[0]

    # we sort intervals by their ends
    intervals.sort(key=lambda x: x[1])

    f = [[False for _ in range(span)] for _ in range(span)]

    for i in range(n):
        beg, end = intervals[i]
        beg -= correction
        end -= correction

        # mark this interval as creatable
        f[beg][end] = True

        # check if we can create interval <prevBeg,end> by marging interval <prevBeg,beg> with <beg,end>
        for prevBeg in range(beg - 1, -1, -1):
            f[prevBeg][end] = f[prevBeg][beg] or f[prevBeg][end]
    
    return f[0][span - 1]

def test(intervals, targetInterval):
    global testId
    testId += 1
    print(f"\n\n######## test {testId} ########\n\n")
    print(f"intervals (sorted):\n{sorted(intervals)}")
    print(f"is interval: {targetInterval} creatable? {is_interval_creatable(intervals, targetInterval)}")


if __name__ == "__main__":
    testId = 0
    targetInterval = (1,5)
    intervals = [(0,3), (1,3), (2,4), (3,4), (4,6)]
    test(intervals, targetInterval)

    intervals = [(0,3), (1,3), (2,4), (3,4), (3,6), (4,5)]
    test(intervals, targetInterval)

    intervals = [(4, 5), (2, 4), (1, 3), (3, 6), (5, 7), (1, 5), (-5, 2)]

    targetInterval = (1, 7)
    test(intervals, targetInterval)

    targetInterval = (2, 5)
    test(intervals, targetInterval)

    targetInterval = (-5, 5)
    test(intervals, targetInterval)

    targetInterval = (0, 2)
    test(intervals, targetInterval)

