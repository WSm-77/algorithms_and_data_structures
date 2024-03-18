# Proszę zaimplementować algorytm QuickSort bez użycia rekurencji (ale można wykorzystać własny stos).

from random import randint

class StackElem:
    def __init__(self, val = None, prev = None) -> None:
        self.val = val
        self.prev = prev

class Stack:
    myTop: StackElem = None
    
    def top(self):
        return self.myTop.val if not self.isEmpty() else None
        
    def pop(self):
        topVal = self.top()
        self.myTop = self.myTop.prev
        return topVal

    def append(self, val):
        new = StackElem(val, self.myTop)
        self.myTop = new

    def isEmpty(self):
        return self.myTop == None
        

def quick_sort_it(tab: list):
    n = len(tab)
    myStack = Stack()
    beg = 0
    end = n - 1
    myStack.append((beg, end))

    while not myStack.isEmpty():
        beg, end = myStack.pop()
        pivot = partition(tab, beg, end)
        if pivot + 1 < end:
            myStack.append((pivot + 1, end))

        if beg < pivot - 1:
            myStack.append((beg, pivot - 1))

def quick_sort_rek(tab, beg, end):
    if beg < end:
        pivot = partition(tab, beg, end)
        quick_sort_rek(tab, beg, pivot - 1)
        quick_sort_rek(tab, pivot + 1, end)
        

def partition(tab, beg, end):
    i = beg - 1

    for j in range(beg, end):
        if tab[j] < tab[end]:
            i += 1
            tab[j], tab[i] = tab[i], tab[j]

    tab[i + 1], tab[end] = tab[end], tab[i + 1]
    return i + 1        


if __name__ == "__main__":
    testTab = [randint(1, 50) for _ in range(randint(5, 10))]
    testTabCopy = [testTab[i] for i in range(len(testTab))]
    print(f"original testTab:\n{testTab}\n")
    quick_sort_rek(testTab, 0, len(testTab) - 1)
    print(f"sorted testTab (rek):\n{testTab}\n")
    quick_sort_it(testTabCopy)
    print(f"sorted testTab (it):\n{testTabCopy}\n")