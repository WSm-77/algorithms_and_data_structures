# ile jest inversji w tablicy długości n?

from random import randint

def inversions(tab):
    def merge_sort(tab: list, beg: int, end: int):
        if beg == end:
            return ([tab[beg]], 0)
        
        inversionsCnt = 0
        mid = (beg + end) // 2
        beg1 = beg
        end1 = mid
        beg2 = mid + 1
        end2 = end
        left, inv = merge_sort(tab, beg1, end1)
        inversionsCnt += inv
        right, inv = merge_sort(tab, beg2, end2)
        inversionsCnt += inv
        result, inv = merge(left, right)
        inversionsCnt += inv

        return (result, inversionsCnt)
    #end def

    n = len(tab)
    _, result = merge_sort(tab, 0, n - 1)
    
    return result

# in merge function we count inversions
def merge(tab1, tab2):
    inversions = 0
    len1 = len(tab1)
    len2 = len(tab2)
    index1 = 0
    index2 = 0
    merged = [0 for _ in range(len1 + len2)]
    mergedIndex = 0
    while index1 < len1 and index2 < len2:
        if tab1[index1] > tab2[index2]:
            merged[mergedIndex] = tab2[index2]
            index2 += 1
        else:
            merged[mergedIndex] = tab1[index1]
            inversions += index2
            index1 += 1
        #end if
        mergedIndex += 1
    #end while
    remaining = tab1
    remainingIndex = index1
    remainingLen = len1
    multiplier = 1
    if index1 == len1:
        remaining = tab2
        remainingIndex = index2
        remainingLen = len2
        multiplier = 0

    while remainingIndex < remainingLen:
        merged[mergedIndex] = remaining[remainingIndex]
        mergedIndex += 1
        remainingIndex += 1
        inversions += index2 * multiplier
    #end while
        
    return (merged, inversions)

def inversions_brute_force(tab):
    n = len(tab)
    inversions = 0
    for i in range(0, n - 1):
        for j in range(i, n):
            if tab[i] > tab[j]:
                inversions += 1

    return inversions

if __name__ == "__main__":
    tab = [randint(1, 100) for _ in range(randint(4, 15))]
    print(tab)

    print(f"inversions (optimaly):\t\t{inversions(tab)}")
    print(f"inversions (brute force):\t{inversions_brute_force(tab)}")


