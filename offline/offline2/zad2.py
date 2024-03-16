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

# Note:
# heapId:
# 0 - kopiec z p - k elementami
# 1 - kopiec z k elementami
class HeapMap:
    def __init__(self, heapId: int, indexInHeap: int) -> None:
        self.heapId = heapId
        self.indexInHeap = indexInHeap

###########################
#   min heap management   #
###########################
        
def heap_replace(originalTab: list, indexToAddOriginal: int, heap: list[HeapElement], \
                 indexesInHeap: list[HeapMap], oldestElementIndex: int, minHeapFirstIndex:int ):
    
    toRemoveHeapMap = indexesInHeap[oldestElementIndex]
    toAddHeapMap = HeapMap(0, 0)
    toAdd = HeapElement(originalTab[indexToAddOriginal], indexToAddOriginal)


    # 0 - we add to heap 1 and remove from heap 1
    # 1 - we add to heap 1 and remove from heap 0
    # 2 - we add to heap 0 and remove from heap 0
    # 3 - we add to heap 0 and remove from heap 1 
    result = 0

    if toRemoveHeapMap.heapId == 0:
        if toAdd.val <= heap[minHeapFirstIndex].val:
            result = 2
        else:
            result = 1
    else:
        if toAdd.val >= heap[0].val:
            result = 0
        else:
            result = 3

    
    match result:
        case 0:
            heap[toRemoveHeapMap.indexInHeap] = toAdd
            toAddHeapMap.indexInHeap = toRemoveHeapMap.indexInHeap
            toAddHeapMap.heapId = 1
            indexesInHeap[oldestElementIndex] = toAddHeapMap
            min_heap_repair(heap, indexesInHeap, minHeapFirstIndex, toRemoveHeapMap.indexInHeap)
        
        case 1:
            swap_elements_in_heap(heap, indexesInHeap, minHeapFirstIndex, toRemoveHeapMap.indexInHeap)
            max_heap_repair(heap, indexesInHeap, minHeapFirstIndex, toRemoveHeapMap.indexInHeap)
            heap[minHeapFirstIndex] = toAdd
            toAddHeapMap.heapId = 1
            toAddHeapMap.indexInHeap = minHeapFirstIndex
            indexesInHeap[oldestElementIndex] = toAddHeapMap
            heapify_min(heap, minHeapFirstIndex, indexesInHeap, len(heap) - 1, minHeapFirstIndex)

        case 2:
            heap[toRemoveHeapMap.indexInHeap] = toAdd
            toAddHeapMap.indexInHeap = toRemoveHeapMap.indexInHeap
            toAddHeapMap.heapId = 0
            indexesInHeap[oldestElementIndex] = toAddHeapMap
            max_heap_repair(heap, indexesInHeap, minHeapFirstIndex, toRemoveHeapMap.indexInHeap)

        case 3:
            swap_elements_in_heap(heap, indexesInHeap, 0, toRemoveHeapMap.indexInHeap)
            min_heap_repair(heap, indexesInHeap, minHeapFirstIndex, toRemoveHeapMap.indexInHeap)
            heap[0] = toAdd
            toAddHeapMap.indexInHeap = 0
            toAddHeapMap.heapId = 0
            indexesInHeap[oldestElementIndex] = toAddHeapMap
            heapify_max(heap, indexesInHeap, minHeapFirstIndex - 1, 0)




def max_heap_repair(heap: list[HeapElement], indexesInHeap: list[HeapMap], minHeapFirstIndex: int, indexToRepair: int):
    parent = parent_index(indexToRepair)
    if (0 <= parent) and (heap[parent].val < heap[indexToRepair].val):
        while indexToRepair > 0 and heap[parent].val < heap[indexToRepair].val:
            swap_elements_in_heap(heap, indexesInHeap, indexToRepair, parent)
            indexToRepair = parent
            parent = parent_index(indexToRepair)
    else:
        heapify_max(heap, indexesInHeap, minHeapFirstIndex - 1, indexToRepair)

def min_heap_repair(heap: list[HeapElement], indexesInHeap: list[HeapMap], minHeapFirstIndex: int, indexToRepair: int):
    correction = minHeapFirstIndex
    parent = parent_index(indexToRepair - correction) + correction
    if (0 <= parent) and (heap[parent].val > heap[indexToRepair].val):
        while indexToRepair > minHeapFirstIndex and heap[parent].val > heap[indexToRepair].val:
            swap_elements_in_heap(heap, indexesInHeap, indexToRepair, parent)
            indexToRepair = parent
            parent = parent_index(indexToRepair - correction) + correction
    else:
        heapify_min(heap, minHeapFirstIndex, indexesInHeap, len(heap) - 1, indexToRepair)

def heapify_min(heap: list[HeapElement], minHeapFirstIndex: int, indexesInHeap: list[HeapMap], lastIndex: int, toFix: int):
    mini = toFix
    indexCorrection = minHeapFirstIndex
    
    while True:
        left = left_index(toFix - indexCorrection) + indexCorrection
        right = right_index(toFix - indexCorrection) + indexCorrection

        if left <= lastIndex and heap[left].val < heap[mini].val:
            mini = left

        if right <= lastIndex and heap[right].val < heap[mini].val:
            mini = right

        if mini == toFix:
            break

        swap_elements_in_heap(heap, indexesInHeap, toFix, mini)

        toFix = mini
    #end while

#################
#   max heap    #
#################

def heapify_max(heap: list[HeapElement], indexesInHeap: list[HeapMap], lastIndex: int, toFix: int):
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
        
def parent_index(i):
    return (i - 1) // 2

def left_index(i):
    return 2*i + 1

def right_index(i):
    return 2*i + 2

def swap_elements_in_heap(heap: list[HeapElement], indexesInHeap: list[HeapMap], i1: int, i2: int):
        p = len(heap)
        ele1HeapMapIndex = index_in_heap_map(heap[i1], p)
        ele2HeapMapIndex = index_in_heap_map(heap[i2], p)

        heap[i1], heap[i2] = heap[i2], heap[i1]
        indexesInHeap[ele1HeapMapIndex], indexesInHeap[ele2HeapMapIndex] = \
            indexesInHeap[ele2HeapMapIndex], indexesInHeap[ele1HeapMapIndex]
    

# Note: heapMapLen = p
def index_in_heap_map(elem: HeapElement, heapMapLen: int) -> int:
    return elem.indexInOriginalTab % heapMapLen

def heapElement_to_heapMap(elem: HeapElement, indexesInHeap: list[HeapMap]) -> HeapMap:
    return indexesInHeap[index_in_heap_map(elem, len(indexesInHeap))]

def heapMap_to_heapElement(heapMapElem: HeapMap, heap: list[HeapElement], minHeapFirstIndex: int) -> HeapElement:
    indexInHeap = heapMapElem.indexInHeap
    if heapMapElem.heapId == 1:
        indexInHeap += minHeapFirstIndex

    return heap[indexInHeap]

def k_th_largest_element(heap: list[HeapElement], minHeapFirstIndex: int) -> int:
    return heap[minHeapFirstIndex].val

def print_heap(heap: list[HeapElement], indexesInHeap: list[HeapMap], howManyElements: int):
    for j in range(howManyElements):
        HA = heap[j]
        IIH = heapElement_to_heapMap(HA, indexesInHeap)
        print(f"val: {HA.val}, indexInOriginalTab: {HA.indexInOriginalTab}")
        print(f"heapId: {IIH.heapId}, indexInHeap: {IIH.indexInHeap}")
        print()
    print("\n\n\n")


############
#   main   #
############
    

def ksum(T, k, p):
    # tu prosze wpisac wlasna implementacje
    originalTabLen = len(T)

    # tworzymy tablicę mapującą elementy z pierwotnej talicy z elementami z kopców
    indexesInHeap = [HeapMap(0, i) for i in range(p)]
    oldestElementIndex = 0

    # sortujemy p pierwszych elementów
    heapArray = [HeapElement(T[i], i) for i in range(p)]
    heap_sort(heapArray, indexesInHeap)
    # print_heap(heapArray, indexesInHeap, p)

    # rozdzielamy heapArray na dwa kopce: pierwszy z p-k elementami, drugi z k elementami
    minHeapFirstIndex = p - k
    for i in range(minHeapFirstIndex//2):
        swap_elements_in_heap(heapArray, indexesInHeap, i, minHeapFirstIndex - i - 1)

    for i in range(minHeapFirstIndex, p):
        IIH = heapElement_to_heapMap(heapArray[i], indexesInHeap)
        IIH.heapId = 1

    # przechodzimi przez oryginalną tablicę dopóki nie dojdziemy do jej końca za każdym razem dodając żądaną wartość do sumy
    result = k_th_largest_element(heapArray, minHeapFirstIndex)
    for i in range(p, originalTabLen):
        heap_replace(T, i, heapArray, indexesInHeap, oldestElementIndex, minHeapFirstIndex)
        result += k_th_largest_element(heapArray, minHeapFirstIndex)
        oldestElementIndex = (oldestElementIndex + 1) % p
        
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )

# tab = [51, 56, 45, 6, 75, 52, 49, 58, 71, 36]
# k = 2
# p = 4
# print(ksum(tab, k, p))
