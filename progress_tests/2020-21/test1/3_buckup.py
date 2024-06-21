from test3 import runtests
from math import floor

# bucketsIndexing: 0 - prevIndex, 1 - prevVal, 2 - size
def bucket_index(val, bucketsIndexing):
    interval = floor(val) - 1
    return bucketsIndexing[interval][0] + floor((val - bucketsIndexing[interval][1]) / bucketsIndexing[interval][2])

def SortTab(T, P):
    n = len(T)
    k = len(P)

    # intervals: 1-2, 2-3, ... , (n-1) - n, n - (n + 1)
    howManyNumbersInInterval = [0]*n

    for a, b, c in P:
        intervalSize = b - a
        numberOfNumbersPerOneCell = c*n / intervalSize
        for i in range(a, b):
            howManyNumbersInInterval[i - 1] += numberOfNumbersPerOneCell
        #end for
    #end for
            
    intervalSizeTab = [howManyNumbersInInterval[i] for i in range(n)]


    print(howManyNumbersInInterval)

    for i in range(n):
        intervalSizeTab[i] = 1 / howManyNumbersInInterval[i] if howManyNumbersInInterval[i] != 0 else 0
    #end for
        
    helper = [intervalSizeTab[i] for i in range(n)]
        
    for i in range(1, n):
        howManyNumbersInInterval[i] += howManyNumbersInInterval[i - 1]
        helper[i] += helper[i - 1]

    print(helper)
    print(intervalSizeTab)
    bucketsIndexing = [None for i in range(1, n+1)]
    bucketsIndexing[0] = [0, 1, intervalSizeTab[0]]

    for i in range(1, n):
        # howManyNumbersInInterval[i] += 1
        bucketsIndexing[i] = [floor(howManyNumbersInInterval[i]) - 1, helper[i] + 1, intervalSizeTab[i]]
        
    print(howManyNumbersInInterval)
    print(bucketsIndexing)

    buckets = [[] for _ in range(n)]

    for i in range(n):
        index = bucket_index(T[i], bucketsIndexing)
        print(index)
        buckets[index].append(T[i])
    #end for
        
    print(buckets)






# runtests(SortTab)

T1 = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
P1 = [(1, 5, 0.75), (4, 8, 0.25)]
SortTab(T1, P1)