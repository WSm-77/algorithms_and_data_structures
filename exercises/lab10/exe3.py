# Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce, żeby
# wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który wyznacza,
# które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut. Auta muszą
# wjeżdżąc w takiej kolejności, w jakiej są podane w tablicy A.

# Rozwiązanie:
# Tworzymy funkcję f(i, left, right), która określa czy możliwe jest załadowanie "i" samochodów na prom w taki sposób,
# aby na lewym pasie samochody zajmowały długość "left" a na prawym pasie długość "right".

from random import randint

def max_cars_on_ferry(carLengths: list[int], L: int | float) -> int:
    n = len(carLengths)
    if n < 1 or carLengths[0] > L:
        return 0

    # get max number of cars that possibly can fit on the ferry
    upperBound = 0
    maxSum = 2*L
    while upperBound < n:
        maxSum -= carLengths[upperBound]
        if maxSum < 0:
            break
        upperBound += 1

    f = [[[False for _ in range(L+1)] for _ in range(L+1)] for _ in range(upperBound)]
    parents = [[[None for _ in range(L+1)] for _ in range(L+1)] for _ in range(upperBound)]


    f[0][carLengths[0]][0] = f[0][0][carLengths[0]] = True

    lastLeft, lastRight = carLengths[0], 0

    result = 0
    for i in range(1, upperBound):
        carLength = carLengths[i]

        for left in range(L + 1):
            for right in range(L + 1):

                # current car chooses left lane
                if 0 <= left - carLength and f[i - 1][left - carLength][right]:
                    f[i][left][right] = True
                    result = i
                    parents[i][left][right] = (left - carLength, right)
                    lastLeft, lastRight = left, right

                # current car chooses right lane
                elif 0 <= right - carLength and f[i - 1][left][right - carLength]:
                    f[i][left][right] = True
                    result = i
                    parents[i][left][right] = (left, right - carLength)
                    lastLeft, lastRight = left, right

    return result + 1, get_choices(parents, result, lastLeft, lastRight)

def get_choices(parents, idx, left, right):
    choices = []
    while idx > 0:
        newLeft, newRight = parents[idx][left][right]
        if left != newLeft:
            choices.append("left")
        else:
            choices.append("right")

        left, right = newLeft, newRight
        idx -= 1

    if left != 0:
        choices.append("left")
    else:
        choices.append("right")

    choices.reverse()

    return choices

def test(cars, L):
    print("cars lengths:")
    print(cars)
    carsCnt, choices = max_cars_on_ferry(cars, L)
    print(f"\nfarry can take {carsCnt} cars")
    print("cars choices:")
    for i in range(carsCnt):
        print(f"{i}: {choices[i]}")

if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    cars = [3,1,3,1,2]
    L = 5
    test(cars, L)

    print("\n\n######## test 2 ########\n\n")

    cars = [3,1,3,1,3]
    L = 5
    test(cars, L)

    print("\n\n######## test 3 ########\n\n")

    cars = [4,4,4,4,4,4]
    L = 7
    test(cars, L)

    print("\n\n######## test 4 ########\n\n")

    cars = [randint(1, 5) for _ in range(10)]
    L = 10
    test(cars, L)

