# Dany jest ciąg przedziłów domknietych [a1, b1], ... , [an, bn]. Proszę zaproponować algorytm, który znajduje taki przedział
# [ai, bi], w którym w całości zawiera się jak najwięcej innych przedziałów.

class Event:
    def __init__(self, val, id, isStart = False) -> None:
        self.val = val
        self.isStart = isStart
        self.id = id

def quick_sort(tabOfEvents: list[Event], beg, end):
    if beg < end:
        pivot = partition(tabOfEvents, beg, end)
        quick_sort(tabOfEvents, beg, pivot - 1)
        quick_sort(tabOfEvents, pivot + 1, end)

def partition(tabOfEvents: list[Event], beg, end):
    i = beg - 1

    for j in range(beg, end):
        if tabOfEvents[j].val < tabOfEvents[end].val:
            i += 1
            tabOfEvents[i], tabOfEvents[j] = tabOfEvents[j], tabOfEvents[i]
        #end if
    #end for
            
    tabOfEvents[end], tabOfEvents[i + 1] = tabOfEvents[i + 1], tabOfEvents[end]
    return i + 1

def find_maximal_interval(tab: list[tuple]) -> tuple:
    n = len(tab)

    tabOfEvents = [0 for _ in range(2*n)]

    # rozbijamy każdy punkt na 2 eventy mające: wartość, informację czy są początkiem czy końcem przedziału oraz id punktu
    for i in range(n):
        tabOfEvents[2*i] = Event(tab[i][0], i, True)
        tabOfEvents[2*i + 1] = Event(tab[i][1], i)
    #end for

    # sortujemy eventy
    quick_sort(tabOfEvents, 0, 2*n - 1)

    # wyznaczmy ile jest punków mających wartość start większą lub równą od punktu o danym id oraz
    # ile jest punktów mających wartość końca mniejszą lub równą od punktud o danym id
    S = [0 for _ in range(n)]
    E = [0 for _ in range(n)]

    startsCnt = n - 1
    endsCnt = 0
    prevStartsCnt = startsCnt
    prevEndsCnt = endsCnt
    prevStartVal = 0
    prevEndVal = 0

    for i in range(2*n):
        currentEvent = tabOfEvents[i]
        if currentEvent.isStart:
            if currentEvent.val == prevStartVal:
                S[currentEvent.id] = prevStartsCnt
            else:
                S[currentEvent.id] = startsCnt
                prevStartsCnt = startsCnt
                prevStartVal = currentEvent.val
            startsCnt -= 1
        else:
            if currentEvent.val == prevEndVal:
                E[currentEvent.id] = prevEndsCnt
            else:
                E[currentEvent.id] = endsCnt
                prevEndsCnt = endsCnt
                prevEndVal = currentEvent.val
            endsCnt += 1
        #end if
    #end for

    # znajdujemy maksymalny przedział oraz ile przedziałów zawiera
    maxIntervalSize = -float("inf")
    maxInterval = None

    for i in range(n):
        currentPseudoSize = S[i] + E[i] - n + 1
        if maxIntervalSize < currentPseudoSize:
            maxInterval = tab[i]
            maxIntervalSize = currentPseudoSize

    return maxInterval, maxIntervalSize

if __name__ == "__main__":
    testTab = [(1, 16), (2, 7), (5, 8), (12, 19), (9, 14), (18, 28), (18, 23), (19, 21), (27, 29)]    # answer: (1, 16)
    print(find_maximal_interval(testTab))