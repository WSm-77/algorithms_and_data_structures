# Dana jest tablica A o długości n. Wartości w tablicy pochodzą ze zbioru B, gdzie |B| = log n. Proszę zaproponować możliwie jak 
# najszybszy algorytm sortowania tablicy A.

# tworzymy tablicę B trzymającą różne wartości z tablicy A. Tworzymy też tablicę zliczającą ilości wystąpień danej liczby (musimy powiązać 
# te dwie tablice). Tablicę B utrzymujemy cały czas posortowaną, dzięki czemu możemy znaleźć indeks do wstawienia nowego elementu
# możemy wykonać binary searchem 

from random import randint
from math import log2

def bin_search(tab, val):
    beg = 0
    end = len(tab) - 1

    while beg <= end:
        mid = (end + beg) // 2
        if tab[mid] == val:
            return mid
        elif val < tab[mid]:
            end = mid - 1
        else:
            beg = mid + 1
        #end if
    #end while
            
    return beg


def sort_A(A):
    n = len(A)

    # B[i][0] wartość i-tego elementu, B[i][1] indeks licby B[i][0] w tablicy cntTab 
    B = [A[0]]

    # licznik liczb z B
    cntTab = [1]

    # uzupełniamy tablicę B oraz zliczamy ile jest poszczególnych elementów
    for i in range(1, n):
        currentVal = A[i]
        index = bin_search(B, currentVal)
        BLen = len(B)
        if index >= BLen:
            B.append(currentVal)
            cntTab.append(1)
        elif B[index] == currentVal:
            cntTab[index] += 1
        else:
            cntTab.append(None)
            B.append(None)
            for j in range(BLen, index, - 1):
                B[j] = B[j - 1]
                cntTab[j] = cntTab[j - 1]
            #end for
            B[index] = currentVal
            cntTab[index] = 1
        #end if
    #end for

    for i in range(1, len(cntTab)):
        cntTab[i] += cntTab[i - 1]
    #end for

    sortedTab = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        currentVal = A[i]
        indexInBtab = bin_search(B, currentVal)
        cntTab[indexInBtab] -= 1
        sortedTab[cntTab[indexInBtab]] = currentVal
    #end for
        
    return sortedTab


if __name__  == "__main__":
    n = 20
    start = randint(1, 10)
    testTab = [randint(start, start + round(log2(n))) for _ in range(n)]
    print(testTab)
    testTab = sort_A(testTab)
    print(testTab)
