from test3 import runtests

def selection_sort(tab):
    n = len(tab)

    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if tab[j] < tab[minIndex]:
                minIndex = j
            #end if
        #end for
        tab[i], tab[minIndex] = tab[minIndex], tab[i]
    #end for

def SortTab(T, P):
    n = len(T)

    buckets = [[] for _ in range(n)]

    for i in range(n):
        index = int(T[i]) - 1
        buckets[index].append(T[i])
    #end for
    
    # print(buckets)

    idx = 0
    for bucket in buckets:
        selection_sort(bucket)
        # print(bucket)
        for num in bucket:
            T[idx] = num
            idx += 1
        #end for
    #end for
            
    # print(T)


runtests(SortTab)

# T1 = [6.1, 1.5, 1.2, 3.5, 4.5, 2.5, 3.9, 7.8]
# P1 = [(1, 5, 0.75), (4, 8, 0.25)]
# SortTab(T1, P1)