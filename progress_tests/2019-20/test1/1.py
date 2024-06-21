# Polecenie:
#
# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz. Cyfra wielokrotna to taka, która w liczbie 
# występuje więcej niż jeden raz. Mówimy, że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje 
# więcej cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta liczba, która posiada mniej 
# cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 
# są jednakowo ładne. Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję: pretty_sort(T), która sortuje 
# elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu 
# umieścić 1-2 zdaniowy opis algorytmu oraz proszę oszacować jego złożoność czasową.

# Imię Nazwisko
#
# Opis algorytmu:
# Dla każdej liczby obliczamy ile występuje w niej cyfr pojednyczych oraz wielokrotnych. Następnie na bazie radix sorta sorutjemy
# najpierw po liczbie cyfr wielokrotnych a następnie po liczbie cyfr pojedynczych.
# Złożoność algorymu: O(n), gdzie n to długość tablicy.

from random import randint

class TabElem:
    def __init__(self, val) -> None:
        self.val = val
        self.singular, self.plural = number_prettyness(val)

def number_prettyness(number):
    digits = [0]*10
    singularCnt = 0
    pluralCnt = 0

    while number > 0:
        currentDigit = number % 10
        if digits[currentDigit] == 0:
            singularCnt += 1
            digits[currentDigit] += 1
        elif digits[currentDigit] == 1:
            singularCnt -= 1
            pluralCnt += 1
            digits[currentDigit] += 1
        #end if
        number //= 10

    return singularCnt, pluralCnt

def print_tab(Tcp):
    n = len(Tcp)
    for i in range(n):
        print(f"{Tcp[i].val} {Tcp[i].singular} {Tcp[i].plural}")

def pretty_sort(T):
    n = len(T)

    Tcp = [TabElem(T[i]) for i in range(n)]

    ######################################
    # sorting by number of plural digits #
    ######################################
    
    pluralCnt = [0]*10
    sortedTab = [None]*n

    for i in range(n):
        pluralCnt[Tcp[i].plural] += 1
    #end for
        
    for i in range(1, 10):
        pluralCnt[i] += pluralCnt[i - 1]
    #end for
        
    # print(pluralCnt)

    for i in range(n - 1, -1, -1):
        pluralCnt[Tcp[i].plural] -= 1
        sortedTab[pluralCnt[Tcp[i].plural]] = Tcp[i]
    #end for
    
    # print_tab(sortedTab)

    ########################################
    # sorting by number of singular digits #
    ########################################

    singularCnt = [0]*10

    for i in range(n):
        singularCnt[sortedTab[i].singular] += 1
    #end for
        
    for i in range(8, -1, -1):
        singularCnt[i] += singularCnt[i + 1]
    #end for
        
    for i in range(n - 1, -1, -1):
        singularCnt[sortedTab[i].singular] -= 1
        T[singularCnt[sortedTab[i].singular]] = sortedTab[i].val
    #end for
        
    ###########
    # testing #
    ###########
        
def is_pretty_sorted(tab):
    n = len(tab)
    prettynessTab: list[tuple] = [number_prettyness(number) for number in tab]
    # print(prettynessTab)

    for i in range(1, n):
        if prettynessTab[i][0] > prettynessTab[i - 1][0]:
            return False
        elif prettynessTab[i][0] == prettynessTab[i - 1][0] and prettynessTab[i][1] < prettynessTab[i - 1][1]:
            return False
    
    return True

if __name__ == "__main__":
    
    ############ test 1 ############

    print("test 1\n")
    testTab = [123, 455, 1266, 114577, 2344, 67333]
    print(testTab)
    pretty_sort(testTab)
    print(testTab)

    ############ test 2 ############

    n = 100_000
    testTab = [randint(100, 1_000_000_000_000_000) for _ in range(n)]
    print("\ntest2\n")

    pretty_sort(testTab)
    print("sorted")
    if is_pretty_sorted(testTab):
        print("test PASSED")
    else:
        print("test FAILED")