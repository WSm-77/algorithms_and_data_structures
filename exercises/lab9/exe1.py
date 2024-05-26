# znaleźć najdłuższy rosnący podciąg

from random import randint

def longest_increasing_subsequence(tab: list[int]):
    n = len(tab)
    lengths = [1 for _ in range(n)]
    parents = [None for _ in range(n)]
    maxLength = 0
    lastElemIdx = 0

    for i in range(1, n):
        for j in range(i):
            if tab[j] < tab[i] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                parents[i] = j
        if maxLength < lengths[i]:
            maxLength = lengths[i]
            lastElemIdx = i
        # print()

    return maxLength, lastElemIdx, parents

def get_path(parents, idx, tab):
    path = []
    while idx != None:
        path.append(tab[idx])
        idx = parents[idx]

    path.reverse()
    return path

def test(testTab):
    print(f"testTab: {testTab}")
    maxLength, lastElemIdx, parents = longest_increasing_subsequence(testTab)
    print(f"maxLenght: {maxLength}")
    path = get_path(parents, lastElemIdx, testTab)
    print(*path, sep=" -> ")

if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    testTab = [2,3,6,1,4,7,8,5]
    test(testTab)

    print("\n\n######## test 2 ########\n\n")

    testTab = [randint(1,20) for _ in range(randint(8,15))]
    test(testTab)