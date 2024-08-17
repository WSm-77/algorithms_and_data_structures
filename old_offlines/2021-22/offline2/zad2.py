from zad2testy import runtests

# key: 0 - x, 1 - y
def quick_sort(tab, beg, end, key):
    if beg < end:
        pivot = partition(tab, beg, end, key)

        quick_sort(tab, beg, pivot - 1, key)
        quick_sort(tab, pivot + 1, end, key)

def partition(tab, beg, end, key):
    i = beg

    for j in range(beg, end):
        if tab[j][0][key] < tab[end][0][key]:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1

    tab[i], tab[end] = tab[end], tab[i]
    return i

def depth(L):
    # tu prosze wpisac wlasna implementacje
    n = len(L)

    L = [(L[i], i) for i in range(n)]

    ########## sortowanie po x ##########

    # quick_sort(L, 0, n - 1, 0)            # custom sort
    L.sort(key=lambda x: x[0][0])
    xDepth = [n - 1]*n

    currentXDepth = n - 1
    prevIndex = 0
    i = 1
    numberOfPointsWithTheSameCoordinate = 0
    while i < n:
        if L[i][0][0] > L[i - 1][0][0]:
            numberOfPointsWithTheSameCoordinate = i - prevIndex - 1
            currentXDepth = n - i
            while prevIndex < i:
                xDepth[L[prevIndex][1]] = currentXDepth + numberOfPointsWithTheSameCoordinate
                prevIndex += 1
            #end while
            currentXDepth = i
        #end if
        i += 1
    #end while

    numberOfPointsWithTheSameCoordinate = i - prevIndex - 1
    currentXDepth = n - i

    while prevIndex < i:
        xDepth[L[prevIndex][1]] = currentXDepth + numberOfPointsWithTheSameCoordinate
        prevIndex += 1
    #end while

    ########## sortowanie po y ##########

    # quick_sort(L, 0, n - 1, 1)            # custom sort
    L.sort(key=lambda x: x[0][1])

    yDepth = [0]*n
    currentYDepth = 0
    prevIndex = 0
    i = 1

    while i < n:
        if L[i][0][1] > L[i - 1][0][1]:
            currentYDepth = i - 1
            while prevIndex < i:
                yDepth[L[prevIndex][1]] = currentYDepth
                prevIndex += 1
            #end while
            currentYDepth = i
        #end if
        i += 1
    #end while

    currentYDepth = i - 1

    while prevIndex < i:
        yDepth[L[prevIndex][1]] = currentYDepth
        prevIndex += 1
    #end while

    maxDepth = 0

    i = 0
    while i < n:
        currentPseudoDepth = xDepth[L[i][1]] + yDepth[L[i][1]] - n + 1
        maxDepth = max(maxDepth, currentPseudoDepth)
        i += 1
    #end while

    return maxDepth



runtests( depth )

# testTab = [[1, 6], [5, 6], [2, 5], [8, 9], [1, 6]]
# print(depth(testTab))
