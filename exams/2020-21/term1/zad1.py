# Imię Nazwisko
#
# Opis algorytmu:
# Najpierw każdemu elementowi z tablicy przypisujemy jego wartość oraz jego indeks przed posortowaniem. Kolejny krok to posortowanie,
# przy czym ważne jest, aby zastosować sortowanie stabilne. Ostatecznie przechodzimy przez tablicę i znajdujemy maksymalną różnicę
# pomiędzy obecną a pierwotną pozycją danego elementu. Jest to szukana liczba k.

from zad1testy import runtests

def heap_sort(T):
    n = len(T)

    build_max_heap(T)

    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify_max(T, i - 1, 0)

def build_max_heap(T):
    n = len(T)
    lastElemParent = (n - 2) // 2
    for i in range(lastElemParent, - 1, -1):
        heapify_max(T, n - 1, i)

def heapify_max(T, lastIndex, toFix):
    while True:
        maxi = toFix
        left = 2*toFix + 1
        right = 2*toFix + 2

        if left <= lastIndex and T[left] > T[maxi]:
            maxi = left

        if right <= lastIndex and T[right] > T[maxi]:
            maxi = right

        if maxi != toFix:
            T[toFix], T[maxi] = T[maxi], T[toFix]
            toFix = maxi
        else:
            break

def chaos_index(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)

    for i in range(n):
        T[i] = (T[i], i)

    heap_sort(T)
    print(T)

    k = 0

    for i in range(n):
        currentK = abs(T[i][1] - i)
        if currentK > k:
            k = currentK

    return k

runtests( chaos_index )
