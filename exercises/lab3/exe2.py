#Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego.

# implementacja dla minHeap (rodzice mają mniejszą wartość od swoich dzieci)

import useful as uf
from random import randint

def parent(i):
    return (i - 1) // 2

def repair_min_heap(heap, toRepair):
    while toRepair > 0:
        eleParent = parent(toRepair)
        if heap[toRepair] < heap[eleParent]:
            heap[eleParent], heap[toRepair] = heap[toRepair], heap[eleParent]
            toRepair = eleParent
        else:
            break
        #end if
    #end while

def add_min_heap(heap, val):
    n = len(heap)
    heap.append(val)
    repair_min_heap(heap, n)

if __name__ == "__main__":
    minHeap = [randint(1, 100) for _ in range(randint(8, 15))]
    print(minHeap)
    uf.build_min_heap(minHeap)
    print(minHeap)
    add_min_heap(minHeap, randint(1, 8))
    print(minHeap)
    print(uf.is_min_heap(minHeap))
