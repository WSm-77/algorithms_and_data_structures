# Zadanie 4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n-1, skacząc wyłącznie
# w kierunku większych liczb. Skok z liczby i do liczby j (j> i) kosztuje ją j-i jednostek energii, a jej energia
# nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na niektórych
# iczbach także na zerze leżą przekąski o określonej wartości energetycznej (wartość przekąski dodaje się do aktualnej
# energii żaby). Proszę zaproponować algorytm, który oblicza minimalną liczbę skoków potrzebną na dotarcie z 0 do n-1,
# mając daną tablicę A z wartościami energetycznymi przekąsek na każdej z liczb.

from random import randint

def hungry_frog(energy: list[int]) -> int:
    n = len(energy)
    INF = float("inf")

    # f[i][e] = min(f[j][e + i - j]) + 1, where j < i
    f = [[INF for _ in range(n)] for _ in range(n)]
    parents = [[None for _ in range(n)] for _ in range(n)]

    startEnergy = min(energy[0], n - 1)

    for e in range(startEnergy + 1):
        f[0][e] = 0

    for i in range(1, n):
        for j in range(i):
            for remainingEnergy in range(n - i + j):
                newEnergy = min(remainingEnergy + energy[i], n - 1)
                if f[j][remainingEnergy + i - j] + 1 < f[i][newEnergy]:
                    f[i][newEnergy] = f[j][remainingEnergy + i - j] + 1
                    parents[i][newEnergy] = (j, remainingEnergy + i - j)

    lastEnergy = 0
    minSteps = INF
    for i in range(n):
        if f[n - 1][i] < minSteps:
            minSteps = f[n - 1][i]
            lastEnergy = i

    return (minSteps, get_path(parents, lastEnergy)) if minSteps != INF else (INF, [])

def get_path(parents, energy):
    idx = len(parents) - 1

    path = []

    while True:
        path.append(idx)
        if parents[idx][energy] == None:
            break

        idx, energy = parents[idx][energy]

    path.reverse()

    return path

def test(testTab):
    print(testTab)
    minSteps, path = hungry_frog(testTab)
    print(f"min steps to reach end: {minSteps}")
    print("path:")
    print(path)

if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    testTab = [2, 1, 3, 1, 1, 1]
    test(testTab)

    print("\n\n######## test 2 ########\n\n")

    testTab = [3, 2, 3, 1, 3, 1, 1, 1]
    test(testTab)

    print("\n\n######## test 3 ########\n\n")

    testTab = [randint(0, 4) for _ in range(randint(8, 10))]
    test(testTab)
