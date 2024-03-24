# Proszę zaproponować algorytm, który w czasie liniowym sortuje tablicę A zwierającą n liczb ze zbrioru 0, 1, ..., n^2 - 1

from random import randint

def my_sort(tab):
    n = len(tab)

    # dzielimy liczbę na dwie składowe: resztę z dzielenia przez n i wartość dzielenie całkowitego przez n
    tab = [(ele // n, ele % n) for ele in tab]

    # teraz sortujemy tablicę najpierw po reszczie z dzielenia a później po części całkowitej dzielenia (stosując radix sort)
    for i in range(1, -1, -1):
        sortedTab = [None]*n
        cntTab = [0]*n
        
        for j in range(n):
            cntTab[tab[j][i]] += 1
        #end for
        
        for j in range(1, n):
            cntTab[j] += cntTab[j - 1]
        #end for
        
        for j in range(n - 1, -1, -1):
            cntTab[tab[j][i]] -= 1
            sortedTab[cntTab[tab[j][i]]] = tab[j]
        #end for
        
        tab = sortedTab
    #end for
    
    # teraz odtwarzamy naszą liczbę
    return [n*tab[i][0] + tab[i][1] for i in range(n)]


if __name__ == "__main__":
    n = randint(1, 20)
    testTab = [randint(0, n**2 - 1) for _ in range(n)]
    print("unsorted:")
    print(testTab)
    testTab = my_sort(testTab)
    print("sorted:")
    print(testTab)