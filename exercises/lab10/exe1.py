# Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0,...,n-1. Dla każdego i € {0,...,n-1} znany jest zysk c1,
# jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu John
# znajdzie optymalny plan wycinki.

from random import randint

def cutting_plan(costs: list[int]):
    n = len(costs)
    if n == 1:
        return costs[0]

    profit = [cost for cost in costs]

    profit[1] = max(profit[0], profit[1])

    for i in range(2, n):
        profit[i] = max(profit[i - 1], profit[i - 2] + costs[i])

    return find_plan(profit), profit[-1]

def find_plan(profit):
    n = len(profit)
    toCut = []

    i = n - 1
    prevTaken = 0
    while i > 0:
        if profit[i - 1] != profit[i]:
            toCut.append(i)
            prevTaken = i
            i -= 2
        else:
            i -= 1

    if prevTaken != 1:
        toCut.append(0)

    toCut.reverse()

    return toCut

if __name__ == "__main__":
    n = randint(4,10)
    print(f"n = {n}")
    testCosts = [randint(1, 20) for _ in range(n)]
    # testCosts = [6, 4, 2, 16]
    toCut, profit = cutting_plan(testCosts)
    print(f"prices:\n{testCosts}")
    print(f"\nto get max profit of {profit}$ you should cut following trees:")
    print(toCut)
