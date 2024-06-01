# Rozważmy ciąg (ao,..., an-1) liczb naturalnych. Załóżmy, że został podzielony na k spójnych podciągów: 
# (ao,..., a l1), (a l1 + 1,..., a l2 ), . . ., (a lk-1+1, ... ‚a n-1). Przez wartość i-go podciągu rozumiemy sumę 
# jego elementów, a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości (rozstrzygając remisy 
# w dowolny sposób). Wartością podziału jest wartość jego najgorszego podciągu. Proszę zaproponować algorytm 
# znajdujący podział ciągu (ao,..., ɑn-1) o maksymalnej wartości.
#
# Rozwiązanie:
# Rozważmy funkcję f(divIdx, currEnd), która zwraca maksymalną wartość podziału liczb z zakresu 0 ~ currEnd na divIdx + 1 
# przedziałów. Aby wyznaczyć wartość tej funkcji rozważamy podziały na divIdx przedziałów liczb z zakresu 0 ~ prevDivEnd
# (prevDivEnd jest z przedziału <divIdx, currEnd - 1>, bo poprzedzni podział mógł się kończyć na indeksach z tych zakresów).
# Do każdego z tych podziałów dokładamy jeden kolejny przedział, zawierający liczby z zakresu od prevDivEnd + 1 do currEnd.
# Nowa wartość funkcji jest równa mimimum z wartości poprzedniego popdziału i wartości nowego przedziału.
#
# Przykład:
#
# testTab = [2,1,3,6]
# k = 2
#
# Najlepsze podziały:
# Indeksy:               0        1            2              3 
# dla k = 1:            [2]     [2,1]       [2,1,3]       [2,1,3,6]
# dla k = 2:             X      [2],[1]     [2,1],[3]         ?
#
# Jeżeli chcemy wyznaczyć wartość funkcji f[1][3] (pole oznaczone "?") rozważamy podział na 1 przedział, do którego dokładamy
# nowy przedział. W naszym przypadku rozważamy trzy możliwości:
#
# 1) do podziału [2] dodajemy nowy przedział [1,3,6]; wartość nowego podziału jest równa 2
# 2) do podziału [2,1] dodajemy nowy przedział [3,6]; wartość nowego podziału jest równa 3
# 3) do podziału [2,1,3] dodajemy nowy przedział [6]; wartość nowego podziału jest równa 6
#
# Zatem w naszym przypadku, aby zmaksymalizować wartość podziału wybierzemy trzecią opcję tworząc podział:
# ? = [2,1,3],[6]

from random import randint

INF = float("inf")

def division(tab, k):
    n = len(tab)
    f = [[-INF for _ in range(n)] for _ in range(k)]
    parents = [[None for _ in range(n)] for _ in range(k)]

    # prefixSum[i] stores sum of first "i" elements of "tab"
    # used for quickly calculate sum of elements from "j-th" to "i-th" element with formula: prefisSum[i] - prefixSum[j-1] 
    prefixSum = [0 for _ in range(n)]

    f[0][0] = prefixSum[0] = tab[0]
    for numIdx in range(1, n):
        f[0][numIdx] = prefixSum[numIdx] = prefixSum[numIdx - 1] + tab[numIdx]
        parents[0][numIdx] = numIdx - 1


    # divisionsIdx: 0 ~ 1 division, 1 ~ 2 divisions, ..., k - 1 ~ k divisions
    for divisionsIdx in range(1, k):
        for currentDivisionEnd in range(divisionsIdx, n):
            for previousDivisionEnd in range(divisionsIdx - 1, currentDivisionEnd):
                currentDivisionSum = prefixSum[currentDivisionEnd] - prefixSum[previousDivisionEnd]
                previousDivisionValue = f[divisionsIdx - 1][previousDivisionEnd]

                currentDivisionValue = min(currentDivisionSum, previousDivisionValue)
                if f[divisionsIdx][currentDivisionEnd] < currentDivisionValue:
                    f[divisionsIdx][currentDivisionEnd] = currentDivisionValue
                    parents[divisionsIdx][currentDivisionEnd] = previousDivisionEnd

    return get_divisions(tab, parents, k - 1, n - 1), f[k - 1][n - 1]

def get_divisions(tab, parents, divisionIdx, divisionEnd):
    divs = []
    while divisionIdx > 0:
        prevDivisionEnd = parents[divisionIdx][divisionEnd]
        if prevDivisionEnd == None:
            break
        divs.append(tab[prevDivisionEnd + 1:divisionEnd + 1])
        divisionIdx -= 1
        divisionEnd = prevDivisionEnd
    

    divs.append(tab[:divisionEnd + 1])
    divs.reverse()

    return divs

def test(testTab, k):
    print(f"tab: {testTab}")
    print(f"k = {k}\n")
    divs, minSum = division(testTab, k)
    print(f"division value: {minSum}")
    print(f"divisions: {divs}")

if __name__ == "__main__":
    print("######## test 1 ########\n\n")
    testTab = [2,1,3,6]
    k = 2
    test(testTab, k)

    print("\n\n######## test 2 ########\n\n")
    testTab = [2,1,3,6,4]
    k = 3
    test(testTab, k)

    print("\n\n######## test 3 ########\n\n")
    testTab = [10, 4, 7, 10, 1, 3, 6]
    k = 4
    test(testTab, k)

    print("\n\n######## test 4 ########\n\n")
    testTab = [8, 4, 4, 3, 7]
    k = 3
    test(testTab, k)

    print("\n\n######## test 5 ########\n\n")
    n = randint(5,10)
    testTab = [randint(1,10)  for _ in range(n)]
    k = randint(2, n)
    test(testTab, k)

    