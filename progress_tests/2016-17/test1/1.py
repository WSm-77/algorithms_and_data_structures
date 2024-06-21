# Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych: struct Node{ Node* next; double value; }
# Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę liczb rzeczywistych (z wartownikiem), 
# wygenerowaną zgodnie z rozkładem jednostajnym na przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja 
# powinna być możliwie jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność zaimplementowanej funkcji.

import sys
from random import randint
sys.path.insert(0, '/home/wiktor/university/ASD/exercises')
from usefullFunctions import list_to_linked_list, remove_guradian, print_guardian_list, Node

def guardian_list_len(ptr):
    listLen = 0

    while ptr.next != None:
        listLen += 1
        ptr = ptr.next
    #end while
    
    return listLen

def val_to_bucket_index(val, numberOfBuckets):
    return int(val / 10 * numberOfBuckets)

def insertion_sort(tab: list[Node]):
    n = len(tab)

    for i in range(1, n):
        tmp = tab[i]
        j = i - 1

        while j >= 0 and tab[j].val > tmp.val:
            tab[j + 1] = tab[j]
            j -= 1
        #end while
        
        tab[j + 1] = tmp
    #end for

def sort(ptr):
    n = guardian_list_len(ptr)

    buckets = [[] for _ in range(n)]

    p = ptr.next

    while p != None:
        bucketIndex = val_to_bucket_index(p.val, n)
        buckets[bucketIndex].append(p)
        p = p.next
    #end while

    p = ptr

    for bucket in buckets:
        if bucket:
            insertion_sort(bucket)
            for ele in bucket:
                p.next = ele
                p = p.next

    p.next = None

def is_sorted(ptr):
    tail = ptr.next
    
    if tail == None or tail.next == None:
        return True
    
    ptr = tail.next

    while ptr != None:
        if tail.val > ptr.val:
            return False
        
        tail = tail.next
        ptr = ptr.next
    #end while
    
    return True

def test_result(testList):
    if is_sorted(testList):
        print("test PASSED")
    else:
        print("test FAILED")

if __name__ == "__main__":

    ########### test 1 ###########

    print("test1\n")
    precision = 100
    n = 15
    print(f"number of nodes: {n}")
    testTab = [randint(0, 10*precision - 1) / precision for _ in range(n)]
    print(f"testTab: {testTab}")
    print("before sorting:")
    testList = list_to_linked_list(testTab)
    print_guardian_list(testList)
    sort(testList)
    print("after sorting:")
    print_guardian_list(testList)

    test_result(testList)

    ########### test 2 ###########

    print("\ntest2\n")
    precision = 100
    n = 100_000
    testTab = [randint(0, 10*precision - 1) / precision for _ in range(n)]
    print(f"number of nodes: {n}")
    testList = list_to_linked_list(testTab)
    sort(testList)

    test_result(testList)