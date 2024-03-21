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

# sorting numbers < 0, 1 )
def bucket_index(ele, n):
    return floor(n*ele)

def bucket_sort(tab):
    n = len(tab)

    sortedTab = [0]*n
    sortedIndex = 0

    # i-th bucket represents interval from < i/n, (i+1)/n ) 
    buckets: list[list[float]] = [[0.0] for _ in range(n)]

    for ele in tab:
        buckets[bucket_index(ele, n)].append(ele)
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
    testTab = [randint(0, n - 1) / n for _ in range(n)]
    print("unsorted:")
    print(testTab, end='\n\n')
    
    testTab = bucket_sort(testTab)
    print("sorted:")
    print(testTab)