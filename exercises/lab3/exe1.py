# Proszę zaimplementować algorytm QuickSort do sortowanie n elementowej tablicy tak, żzeby zawsze używał najwyżej O(log n) dodatkowej pamięci 
# na stosie, niezależnie od jakości podziałów w funkcji partition.

from random import randint

def quick_sort(tab, beg, end):
    while beg < end:
        pivot = partition(tab, beg, end)
        if (pivot - beg < end - pivot):
            quick_sort(tab, beg, pivot - 1)
            beg = pivot + 1
        else:
            quick_sort(tab, pivot + 1, end)
            end = pivot - 1

def partition(tab, beg, end):
    pivot = tab[end]
    i = beg - 1

    for j in range(beg, end):
        if tab[j] <= pivot: 
            i = i + 1
            (tab[i], tab[j]) = (tab[j], tab[i])
 
    (tab[i + 1], tab[end]) = (tab[end], tab[i + 1])
    return i + 1

if __name__ == "__main__":
    testTab = [randint(1, 100) for _ in range(randint(8, 15))]
    print(f"original:\n{testTab}\n")
    print(f"sorted (build-in):\n{sorted(testTab)}\n")
    quick_sort(testTab, 0, len(testTab) - 1)
    print(f"sorted (quick sort):\n{testTab}")