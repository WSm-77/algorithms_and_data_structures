# Dane są 2 tablice (niekoniecznie tej samej długości). Proszę znaleźć długość najdłuższego wspólnego podciągu.

from random import randint

def longest_common_subsequence(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)

    if n1 == 0 or n2 == 0:
        return 0

    lcsTab = [[0 for _ in range(n2)] for _ in range(n1)]

    for R in range(n1):
        lcsTab[R][0] = 1 if tab1[R] == tab2[0] else 0

    for C in range(n2):
        lcsTab[0][C] = 1 if tab1[0] == tab2[C] else 0

    for R in range(1, n1):
        for C in range(1, n2):
            lcsTab[R][C] = max(lcsTab[R - 1][C], lcsTab[R][C - 1])
            if tab1[R] == tab2[C]:
                lcsTab[R][C] = max(lcsTab[R][C], lcsTab[R - 1][C - 1] + 1)

    return lcsTab[n1 - 1][n2 - 1], get_sequence(lcsTab, tab1)

def get_sequence(lcsTab, tab1):
    sequence = []

    R = len(lcsTab) - 1
    C = len(lcsTab[0]) - 1

    while R != 0 and C != 0:
        if lcsTab[R][C] == lcsTab[R][C - 1]:
            C -= 1
        elif lcsTab[R][C] == lcsTab[R - 1][C]:
            R -= 1
        else:
            sequence.append(tab1[R])
            R -= 1
            C -= 1
    
    if lcsTab[R][C] == 1:
        sequence.append(tab1[R])

    sequence.reverse()

    return sequence

def test(tab1, tab2):
    lcsLen, lcsMembers = longest_common_subsequence(tab1, tab2)
    print(f"tab1: {tab1}")
    print(f"tab2: {tab2}")
    print(f"longest common subsequence lenght: {lcsLen}")
    print("longest common subsequence:", end=" ")
    print(*lcsMembers, sep=", ")

if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    tab1 = [1, 4,3, 2, 5, 7 ]
    tab2 = [0,1, 2, 5, 4,6,7 ]
    test(tab1, tab2)

    print("\n\n######## test 2 ########\n\n")

    tab1 = [randint(1, 10) for _ in range(randint(5, 8))]
    tab2 = [randint(1, 10) for _ in range(randint(5, 8))]
    test(tab1, tab2)
