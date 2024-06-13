# Zadanie 5 (dwuwymiarowy problem plecakowy) Proszę zaproponować algorytm dla dwuwymiarowej wersji dyskretnego problemu plecakowego.
# Mamy dany zbiór P (PP) przedmiotów i dla każdego przedmiotu p, dane są następujące trzy liczby:
# 1. v(p) wartość przedmiotu,
# 2. w(p) waga przedmiotu, oraz
# 3. h(p.)- wysokość przedmiotu.
# Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie przekracza danej liczby W oraz których łączna
# wysokość nie przekracza danej liczby H (przedmioty zapakowane są w kartony, które złodziej układa jeden na drugim). Proszę
# oszacować złożoność czasową swojego algorytmu oraz uzasadnić jego poprawność.

def knapsack_2D(values: list[int], weights: list[int], heights: list[int], W: int, H: int) -> int:
    assert(len(values) == len(weights) == len(heights))
    n = len(values)

    parents = [[[None for _ in range(H+1)] for _ in range(W+1)] for _ in range(n)]
    profits = [[[0 for _ in range(H+1)] for _ in range(W+1)] for _ in range(n)]

    for weight in range(weights[0], W + 1):
        for height in range(heights[0], H + 1):
            profits[0][weight][height] = values[0]

    for i in range(1, n):
        for weight in range(W + 1):
            for height in range(H + 1):
                # 1) we don't take this item
                profits[i][weight][height] = profits[i - 1][weight][height]
                parents[i][weight][height] = (weight, height)

                # 2) we check if we can take this item and optimize profits
                if 0 <= weight - weights[i] and 0 <= height - heights[i]:
                    newProfit = profits[i - 1][weight - weights[i]][height - heights[i]] + values[i]
                    if profits[i][weight][height] < newProfit:
                        profits[i][weight][height] = newProfit
                        parents[i][weight][height] = (weight - weights[i], height - heights[i])


    return profits[n - 1][W][H], get_itmes(profits, parents, W, H)

def get_itmes(profits, parents, weight, height):
    idx = len(parents) - 1
    itmes = []

    while idx > 0:
        newWeight, newHeight = parents[idx][weight][height]
        if newWeight != weight or newHeight != height:
            itmes.append(idx)

        weight, height = newWeight, newHeight
        idx -= 1

    if profits[0][weight][height] != 0:
        itmes.append(0)

    itmes.reverse()
    return itmes

def test(values, weights, heights, W, H):
    print(f"values: {values}")
    print(f"weights: {weights}")
    print(f"heights: {heights}")
    print(f"bounderies: maxWeight = {W}, maxHeights = {H}")
    maxProfit, items = knapsack_2D(values, weights, heights, W, H)
    print(f"max profit: {maxProfit}")
    print(f"itmes: {items}")


if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    values = [4, 10, 2, 3, 8]
    weights = [10, 4, 1, 2, 6]
    heights = [3, 9, 12, 4, 2]
    W = 12
    H = 20

    test(values, weights, heights, W, H)

    print("\n\n######## test 2 ########\n\n")

    values = [4, 10, 2, 3, 8]
    weights = [10, 6, 1, 2, 6]
    heights = [3, 9, 12, 4, 9]
    W = 12
    H = 20

    test(values, weights, heights, W, H)


