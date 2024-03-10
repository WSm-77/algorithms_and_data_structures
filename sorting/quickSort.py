from random import randint

def quick_sort(tab: list) -> None:
    def rek(tab, beg, end):
        if end <= beg:
            return
        #end if
        pivot = partitionate(tab, beg, end)
        rek(tab, beg, pivot - 1)
        rek(tab, pivot + 1, end)
    #end def
        
    n = len(tab)
    rek(tab, 0, n - 1)

def partitionate(tab, beg, end):
    pivot = (beg + end) // 2

    #we choose pivot as median of the first, middle and last elements of array
    if tab[beg] > tab[pivot]:
        tab[beg], tab[pivot] = tab[pivot], tab[beg]
    #end if
    if tab[pivot] < tab[end]:
        tab[end], tab[pivot] = tab[pivot], tab[end]
    #end if
        
    pivot = end
    end -= 1
    while beg <= end:
        if tab[beg] <= tab[pivot]:
            beg += 1
        elif tab[end] >= tab[pivot]:
            end -= 1
        else:
            tab[beg], tab[end] = tab[end], tab[beg]
            beg += 1
            end -= 1
        #end if
    #end while
    tab[beg], tab[pivot] = tab[pivot], tab[beg]
    pivot = beg

    return pivot

if __name__ == "__main__":
    tab = [randint(1, 100) for _ in range(randint(8, 15))]
    print(f"array:\t\t{tab}")
    quick_sort(tab)
    print(f"quicksort:\t{tab}")
    print(f"build-in sort:\t{sorted(tab)}")
    