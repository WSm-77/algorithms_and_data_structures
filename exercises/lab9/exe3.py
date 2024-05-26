# Do domu włamał się złodziej z plecakiem o udźwigu "load", do którego będzie wkładał ukradzione przedmioty.
# Złodziej chce ukraść przedmioty o jak największej sumarycznej wartości, ale suma wag ukradzionych przedmiotów nie może
# przekroczyć wartości "load". Znaleźć maksymalną wartość ukradzionych przedmiotów.

def knapsock(weights: list[int], values: list[int], load: int):
    n = len(weights)

    # maxSums[i][w] - max value of stolen itmes, which total weight doesn't exceed load
    maxSums = [[0 for _ in range(load + 1)] for _ in range(n)]
    parents = [[0 for _ in range(load + 1)] for _ in range(n)]

    # we consider first item
    for weight in range(weights[0], load + 1):
        maxSums[0][weight] = values[0]
        parents[0][weight] = -1

    for itemId in range(1, n):
        currentWeight = weights[itemId]
        for weight in range(min(currentWeight, load + 1)):
            parents[itemId][weight] = weight
            maxSums[itemId][weight] = maxSums[itemId - 1][weight]

        for weight in range(currentWeight, load + 1):
            maxSums[itemId][weight] = maxSums[itemId - 1][weight]
            parents[itemId][weight] = weight
            if maxSums[itemId][weight] < maxSums[itemId - 1][weight - currentWeight] + values[itemId]:
                maxSums[itemId][weight] = maxSums[itemId - 1][weight - currentWeight] + values[itemId]
                parents[itemId][weight] = weight - currentWeight

    return maxSums[n - 1][load], get_itmes(parents, n - 1, load)


def get_itmes(parents, itemId, load):
    items = []

    while itemId >= 0:
        parentLoad = parents[itemId][load]
        if load != parentLoad:
            load = parentLoad
            items.append(itemId)
        itemId -= 1

    items.reverse()

    return items

def test(weights, values, load):
    maxSum, items = knapsock(weights, values, load)
    print(f"\n\nmax load: {load}\nto have max profit of {maxSum}$ take following items:")
    for item in items:
        print(f"id: {item}, weight: {weights[item]}, value: {values[item]}")

if __name__ == "__main__":
    weights = [1,4,2,6,3,7,1,2]
    values = [4,10,9,25,9,30,5,5]

    for testId in range(1, 6):
        print(f"\n\n######## test {testId} ########")
        load = testId * 5
        test(weights, values, load)
