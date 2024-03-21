from random import randint

def heapify_rek(heap, heapLen, index):
    maxi = index
    left = 2*index + 1
    right = 2*index + 2

    if left < heapLen and heap[left] > heap[maxi]:
        maxi = left

    if right < heapLen and heap[right] > heap[maxi]:
        maxi = right

    if maxi != index:
        heap[maxi], heap[index] = heap[index], heap[maxi]
        heapify_rek(heap, heapLen, maxi)

def heapify_it(heap, heapLen, toFix):
    while True:
        maxi = toFix
        left = 2*toFix + 1
        right = 2*toFix + 2

        if left < heapLen and heap[left] > heap[maxi]:
            maxi = left

        if right < heapLen and heap[right] > heap[maxi]:
            maxi = right

        if maxi != toFix:
            heap[maxi], heap[toFix] = heap[toFix], heap[maxi]
            toFix = maxi
        else:
            break
    #end while
        

def build_heap(tab):
    n = len(tab)
    for i in range(n - 1, -1, -1):
        heapify_it(tab, n, i)

def heap_sort(tab):
    n = len(tab)
    build_heap(tab)
    for i in range(n - 1, -1 , -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify_it(tab, i, 0)


if __name__ == "__main__":
    tab = [randint(1, 100) for i in range(10, -1, -1)]
    print(tab)
    heap_sort(tab)
    print(tab)