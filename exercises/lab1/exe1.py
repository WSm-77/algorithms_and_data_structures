# given sorted array of length "n" that contains unique numbers from 0 to m - 1 (m > n); find the smallest non-negative intiger that is not contained by the array

from random import randint

def draw_without_repetitions(rangeStart: int, rangeStop: int, toDraw: int) -> list:
    drawn = [-1 for _ in range(toDraw)]
    drawnCnt = 0

    while drawnCnt < toDraw:
        new = randint(rangeStart, rangeStop)
        i = 0
        while drawn[i] != -1 and drawn[i] < new:
            i += 1
        #end while
        if drawn[i] == new:
            continue
        else:
            drawnCnt += 1
        #end if
        while i < toDraw:
            drawn[i], new = new, drawn[i]
            i += 1
        #end while
    #end while
    return drawn

def exe1(arr: list) -> int:
    n = len(arr)
    if arr[n - 1] == n - 1:
        return n
    
    beg, end = 0, n - 1
    while end - beg > 1:
        mid = (beg + end) // 2
        if mid != arr[mid]:
            end = mid
        else:
            beg = mid
        #end if
    #end while
            
    return beg if arr[beg] != beg else beg + 1


if __name__ == "__main__":
    tab = [0, 1, 2, 3, 6, 7, 8, 9, 10]          # answer: 4
    print(tab)
    print(exe1(tab))
    
    tab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]       # answer: 9
    print(tab)
    print(exe1(tab))
    
    tab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    # answer: 11
    print(tab)
    print(exe1(tab))
    
    tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]       # answer: 0
    print(tab)
    print(exe1(tab))

    n = randint(8, 15)
    tab = draw_without_repetitions(0, n + 1, n)
    print(tab)
    print(exe1(tab))