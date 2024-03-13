from zad2testy import runtests

def binary_search(tab, val):
    n = len(tab)
    end = n - 1
    beg = 0
    while beg <= end:
        mid = (beg + end) // 2
        # print("bin s", beg, mid, end)
        if val < tab[mid]:
            end = mid - 1
        elif val > tab[mid]:
            beg = mid + 1
        else:
            return mid
    
    return beg

def binary_insert(tab, val):
    beg, end = 0, len(tab) - 1
    while beg <= end:
        mid = (beg + end) // 2
        if val >= tab[mid]:
            beg = mid + 1
        else:
            end = mid - 1
    return beg


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
    helpArray = [T[j] for j in range(p)]
    quick_sort(helpArray, 0, p - 1)
    result = helpArray[-k]

    for i in range(1, n - p + 1):
        valueToRemove = T[i-1]
        valueToInsert = T[i+p-1]

        toRemoveIndex = binary_search(helpArray, valueToRemove)
        del helpArray[toRemoveIndex]

        toInsertIndex = binary_insert(helpArray, valueToInsert)
        helpArray.insert(toInsertIndex, valueToInsert)

        result += helpArray[-k]
        
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
