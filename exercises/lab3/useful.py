def parent_index(i):
    return (i - 1) // 2

def left_index(i):
    return 2*i + 1

def right_index(i):
    return 2*i + 2

#################
#   max heap    #
#################

def is_max_heap(heap):
    def rek(heap, lastIndex, index = 0):
        if index >= lastIndex:
            return True
        left = left_index(index)
        right = right_index(index)
        if (left <= lastIndex and heap[left] > heap[index]) or \
           (right <= lastIndex and heap[right] > heap[index]):
            
            return False
        #end if
        return rek(heap, lastIndex, left) and rek(heap, lastIndex, right)

    #end def
    n = len(heap)
    return rek(heap, n - 1)

def heapify_max(heap, lastIndex, toFix):
    maxi = toFix
    while True:
        left = left_index(toFix)
        right = right_index(toFix)

        if left <= lastIndex and heap[left] > heap[maxi]:
            maxi = left

        if right <= lastIndex and heap[right] > heap[maxi]:
            maxi = right

        if maxi == toFix:
            break

        heap[toFix], heap[maxi] = heap[maxi], heap[toFix]
        toFix = maxi
    #end while

def build_max_heap(tab):
    n = len(tab)
    for i in range(n - 1, -1, -1):
        heapify_max(tab, n-1, i)

#################
#   min heap    #
#################

def is_min_heap(heap):
    def rek(heap, lastIndex, index = 0):
        if index >= lastIndex:
            return True
        left = left_index(index)
        right = right_index(index)
        if (left <= lastIndex and heap[left] < heap[index]) or \
           (right <= lastIndex and heap[right] < heap[index]):
            
            return False
        #end if
        return rek(heap, lastIndex, left) and rek(heap, lastIndex, right)

    #end def
    n = len(heap)
    return rek(heap, n - 1)

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

def build_min_heap(tab):
    n = len(tab)
    for i in range(n - 1, -1, -1):
        heapify_min(tab, n-1, i)

if __name__ == "__main__":
    maxHeap = [5,6,1,7,8,2,9,11,15]
    build_max_heap(maxHeap)
    print(maxHeap)
    print(is_max_heap(maxHeap))

    minHeap = [5,6,1,7,8,2,9,11,15]
    build_min_heap(minHeap)
    print(minHeap)
    print(is_min_heap(minHeap))