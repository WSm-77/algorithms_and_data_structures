from math import floor
from random import randint

def insertion_sort(tab, tabLen):
    for i in range(1, tabLen):
        tab[0] = tab[i]
        j = i
        while tab[j - 1] > tab[0]:
            tab[j] = tab[j - 1]
            j -= 1
        #end while
        tab[j] = tab[0]
    #end for

# sorting numbers < intervalStart, intervalEnd )
def bucket_index(val, tabLen, intervalStart, intervalEnd):
    # return floor(val*tabLen)
    return floor((val - intervalStart)*tabLen / (intervalEnd - intervalStart))

def bucket_sort(tab, intervalStart, intervalEnd):
    n = len(tab)

    sortedTab = [0]*n
    sortedIndex = 0

    # i-th bucket represents interval from < intervalStart + (i*intervalSize)/n, intervalStart + ((i+1)*(intervalSize))/n ) 
    buckets: list[list[float]] = [[0.0] for _ in range(n)]

    for ele in tab:
        # buckets[bucket_index(ele, n)].append(ele)
        buckets[bucket_index(ele, n, intervalStart, intervalEnd)].append(ele)
    #end for
    
    for bucket in buckets:
        bucketSize = len(bucket)
        insertion_sort(bucket, bucketSize)
        for i in range(1, bucketSize):
            sortedTab[sortedIndex] = bucket[i]
            sortedIndex += 1
        #end for
    #end for
    return sortedTab
            
if __name__ == "__main__":
    n = 20
    intervalStart = 2
    intervalEnd = 4
    precision = 1000
    testTab = [randint(intervalStart*precision, intervalEnd*(precision - 1)) / (precision) for _ in range(n)]
    print("unsorted:")
    print(testTab, end='\n\n')

    testTab = bucket_sort(testTab, intervalStart, intervalEnd)
    print("sorted:")
    print(testTab)