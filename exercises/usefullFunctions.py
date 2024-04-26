class Node:
    def __init__(self, v = None, n = None) -> None:
        self.val = v
        self.next = n

    def __repr__(self) -> str:
        return f"Node({self.val})"

##################
# guardian lists #
##################

def guardian_pop(g):
    if g.next == None:
        return g
    start = g
    while g.next.next != None:
        g = g.next
    #end while
    g.next = None
    return start
        
def list_to_linked_list(elemList):
    guardian = Node(None, None)
    ptr = guardian
    for ele in elemList:
        ptr.next = Node(ele)
        ptr = ptr.next
    #end for
    return guardian

def list_to_linked_list_with_cycle(elemList, startOfCycle):         #startOfCycle is indexed from 0
    N = len(elemList)
    assert(0 < startOfCycle < N)
    guradian = Node(None, None)
    ptr = guradian
    ptrToStart = None
    for i in range(N):
        ptr.next = Node(elemList[i], None)
        ptr = ptr.next
        if i == startOfCycle:
            ptrToStart = ptr
        #end if
    #end for
    ptr.next = ptrToStart
    return guradian

def print_guardian_list(ptr):
    print("GUARDIAN", end=' -> ')
    while ptr.next != None:
        print(ptr.next.val, end=' -> ')
        ptr = ptr.next
    #end while
    print("END")

def print_guardian_number(ptr, myEnd = '\n'):
    while ptr.next != None:
        print(ptr.next.val, end='')
        ptr = ptr.next
    #end while
    print(end=myEnd)

def guardian_append(ptr, element):
    begining = ptr
    while ptr.next != None:
        ptr = ptr.next
    #end while
    ptr.next = Node(element)
    return begining

def guradian_list_len(linkedList):
    cnt = 0
    while linkedList.next != None:
        cnt += 1
        linkedList = linkedList.next
    #end while
    return cnt

def init_guradian_list():
    return Node(None, None)

def remove_guradian(g):
    tmp = g.next
    g.next = None
    return tmp

######################
# non-guradian lists #
######################
        
def pop(ptr):
    if ptr == None:
        return None
    elif ptr.next == None:
        return None
    originalPtr = ptr
    while ptr.next.next != None:
        ptr = ptr.next
    #end while
    ptr.next = None
    return originalPtr

def print_list(ptr):
    while ptr != None:
        print(ptr.val, end=' -> ')
        ptr = ptr.next
    #end while
    print("END")

def print_number(ptr):
    print("your number:")
    if ptr == None:
        print("list is empty")
    while ptr != None:
        print(ptr.val, end='')
        ptr = ptr.next
    #end while
    print()
