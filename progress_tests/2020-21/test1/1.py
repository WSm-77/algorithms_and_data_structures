# Dana jest dwuwymiarowa tablica T rozmiaru NxN wypełniona liczbami naturalnymi (liczby są parami różne). Proszę zaimplementować funkcję Median(T), 
# która przekształca tablicę T, tak aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej, a elementy leżące nad 
# główną przekątną nie były mniejsze od elementów na głównej przekątnej.


# znajdujemy pierwszy i ostatni element z głównej przekątnej wykorzystując algorytm quickSelect, dzięki czemu ustawimy elementy w żądanej kolejności
def Median(T):
    n = len(T)
    firstElemOnDiagLinearized = (n*n - n) // 2
    lastElemOnDiagLinearized = firstElemOnDiagLinearized + n - 1
    quick_select(T, firstElemOnDiagLinearized)
    quick_select(T, lastElemOnDiagLinearized)

def next_position(row, coll, n):
    if coll == n - 1:
        return (0, n - row)
    elif row == n - 1:
        return (n - coll - 2, 0)

    return (row + 1, coll + 1)

def prev_position(row, coll, n):
    if coll == 0:
        return (n - 1, n - row - 2)
    elif row == 0:
        return (n - coll, n - 1)
    
    return (row - 1, coll - 1)

def swap(T, row1, coll1, row2, coll2):
    T[row1][coll1], T[row2][coll2] = T[row2][coll2], T[row1][coll1]


def partition(T, begLinearized, endLinearized, begRow, begColl):
    n = len(T)

    # we choose pivota as first element
    pivot = T[begRow][begColl]
    pivotLinearized = begLinearized
    iRow, iColl = next_position(begRow, begColl, n)
    jRow, jColl = iRow, iColl
    begLinearized += 1
    

    while begLinearized <= endLinearized:
        if T[jRow][jColl] <= pivot:
            pivotLinearized += 1
            swap(T, jRow, jColl, iRow, iColl)
            iRow, iColl = next_position(iRow, iColl, n)
        jRow, jColl = next_position(jRow, jColl, n)
        begLinearized += 1
    #end while
        
    iRow, iColl = prev_position(iRow, iColl, n)    
    swap(T, iRow, iColl, begRow, begColl)
    return (iRow, iColl, pivotLinearized)

def quick_select(T, indexToFindLinearized):
    n = len(T)
    begLinearized = 0
    endLinearized = n*n - 1
    begRow = n - 1
    begColl = 0

    while True:
        pivotRow, pivotColl, pivotLinearized = partition(T, begLinearized, endLinearized, begRow, begColl)
        if pivotLinearized == indexToFindLinearized:
            break
        elif pivotLinearized < indexToFindLinearized:
            #quick_select(T, pivot+1, end, toFind)
            begRow, begColl = next_position(pivotRow, pivotColl, n)
            begLinearized = pivotLinearized + 1
        else:
            endLinearized = pivotLinearized - 1
        #end if
    #end while

if __name__ == "__main__":
    ##########  test 1  ###########
    print("test 1\n")

    testTab =   [[2, 3, 5],
                [7, 11, 13],
                [17, 19, 23]]
    
    print("unsorted:")
    print(*testTab, sep="\n")
    Median(testTab)
    print("\nsorted:")
    print(*testTab, sep="\n", end="\n\n")

    ##########  test 2  ###########
    print("test 2\n")

    testTab = [[43, 74, 53, 97],
               [80, 61, 61, 19],
               [61, 73, 89, 93],
               [42, 17, 89, 80]]

    print("unsorted:")
    print(*testTab, sep="\n")
    Median(testTab)
    print("\nsorted:")
    print(*testTab, sep="\n")