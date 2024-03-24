# Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami. Pojemniki mają kształty prostokątów, rury nie mają objętości (powierzchni). 
# Każdy pojemnik opisany jest przez współrzędne lewego górnego rogu i prawego dolnego rogu. Wiemy, że do pojemników nalano A "powierzchni" wody 
# (oczywiście woda rurami spłynęła do najniższych pojemników). Proszę zaproponować algorytm obliczający ile pojemników zostało w pełni zalanych.

class Bucket:
    def __init__(self, topLeft: tuple, bottomRigth: tuple) -> None:
        self.topLeft = topLeft
        self.bottomRight = bottomRigth

class Event:
    def __init__(self, y: int, width: int, isBottom: bool) -> None:
        self.y = y
        self.width = width
        self.isBottom = isBottom

def quick_sort(tab: list, key) -> None:
    def rek(tab, beg, end, key):
        if beg >= end:
            return
        
        pivot = partition(tab, beg, end, key)
        rek(tab, beg, pivot - 1, key)
        rek(tab, pivot + 1, end, key)
    #end def
    n = len(tab)
    rek(tab, 0, n - 1, key)
    
def partition(tab, beg, end, key):
    pivot = (beg + end) // 2
    if key(tab[beg]) > key(tab[pivot]):
        tab[beg], tab[pivot] = tab[pivot], tab[beg]
    #end if
    if key(tab[pivot]) < key(tab[end]):
        tab[pivot], tab[end] = tab[end], tab[pivot]
    #end if
    pivot = end
    end -= 1
    while beg <= end:
        if key(tab[beg]) <= key(tab[pivot]):
            beg += 1
        elif key(tab[end]) >= key(tab[pivot]):
            end -= 1
        else:
            tab[end], tab[beg] = tab[beg], tab[end]
            beg += 1
            end -= 1
        #end if
    #end while
    tab[beg], tab[pivot] = tab[pivot], tab[beg]
    return beg

def buckets_to_event(tabOfBuckets: list[Bucket]) -> list:
    n = len(tabOfBuckets)
    tabOfEvents = [None for _ in range(2*n)]
    eventId = 0
    for bucket in tabOfBuckets:
        bucketWidth = bucket.bottomRight[0] - bucket.topLeft[0]
        tabOfEvents[eventId] = Event(bucket.bottomRight[1], bucketWidth, True)
        eventId += 1
        tabOfEvents[eventId] = Event(bucket.topLeft[1], bucketWidth, False)
        eventId += 1
    #end for

    return tabOfEvents



def full_buckets(tab: list, waterArea: int) -> int:
    tabOfEvents = buckets_to_event(tab)
    quick_sort(tabOfEvents, lambda event: event.y)

    n = len(tabOfEvents)
    i = 1
    totalWidth = tabOfEvents[0].width
    prev_y = tabOfEvents[0].y
    result = 0
    while i < n:
        currentEvent = tabOfEvents[i]
        current_y = currentEvent.y
        waterArea -= totalWidth*(current_y - prev_y)
        if waterArea < 0:
            break
        if currentEvent.isBottom:
            totalWidth += currentEvent.width
        else:
            result += 1
            totalWidth -= currentEvent.width
        #end if
        prev_y = current_y
        i += 1
    #end while
    return result

if __name__ == "__main__":
    tabOfBuckets = [Bucket((0, i+2), (2, i)) for i in range(10)]
    waterArea = 10
    print(full_buckets(tabOfBuckets, waterArea))