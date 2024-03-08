from random import randint

def heapify(heap, heapLen, index):
    maxi = index
    left = 2*index + 1
    right = 2*index + 2

    if left < heapLen and tab[left] > tab[maxi]:
        maxi = left

    if right < heapLen and tab[right] > tab[maxi]:
        maxi = right

    if maxi != index:
        tab[maxi], tab[index] = tab[index], tab[maxi]
        heapify(heap, heapLen, maxi)

def build_heap(tab):
    n = len(tab)
    for i in range(n - 1, -1, -1):
        heapify(tab, n, i)

def heap_sort(tab):
    n = len(tab)
    build_heap(tab)
    for i in range(n - 1, -1 , -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, i, 0)


if __name__ == "__main__":
    tab = [randint(1, 100) for i in range(10, -1, -1)]
    print(tab)
    heap_sort(tab)
    print(tab)