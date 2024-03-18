# Proszę zaproponować algorytm scalający k posortowanych list.

import sys
from random import randint
sys.path.insert(0, '/home/wiktor/university/ASD/exercises')
from usefullFunctions import Node, list_to_linked_list, remove_guradian, print_list


class Node:
  def __init__(self, val = None, next = None):
    self.val = val
    self.next = next

def merge_k_sorted_linked_lists(lists: list[Node]) -> Node:
    n = len(lists)
    
    while n > 1:
        mergedLists = []

        for i in range(0, n, 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < n else None
            mergedLists.append(merge(l1, l2))
        #end for
        
        lists = mergedLists
        n = len(lists)
    #end while
        
    return lists[0]
       
def merge(l1: Node, l2: Node) -> Node:
    guradian = Node()
    last = guradian
    
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            last.next = l1
            l1 = l1.next
        else:
            last.next = l2
            l2 = l2.next
        #end if
        last = last.next
    #end while
    
    if l1 != None:
        last.next = l1
    else:
        last.next = l2
    #end if
    
    return guradian.next

if __name__ == "__main__":
    tab = [remove_guradian(list_to_linked_list(sorted([randint(1, 100) for _ in range(randint(1,5))]))) for _ in range(8, 15)]
    for i in range(len(tab)):
        print_list(tab[i])
    #end for
    print_list(merge_k_sorted_linked_lists(tab))