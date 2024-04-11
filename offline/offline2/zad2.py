# Wiktor Sędzimir
#
# Opis:
# Algorytm opiera się na stworzeniu dwóch kopców: pierwszy - kopiec maksymalny wielkości p - k elementów, drugi - kopiec minimalny zawierający k elementów.
# Dzięki temu k-ty największy element spośród p elmentów będzie się znajdował na samym szczycie kopca minimalnego. Przechodząc o jedną pozycję dalej 
# w oryginalnej tablicy musimy usunąć najstarszy element z naszej struktury oraz dodać do niej kolejny element z tablicy. Dzięki wykorzystaniu kopców
# jesteśmy to w stanie zrobić w czasie logarytmicznym. Do znalezienia najstarszego elementu w kopcu stosujemy tablicę pomocniczą indexesInHeap, która zawiera
# ID kopca oraz indeks pod którym znajduje się w kopcu szukany element.  

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
    toAddHeapElement = HeapElement(originalTab[indexToAddOriginal], indexToAddOriginal)


    if toRemoveHeapMap.heapId == 0:
        if toAddHeapElement.val <= heap[minHeapFirstIndex].val:
            # dodajemy do kopca nr 0 i usuwamy z kopca nr 0
            heap[toRemoveHeapMap.indexInHeap] = toAddHeapElement
            toAddHeapMap.indexInHeap = toRemoveHeapMap.indexInHeap
            toAddHeapMap.heapId = 0
            indexesInHeap[oldestElementIndex] = toAddHeapMap
            max_heap_repair(heap, indexesInHeap, minHeapFirstIndex, toRemoveHeapMap.indexInHeap)
        else:
            # dodajemy do kopca nr 1 i usuwamy z kopca nr 0
            swap_elements_in_heap(heap, indexesInHeap, minHeapFirstIndex, toRemoveHeapMap.indexInHeap)
            max_heap_repair(heap, indexesInHeap, minHeapFirstIndex, toRemoveHeapMap.indexInHeap)
            heap[minHeapFirstIndex] = toAddHeapElement
            toAddHeapMap.heapId = 1
            toAddHeapMap.indexInHeap = minHeapFirstIndex
            indexesInHeap[oldestElementIndex] = toAddHeapMap
            heapify_min(heap, minHeapFirstIndex, indexesInHeap, len(heap) - 1, minHeapFirstIndex)
    else:
        if toAddHeapElement.val >= heap[0].val:
            # dodajemy do kopca nr 1 i usuwamy z kopca nr 1
            heap[toRemoveHeapMap.indexInHeap] = toAddHeapElement
            toAddHeapMap.indexInHeap = toRemoveHeapMap.indexInHeap
            toAddHeapMap.heapId = 1
            indexesInHeap[oldestElementIndex] = toAddHeapMap
            min_heap_repair(heap, indexesInHeap, minHeapFirstIndex, toRemoveHeapMap.indexInHeap)
        else:
            # dodajemy do kopca nr 0 i usuwamy z kopca nr 1 
            swap_elements_in_heap(heap, indexesInHeap, 0, toRemoveHeapMap.indexInHeap)
            min_heap_repair(heap, indexesInHeap, minHeapFirstIndex, toRemoveHeapMap.indexInHeap)
            heap[0] = toAddHeapElement
            toAddHeapMap.indexInHeap = 0
            toAddHeapMap.heapId = 0
            indexesInHeap[oldestElementIndex] = toAddHeapMap
            heapify_max(heap, indexesInHeap, minHeapFirstIndex - 1, 0)

def min_heap_repair(heap: list[HeapElement], indexesInHeap: list[HeapMap], minHeapFirstIndex: int, indexToRepair: int):
    correction = minHeapFirstIndex
    parent = (indexToRepair - correction - 1) // 2 + correction
    if (0 <= parent) and (heap[parent].val > heap[indexToRepair].val):
        while indexToRepair > minHeapFirstIndex and heap[parent].val > heap[indexToRepair].val:
            swap_elements_in_heap(heap, indexesInHeap, indexToRepair, parent)
            indexToRepair = parent
            parent = (indexToRepair - correction - 1) // 2 + correction
    else:
        heapify_min(heap, minHeapFirstIndex, indexesInHeap, len(heap) - 1, indexToRepair)

def heapify_min(heap: list[HeapElement], minHeapFirstIndex: int, indexesInHeap: list[HeapMap], lastIndex: int, toFix: int):
    mini = toFix
    indexCorrection = minHeapFirstIndex
    
    while True:
        mini = toFix
        left = 2*(toFix - indexCorrection) + 1 + indexCorrection
        right = 2*(toFix - indexCorrection) + 2 + indexCorrection

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

def max_heap_repair(heap: list[HeapElement], indexesInHeap: list[HeapMap], minHeapFirstIndex: int, indexToRepair: int):
    parent = (indexToRepair - 1) // 2
    if (0 <= parent) and (heap[parent].val < heap[indexToRepair].val):
        while indexToRepair > 0 and heap[parent].val < heap[indexToRepair].val:
            swap_elements_in_heap(heap, indexesInHeap, indexToRepair, parent)
            indexToRepair = parent
            parent = (indexToRepair - 1) // 2
    else:
        heapify_max(heap, indexesInHeap, minHeapFirstIndex - 1, indexToRepair)

def heapify_max(heap: list[HeapElement], indexesInHeap: list[HeapMap], lastIndex: int, toFix: int):
    maxi = toFix
    while True:
        maxi = toFix
        left = 2*toFix + 1
        right = 2*toFix + 2

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

def modified_heap_sort(heap: list[HeapElement], indexesInHeap: list[HeapMap], k: int):
    n = len(heap)
    build_max_heap(heap, indexesInHeap)

    for i in range(n - 1, n - k -1 , -1):
        swap_elements_in_heap(heap, indexesInHeap, 0, i)
        IIH = heapElement_to_heapMap(heap[i], indexesInHeap)
        IIH.heapId = 1
        heapify_max(heap, indexesInHeap, i - 1, 0)

#######################
#   heap management   #
#######################

def swap_elements_in_heap(heap: list[HeapElement], indexesInHeap: list[HeapMap], i1: int, i2: int):
        p = len(heap)
        ele1HeapMapIndex = heap[i1].indexInOriginalTab % p
        ele2HeapMapIndex = heap[i2].indexInOriginalTab % p

        heap[i1], heap[i2] = heap[i2], heap[i1]
        indexesInHeap[ele1HeapMapIndex], indexesInHeap[ele2HeapMapIndex] = \
            indexesInHeap[ele2HeapMapIndex], indexesInHeap[ele1HeapMapIndex]    

def heapElement_to_heapMap(elem: HeapElement, indexesInHeap: list[HeapMap]) -> HeapMap:
    return indexesInHeap[elem.indexInOriginalTab % len(indexesInHeap)]

# przydatne w debugowaniu
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

    # rozdzielamy heapArray na dwa kopce: pierwszy z p-k elementami, drugi z k elementami, w tym celu mudyfikujemy heap sorta aby posortował tylko k 
    # elementów dzięki czemu ostatnie k elementów tworzy minHeap a pozostałe tworzą maxHeap 
    heapArray = [HeapElement(T[i], i) for i in range(p)]
    modified_heap_sort(heapArray, indexesInHeap, k)
    minHeapFirstIndex = p - k

    # przechodzimi przez oryginalną tablicę dopóki nie dojdziemy do jej końca za każdym razem dodając żądaną wartość do sumy
    result = heapArray[minHeapFirstIndex].val
    for i in range(p, originalTabLen):
        heap_replace(T, i, heapArray, indexesInHeap, oldestElementIndex, minHeapFirstIndex)
        result += heapArray[minHeapFirstIndex].val
        oldestElementIndex = (oldestElementIndex + 1) % p
        
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
