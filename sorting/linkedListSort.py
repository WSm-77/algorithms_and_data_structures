from random import randint

class Node:
    def __init__(self, v = None, n = None) -> None:
        self.val = v
        self.next = n

def list_to_lined_list(tab: list) -> Node:
    n = len(tab)
    root = Node()
    if n == 0:
        return root
    #end if
    root.val = tab[0]
    ptr = root
    for i in range(1, n):
        ptr.next = Node(tab[i])
        ptr = ptr.next
    #end for
    return root

def print_list(ptr: Node) -> None:
    while ptr != None:
        print(ptr.val, end=" -> ")
        ptr = ptr.next
    #end while
    print("END")

def linked_list_selection_sort(ptr: Node) -> Node:
    guardian = Node(n = ptr)
    new = Node()
    last = new
    while guardian.next != None:
        currentNode = guardian
        mini = currentNode
        while currentNode.next != None:
            if currentNode.next.val < mini.next.val:
                mini = currentNode
            #end if
            currentNode = currentNode.next
        #end while
        tmp = mini.next
        mini.next = mini.next.next
        last.next = tmp
        last = last.next
        tmp.next = None
    #end while
    return new.next

def linked_list_merge_sort(ptr: Node) -> Node:
    if ptr == None or ptr.next == None:
        return ptr
    #end if
    midPtr = linked_list_middle(ptr)
    tmp = midPtr
    midPtr = midPtr.next
    tmp.next = None
    list1 = linked_list_merge_sort(ptr)
    list2 = linked_list_merge_sort(midPtr)
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

if __name__ == "__main__":
    tab = [randint(1, 100) for _ in range(randint(8, 15))]
    root1 = list_to_lined_list(tab)
    tab = [randint(1, 100) for _ in range(randint(8, 15))]
    root2 = list_to_lined_list(tab)
    print("list1: ", end="")
    print_list(root1)
    print("list2: ", end="")
    print_list(root2)

    ##########  middle value  ##########
    list1Mid = linked_list_middle(root1)
    print(f"list1 middle value: {list1Mid.val}")

    ##########  selection sort  ##########
    root1 = linked_list_selection_sort(root1)
    print("sorted list1: ", end="")
    print_list(root1)

    ##########  merge sort  ##########
    root2 = linked_list_merge_sort(root2)
    print("sorted list2: ", end="")
    print_list(root2)

    ##########  merging 2 lists  ##########
    mergedList = merge_sorted_linked_lists(root1, root2)
    print("merged: ", end="")
    print_list(mergedList)
