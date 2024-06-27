# Opis algorytmu:
# Zawsze zjadamy największy lód, dopóki pozostał jakiś nieroztopiony. Aby osiągnąć złożoność liniową najpierw zjadamy
# wszystkie lody, które nie będą miały okazji się roztopić, a pozostałe sortujemy counting sortem.
# 
# Złożoność obliczeniowa:
# O(n)

from kolutesty import runtests

def counting_sort(array: list, n):
    arrayLen = len(array)
    cnt = [0]*n

    for ele in array:
        cnt[ele] += 1

    for i in range(1, n):
        cnt[i] += cnt[i - 1]
    
    sortedArray = [0]*arrayLen

    for i in range(arrayLen - 1, -1, -1):
        cnt[array[i]] -= 1
        idx = cnt[array[i]]
        sortedArray[idx] = array[i]

    return sortedArray


def ice_cream( T ):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    iceCreamAmount = 0
    time = 0
    remainingTab = []

    for amount in T:
        if amount >= n:
            iceCreamAmount += amount
            time += 1
        else:
            remainingTab.append(amount)

    remainingTab = counting_sort(remainingTab, n)

    for i in range(len(remainingTab) - 1, -1, -1):
        # all left ice creams have already melt
        if remainingTab[i] <= time:
            break
        iceCreamAmount += remainingTab[i]
        time += 1

    return iceCreamAmount - (time*(time - 1) // 2)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
