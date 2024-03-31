# Proszę zaimplementować funkcję: int SumBetween(int T[], int from, int to, int n); Zadaniem tej funkcji jest obliczyć sumę liczb 
# z n elementowej tablicy T, które w posortowanej tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można 
# przyjąć, że liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych). Zaimplementowana funkcja 
# powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność czasową (oraz bardzo krótko uzasadnić to oszacowanie).

from random import randint

def quick_select(tab, beg, end, position):
    while beg < end:
        pivot = partition(tab, beg, end)
        if pivot == position:
            return
        elif pivot < position:
            beg = pivot + 1
        else:
            end = pivot - 1
        #end if
    #end while
            
def partition(tab, beg, end):
    i = beg

    for j in range(beg, end):
        if tab[j] < tab[end]:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
    
    tab[end], tab[i] = tab[i], tab[end]
    return i

def SumBetween(T, intFrom, intTo):
    n = len(T)
    quick_select(T, 0, n - 1, intFrom)
    quick_select(T, intFrom + 1, n - 1, intTo)

    sumBetween = 0

    for i in range(intFrom, intTo + 1):
        sumBetween += T[i]
    #end for
    
    return sumBetween

def test_result(tabLen, correct, output):
    print(f"tabLen: {tabLen}")
    print(f"correctAnswer:    {correct}")
    print(f"algorithmOutput:  {output}")
    if correct == output:
        print("test PASSED")
    else:
        print("test FAILED")

if __name__ == "__main__":

    ######### test 1 #########

    print("test1\n")
    n = 10
    myRange = 100
    testTab = [randint(1, myRange) for _ in range(n)]
    intFrom = randint(0, n // 2)
    intTo = randint(intFrom + 1, n - 1)
    print(testTab)
    correctAnswer = sum(sorted(testTab)[intFrom:intTo + 1])
    algorithmOutput = SumBetween(testTab, intFrom, intTo)
    test_result(n, correctAnswer, algorithmOutput)

    ######### test 2 #########

    print("\ntest2\n")
    n = 100000
    myRange = 1_000_000_000
    testTab = [randint(1, myRange) for _ in range(n)]
    intFrom = randint(0, n // 2)
    intTo = randint(intFrom + 1, n - 1)
    correctAnswer = sum(sorted(testTab)[intFrom:intTo + 1])
    algorithmOutput = SumBetween(testTab, intFrom, intTo)
    test_result(n, correctAnswer, algorithmOutput)