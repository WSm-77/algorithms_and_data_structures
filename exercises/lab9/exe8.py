# Dana jest szachownica A o wymiarach n × n. Szachownica zawiera liczby wymierne. Należy przejść z pola (1,1)
# na pole (n,n) korzystając jedynie z ruchów "w dół" oraz "w prawo". Wejście na dane pole kosztuje tyle, co
# znajdująca się tam liczba. Proszę podać algorytm znajdujący trasę o minimalnym koszcie.

from random import randint

def chess_travel(board: list[list[int]]):
    n = len(board)
    INF = float("inf")

    travelCost = [[INF for _ in range(n)] for _ in range(n)]
    # parents = [[None for _ in range(n)] for _ in range(n)]
    travelCost[0][0] = board[0][0]

    for RC in range(1, n):
        travelCost[0][RC] = travelCost[0][RC - 1] + board[0][RC]
        travelCost[RC][0] = travelCost[RC - 1][0] + board[RC][0]

    for R in range(1, n):
        for C in range(1, n):
            if travelCost[R][C - 1] < travelCost[R - 1][C]:
                travelCost[R][C] = travelCost[R][C - 1]
            else:
                travelCost[R][C] = travelCost[R - 1][C]

            travelCost[R][C] += board[R][C]

    return travelCost[n - 1][n - 1], get_path(travelCost)

def get_path(travelCost):
    n = len(travelCost)

    R = n - 1
    C = n - 1

    path = set([(R, C), (0, 0)])

    while R != 0 and C != 0:
        if travelCost[R - 1][C] < travelCost[R][C - 1]:
            path.add((R - 1, C))
            R -= 1
        else:
            path.add((R, C - 1))
            C -= 1

    if R == 0:
        while C > 0:
            path.add((0, C))
            C -= 1
    else:
        while R > 0:
            path.add((R, 0))
            R -= 1

    return path

def test(testBoard):
    print("board:")
    print(*testBoard, sep="\n")
    n = len(testBoard)
    travelCost, path = chess_travel(testBoard)
    print(f"minimal cost to reach ({n - 1}, {n - 1}) equals: {travelCost}")
    print("path:")
    print("+", '-'*(2*n+1), "+", sep="")
    for R in range(n):
        print("| ", end="")
        for C in range(n):
            if (R, C) in path:
                print(testBoard[R][C], end=" ")
            else:
                print(" ", end=" ")
        print("|")
    print("+", '-'*(2*n+1), "+", sep="")


if __name__ == "__main__":
    n = randint(3,4)
    testBoard = [[randint(1, 9) for _ in range(n)] for _ in range(n)]

    test(testBoard)