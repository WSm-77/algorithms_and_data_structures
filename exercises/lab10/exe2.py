# Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków
# [a1, b1], [a2, b2], ..., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu.
# Proszę zaproponować algorytm, który oblicza, ile klocków należy usunąć z listy tak, żeby każdy
# kolejny spadający klocek mieścił się w całości w tym, który spadł tuż przed nim.

from random import randint

def does_include(interval1: tuple[int, int], interval2: tuple[int, int]) -> bool:
    return interval1[0] <= interval2[0] and interval1[1] >= interval2[1]

def falling_blocks(blocks: list[tuple[int, int]]):
    n = len(blocks)

    f = [0 for _ in range(n)]
    parents = [None for _ in range(n)]

    for curr in range(1, n):
        for prev in range(curr):
            if does_include(blocks[prev], blocks[curr]) and f[curr] < f[prev] + 1:
                f[curr] = f[prev] + 1
                parents[curr] = prev


    maxTower = 0
    maxIdx = 0
    for i in range(1, n):
        if maxTower < f[i]:
            maxTower = f[i]
            maxIdx = i

    return (n - maxTower - 1, which_blocks(parents, maxIdx))

def which_blocks(parents, idx):
    n = len(parents)
    needsRemoval = [True for _ in range(n)]

    while idx != None:
        needsRemoval[idx] = False
        idx = parents[idx]

    return [i for i in range(n) if needsRemoval[i]]

def rand_interval(lowerBound, upperBound) -> tuple:
    intervalStart = randint(lowerBound, upperBound - 1)
    intervalEnd = randint(intervalStart + 1, upperBound)

    return (intervalStart, intervalEnd)

def test(blocks):
    print(blocks)

    howManyToRemove, whichToRemove = falling_blocks(blocks)

    print(f"remove {howManyToRemove} blocks:")
    print(whichToRemove)


if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    blocks = [(1, 10), (1, 2), (2, 8), (7, 9), (3, 7), (4, 6), (4, 5)]
    test(blocks)

    print("\n\n######## test 2 ########\n\n")

    numOfBlocks = randint(4, 10)
    blocks = [rand_interval(1, 10) for _ in range(numOfBlocks)]
    test(blocks)

