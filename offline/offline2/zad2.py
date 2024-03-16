# Wiktor Sędzimir
#
# Opis:
#
# uzupełnić
#

from zad2testy import runtests

class HeapElement:
    def __init__(self, val: int, indexInOriginalTab: int) -> None:
        self.val = val
        self.indexInOriginalTab = indexInOriginalTab

class HeapMap:
    def __init__(self, heapId: int, indexInHeap: int) -> None:
        self.heapId = heapId
        self.indexInHeap = indexInHeap

def parent_index(i):
    return (i - 1) // 2

def left_index(i):
    return 2*i + 1

def right_index(i):
    return 2*i + 2

#################
#   min heap    #
#################

def heapify_min(heap, lastIndex, toFix):
    mini = toFix
    while True:
        left = left_index(toFix)
        right = right_index(toFix)

        if left <= lastIndex and heap[left] < heap[mini]:
            mini = left

        if right <= lastIndex and heap[right] < heap[mini]:
            mini = right

        if mini == toFix:
            break

        heap[toFix], heap[mini] = heap[mini], heap[toFix]
        toFix = mini
    #end while

#################
#   max heap    #
#################

def heapify_max(heap: list[HeapElement], indexesInHeap: list[HeapMap], lastIndex: int, toFix: int):
    p = len(indexesInHeap)
    maxi = toFix
    while True:
        left = left_index(toFix)
        right = right_index(toFix)

        if left <= lastIndex and heap[left].val > heap[maxi].val:
            maxi = left

        if right <= lastIndex and heap[right].val > heap[maxi].val:
            maxi = right

        if maxi == toFix:
            break

        swap_elements_in_heap(heap, indexesInHeap, toFix, maxi)

        toFix = maxi
    #end while

def build_max_heap(tab: list[HeapElement], indexesInHeap: list[HeapMap]):
    n = len(tab)
    for i in range(n - 1, -1, -1):
        heapify_max(tab, indexesInHeap, n-1, i)

def heap_sort(heap: list[HeapElement], indexesInHeap: list[HeapMap]):
    n = len(heap)
    build_max_heap(heap, indexesInHeap)

    for i in range(n - 1, -1 , -1):
        swap_elements_in_heap(heap, indexesInHeap, 0, i)
        heapify_max(heap, indexesInHeap, i - 1, 0)

#######################
#   heap management   #
#######################

def swap_elements_in_heap(heap: list[HeapElement], indexesInHeap: list[HeapMap], i1: int, i2: int):
        ele1HeapMapIndex = index_in_heap_map(heap[i1], p)
        ele2HeapMapIndex = index_in_heap_map(heap[i2], p)

        heap[i1], heap[i2] = heap[i2], heap[i1]
        indexesInHeap[ele1HeapMapIndex], indexesInHeap[ele2HeapMapIndex] = \
            indexesInHeap[ele2HeapMapIndex], indexesInHeap[ele1HeapMapIndex]
    

# Note: heapMapLen = p
def index_in_heap_map(elem: HeapElement, heapMapLen: int) -> int:
    return elem.indexInOriginalTab % heapMapLen

def print_heap(heap: list[HeapElement], indexesInHeap: list[HeapMap], howManyElements: int):
    for j in range(howManyElements):
        HA = heap[j]
        IIH = indexesInHeap[index_in_heap_map(HA, p)]
        print(f"val: {HA.val}, indexInOriginalTab: {HA.indexInOriginalTab}")
        print(f"heapId: {IIH.heapId}, indexInHeap: {IIH.indexInHeap}")
        print()
    print("\n\n\n")

def ksum(T, k, p):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    result = 0

    # tworzymy tablicę mapującą elementy z pierwotnej talicy z elementami z kopców
    indexesInHeap = [HeapMap(0, i) for i in range(p)]

    # sortujemy p pierwszych elementów
    heapArray = [HeapElement(T[i], i) for i in range(p)]

    # swap_elements_in_heap(heapArray, indexesInHeap, 0, 1)
    heap_sort(heapArray, indexesInHeap)
    print_heap(heapArray, indexesInHeap, p)


    # tworzymy dwa kopce: pierwszy z p-k elementami, drugi z k elementami
        
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( ksum, all_tests=True )

tab = [7,9,1,5,8,6,2,12]
k = 4
p = 5
print(ksum(tab, k, p))
