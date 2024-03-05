# Wiktor Sędzimir
#
# opis: (uzupełnić)
#

from zad1testy import Node, runtests


def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    if k == 0:
        return p
    guradian = Node()
    guradian.next = p
    sortedBeg = Node()
    sortedEnd = sortedBeg
    while guradian.next != None:
        mini = guradian
        p = guradian
        cnt = 0
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


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
