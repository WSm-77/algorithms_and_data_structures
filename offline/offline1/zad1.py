# Wiktor Sędzimir
#
# opis działania:
# Algorytm jest odmianą heap sorta, który korzysta z kopca o wielkości k+1 elementów, w którym u samej góry znajdują się najmniejsze elementy.
# Na początku algorytm tworzy kopiec z pierwszych k+1 elementów linked listy. Póżniej cyklicznie zdejmuje element znajdujący się u szczytu kopca i dodaje
# go na koniec wynikowej listy. Kolejny krok to dodanie elementu z nie posortowanej listy na szczyt kopca oraz jego naprawa. Po wyczerpaniu elementów 
# z k-chaotycznej listy pozostaje opróżnienie kopca i dodanie jego elementów do posortowanej listy.  
# uzasadnienie poprawności:
# k-chaotyczne listy charakteryzują sie tym, że element, który powinien znajdować się na pozycji o indeksie 0, znajduje się na pozycji oddalonej o co 
# najwyżej "k". Oznacze to, że wśród pierwszych k+1 elementów listy na pewno znajduje się najmniejszy element z listy, a użycie kopca gwarantuje, źe będzie
# się on znajdował na jego szczycie. Możemy zatem wziąć ten element i umieścić w posortowanej liści. Teraz bierzemy element znajdujący się pod k+1 indeksem
# nieposortowanej listy i dodajemy go do kopca, co oznacza że w kopcu znajduje się już element, który powinien znajdować się pod indeksem 1 w posortowanej 
# liście (po naprawieniu kopca znowu będzie znajdował się na jego szczycie). Jeżeli rozważamy n-ty indeks posortowanej listy to dodajemy do kopca (n+k)-ty
# element nieposortowanej listy, co oznacza, że pod n-tym indeksem powinien znajdować się nowo dodany element lub jeden z pozostałych w kopcu, który jeszcze
# nie został wykorzystany.
# Algorytm ma złożoność czasową Θ(n log k) oraz pamięciową Θ(k). Dla k = :
# 1) Θ(1), algortym ma złożoność liniową (Θ(n)) - szybszą od złożoności szybkich algorytmów sortujących,
# 2) Θ(log n), algortym ma złożoność Θ(n log (log n)) - szybszą od złożoności szybkich algorytmów sortujących,
# 3) Θ(n), algortym ma złożoność Θ(n log n) - porównywalną z szybkością zwykłego heap sorta, merge sorta czy quick sorta.

from zad1testy import Node, runtests

def heapify(heap, heapSize, index):
    mini = index
    left = 2*index + 1
    right = 2*index + 2

    if left < heapSize and heap[left].val < heap[mini].val:
        mini = left

    if right < heapSize and heap[right].val < heap[mini].val:
        mini = right

    if mini != index:
        heap[mini], heap[index] = heap[index], heap[mini]
        heapify(heap, heapSize, mini)

def build_heap(tab, heapSize):
    for i in range(heapSize - 1, -1, -1):
        heapify(tab, heapSize, i)

def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    if k == 0:
        return p
    
    result = Node()
    lastElem = result
    heapSize = k + 1
    heap = [0 for _ in range(heapSize)]
    for i in range(heapSize):
        if p != None:
            heap[i] = p
            p = p.next
        else:
            heapSize = i
            break
    #end for
        
    build_heap(heap, heapSize)

    while p != None:
        lastElem.next = heap[0]
        lastElem = lastElem.next
        heap[0] = p
        heapify(heap, heapSize, 0)
        p = p.next
    #end while
        
    for i in range(heapSize - 1, -1, -1):
        heap[i], heap[0] = heap[0], heap[i]
        lastElem.next = heap[i]
        lastElem = lastElem.next
        heapify(heap, i, 0)
    #end for
    lastElem.next = None

    return result.next

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
