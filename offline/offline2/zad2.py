from zad2testy import runtests

def quick_sort(tab, beg, end):
    if beg >= end:
        return
    
    pivot = partition(tab, beg, end)
    quick_sort(tab, beg, pivot - 1)
    quick_sort(tab, pivot + 1, end)

def partition(tab, beg, end):
    pivot = (beg + end) // 2
    if tab[beg] > tab[pivot]:
        tab[beg], tab[pivot] = tab[pivot], tab[beg]
    
    if tab[pivot] < tab[end]:
        tab[pivot], tab[end] = tab[end], tab[pivot]

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
        
    tab[beg], tab[pivot] = tab[pivot], tab[beg]
    return beg

def ksum(T, k, p):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    result = 0

    for i in range(n - p + 1):
        helpArray = [T[j] for j in range(i, i + p)]
        quick_sort(helpArray, 0, p - 1)
        # print(helpArray)
        result += helpArray[-k]
        
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )


# tab = [7,9,1,5,8,6,2,12]
# k = 4
# p = 5
# print(ksum(tab, k, p))