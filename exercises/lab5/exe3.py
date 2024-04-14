# dana jest szachownica na której w lewym górnym rogu stoi król; każde pole szachownicy zawiera koszt wejścia na to pole; król ma dotrzeć do prawego
# dolnego rogu płacąc najmniejszy koszt; wyznaczyć ten koszt

from collections import deque
from random import randint

def print_path(pos, parents, board):
    n = len(parent)
    pathTab = [[' ' for _ in range(n)] for _ in range(n)]
    while pos != parents[pos[0]][pos[1]]:
        pathTab[pos[0]][pos[1]] = board[pos[0]][pos[1]]
        pos = parents[pos[0]][pos[1]]
    #end while
    pathTab[pos[0]][pos[1]] = board[pos[0]][pos[1]]


    print("+-", "--"*n, "+", sep="")
    for row in pathTab:
        print("| ", end="")
        print(*row, end="")
        print(" |")
    print("+-", "--"*n, "+", sep="")

def print_board(board):
    print("+-", "--"*n, "+", sep="")
    for row in board:
        print("| ", end="")
        print(*row, end="")
        print(" |")
    print("+-", "--"*n, "+", sep="")


def cost(board: list[list[int]]):
    n = len(board)
    neighbour = ((-1,-1),(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    distance: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]
    parent: list[list[tuple[int]]] = [[(0,0) for _ in range(n)] for _ in range(n)]
    visited: list[list[bool]] = [[False for _ in range(n)] for _ in range(n)]

    # we store:
    # 0: (x, y) - tuple of coordinates of point to visit
    # 1: cnt - which time we visit this vertex
    toVisit: deque = deque()
    toVisit.append(((0, 0), 1))
    visited[0][0] = True

    while len(toVisit) > 0:
        pos, cnt = toVisit.popleft()

        if cnt < board[pos[0]][pos[1]]:
            # if not visited[pos[0]][pos[1]]:
            toVisit.append((pos, cnt + 1))
        else:
            parentPos = parent[pos[0]][pos[1]]
            distance[pos[0]][pos[1]] = distance[parentPos[0]][parentPos[1]] + cnt
            for x, y in neighbour:
                neighbourPos = (pos[0] + x, pos[1] + y)
                if 0 <= neighbourPos[0] < n and 0 <= neighbourPos[1] < n:
                    if not visited[neighbourPos[0]][neighbourPos[1]]:
                        visited[neighbourPos[0]][neighbourPos[1]] = True
                        toVisit.append((neighbourPos, 1))
                        parent[neighbourPos[0]][neighbourPos[1]] = pos
            #end for
        #end if
    #end while

    return distance, parent, visited

if __name__ == "__main__":

    ############ test 1 ############

    testBoard = [[1,5,1,1],
                 [5,1,5,1],
                 [5,5,5,1],
                 [5,5,5,1]]
    
    distance, parent, visited = cost(testBoard)
    n = len(testBoard)
    print("testBoard:")
    print_board(testBoard)
    print()
    for x in range(n):
        for y in range(n):
            print(f"path to ({x}, {y}) with cost {distance[x][y]}:")
            print_path((x,y), parent, testBoard)
            print()

    # ############ test 2 ############

    n = randint(3, 8)
    testBoard = [[randint(1, 5) for _ in range(n)] for _ in range(n)]
    distance, parent, visited = cost(testBoard)

    print("testBoard:")
    print_board(testBoard)
    print()
    for x in range(n):
        for y in range(n):
            print(f"path to ({x}, {y}) with cost {distance[x][y]}:")
            print_path((x,y), parent, testBoard)
            print()