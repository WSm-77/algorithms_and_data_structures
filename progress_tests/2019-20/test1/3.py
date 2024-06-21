# Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy jest sumą dwóch innych 
# liczb z tablicy. Zaproponowany algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową.

from random import randint

def heap_sort(T):
    n = len(T)

    build_max_heap(T)

    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify_max(T, i - 1, 0)

def build_max_heap(T):
    n = len(T)
    lastElemParent = (n - 2) // 2

    for i in range(lastElemParent, -1, -1):
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
            T[maxi], T[toFix] = T[toFix], T[maxi]
            toFix = maxi
        else:
            break
        #end if
    #end while

def is_sum_of_numbers(T, index):
    n = len(T)

    i = 0
    j = n - 1
    while i < j:
        if i == index:
            i += 1
            if i >= j:
                return False
        if j == index:
            j -= 1
            if j <= i:
                return False
        if T[i] + T[j] == T[index]:
            return True
        elif T[i] + T[j] < T[index]:
            i += 1
        else:
            j -= 1
        #end if
    #end while
    
    return False

def check(T):
    n = len(T)
    if n < 3:
        return False
    #end if

    heap_sort(T)

    if T[0] > 0:
        return False
    #end if

    for i in range(n):
        if not is_sum_of_numbers(T, i):
            return False

    return True




if __name__ == "__main__":

    testTab = [5, 6, 1, 2, 8, 4, -1]
    print(testTab)
    print(check(testTab))

    testTab = [-1, 2, 1, -1, 0, 1, -2]
    print(testTab)
    print(check(testTab))

    testTab = [2, 1, -1, 0, 1, -2]
    print(testTab)
    print(check(testTab))
