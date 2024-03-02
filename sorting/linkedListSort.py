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

def linked_list_sort(ptr: Node) -> Node:
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

if __name__ == "__main__":
    tab = [randint(1, 100) for _ in range(randint(8, 15))]
    root1 = list_to_lined_list(tab)
    print_list(root1)
    root1 = linked_list_sort(root1)
    print_list(root1)
