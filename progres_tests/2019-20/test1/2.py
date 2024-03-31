# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu 
# w szeregu malejąco względem wzrostu. Proszę zaimplementować funkcję: section(T,p,q)która zwróci tablicę ze wzrostami żołnierzy na 
# pozycjach od p do q włącznie. Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis 
# algorytmu oraz proszę oszacować jego złożoność czasową.

# Imie Nazwisko
#
# Opis algorytmu:
# Korzystamy z algorytmu "quick select", aby ustawić elementy z pozycji p i q na odpowiednich dla siebie pozycjach. Zastosowanie 
# algorymu "quick select" dodatkowo gwarantuje nam, że elementy większe od p znajdą się na lewo od p oraz elementy mniejsze od q
# znajdą się na prawo od q. Sprawia to, że pomiędzy elementami p a q znajdują się wyłącznie elementy mniejsze od p i większe od q,
# czyli dokładnie te, których szukamy. Ponieważ złożoność czasowa "quick selecta" jest liniowa to nasz algorytm również ma złożoność 
# liniową.

from random import randint

def quick_select(tab, beg, end, position):
    while beg < end:
        pivot = partition(tab, beg, end)

        if pivot == position:
            return
        elif pivot < position:
            beg = pivot + 1
        else:
            end = pivot - 1
        #end if
    #end while

def partition(tab, beg, end):
    i = beg - 1
    for j in range(beg, end):
        if tab[j] > tab[end]:
            i += 1
            tab[j], tab[i] = tab[i], tab[j]
        #end if
    #end for
    
    tab[i + 1], tab[end] = tab[end], tab[i + 1]

    return i + 1

def section(T, p, q):
    n = len(T)

    quick_select(T, 0, n - 1, p)
    quick_select(T, p, n - 1, q)

    return T[p:q+1]

if __name__ == "__main__":

    ########## test 1 ##########

    print("test1\n")

    p = 2
    q = 5
    testTab = [1.30, 1.98, 1.54, 2.00, 1.78, 1.23, 1.80, 1.87, 1.90, 2.10]

    print(testTab)
    correctAnswer = sorted(testTab, reverse=True)[p:q+1]
    algorithmOutput = sorted(section(testTab, p, q), reverse=True)
    print(f"correct answer:\t\t{correctAnswer}")
    print(f"algorithm output:\t{algorithmOutput}")

    ########## test 2 ##########

    print("\ntest2\n")

    n = 100_000
    p = randint(0, n // 2 + n // 4)
    q = randint(p + 1, n - 1)

    print(f"n: {n}, p: {p}, q: {q}")
    testTab = [randint(10*n,20*n) / (10*n) for _ in range(n)]
    correctAnswer = sorted(testTab, reverse=True)[p:q+1]
    algorithmOutput = sorted(section(testTab, p, q), reverse=True)


    if correctAnswer == algorithmOutput:
        print("test PASSED")
    else:
        print("test FAILED")
    #end if