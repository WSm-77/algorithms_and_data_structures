from zad2testy import runtests

def partition(tab, beg, end):
    pivot = end
    i = beg
    for j in range(beg, end):
        if tab[j] <= tab[pivot]:
            tab[j], tab[i] = tab[i], tab[j]
            i += 1
    
    tab[i], tab[pivot] = tab[pivot], tab[i]
    return i

def quick_select(tab, beg, end, k):
    pivot = partition(tab, beg, end)
    if pivot == k:
        return tab[pivot]
    elif k < pivot:
        return quick_select(tab, beg, pivot - 1, k)
    else:
        return quick_select(tab, pivot + 1, end, k)

def ksum(T, k, p):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    result = 0
    for i in range(n - p + 1):
        helpArray = [T[j] for j in range(i, p+i)]
        result += quick_select(helpArray, 0, p - 1, p - k)
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
