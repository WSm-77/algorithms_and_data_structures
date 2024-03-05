# Wiktor Sędzimir
#
# opis:
# Algorytm w zależności od wielkości "k" w stosunku do "n" korzysta z merge sorta lub odmiany selection sorta (wybiera szybszy algorytm).
# Złożoność czasowa zmodyfikowanej wersji selection sorta wynosi O(n*k). Wówczas dla:
# 1) k = O(1) jego złożoność wynosi O(n), więc jest lepsza od złożoności merge sorta,
# 2) k = O(log n) jego złożoność wynosi O(n*log n), więc jest porównywalna ze złożonością merge sorta,
# 3) k = O(n) jego złożoność wynosi O(n*n), więc jest gorsza od złożoności merge sorta.
# Zmodyfikowana wersja selection sorta działa na podobnej zasadzie co wersja oryginalna, tylko zamiast przeszukiwać listę do końca
# w celu znalezienia minimum przeszukuje jedynie "k" elementów w przód, ponieważ specyfika k-chaotycznej listy daje nam gwarancję
# znalezienia wśród tych "k" liczb minimum

from zad1testy import Node, runtests

def linked_list_len(ptr: Node) -> int:
    listLen = 0
    while ptr != None:
        listLen += 1
        ptr = ptr.next
    #end while
    return listLen

def log2(number: int) -> int:
    result = -1
    val = 1
    while val <= number:
        result += 1
        val *= 2
    #end while
    return result

def modified_selection_sort(p: Node, k: int) -> Node:
    guradian = Node()
    guradian.next = p
    sortedBeg = Node()
    sortedEnd = sortedBeg
    while guradian.next != None:
        mini = guradian
        p = guradian.next
        cnt = 1
        while p.next != None and cnt <= k:
            if p.next.val < mini.next.val:
                mini = p 
            p = p.next
            cnt += 1
        #end while
        sortedEnd.next = mini.next
        mini.next = mini.next.next
        sortedEnd = sortedEnd.next
        sortedEnd.next = None
    #end while
    return sortedBeg.next

def merge_sort(ptr: Node) -> Node:
    if ptr == None or ptr.next == None:
        return ptr
    #end if
    midPtr = linked_list_middle(ptr)
    tmp = midPtr
    midPtr = midPtr.next
    tmp.next = None
    list1 = merge_sort(ptr)
    list2 = merge_sort(midPtr)
    return merge_sorted_linked_lists(list1, list2)

def merge_sorted_linked_lists(list1: Node, list2: Node) -> Node:
    guardian = Node()
    last = guardian
    while list1 != None and list2 != None:
        if list1.val < list2.val:
            last.next = list1
            list1 = list1.next
        else:
            last.next = list2
            list2 = list2.next
        #end if
        last = last.next
        last.next = None
    #end while
    remaining = list1
    if list2 != None:
        remaining = list2
    #end if
    last.next = remaining
    return guardian.next

def linked_list_middle(ptr: Node) -> Node:
    slow = ptr
    fast = ptr.next
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    #end while
    return slow

def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    if k == 0:
        return p
    n = linked_list_len(p)
    result = None
    if k < log2(n):
        result = modified_selection_sort(p, k)
    else:
        result = merge_sort(p)
    #end if
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
