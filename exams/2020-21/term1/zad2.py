# Wiktor Sędzimir
#
# Opis algorytmu:
# Algorytm polega na stworzeniu tablicy czasów dotarcia na dane pole przy określonym kierunku poruszania się oraz przy
# określonej prędkości poruszania się robota. Rozwiązaniem jest znalezienie minimum z czasów dotarcia do pola wyznaczenego
# przez punkt "B" przy dowolnym sposobie poruszania się oraz dowolnej prędkości.
#
# Złożoność:
# Algorytm korzysta z modyfikacji algorytmu Dijkstry, dla którego złożoność wynosi O(E log V). W naszym przypadku V = n * m,
# natomiast E = (n - 1) * m + (m - 1) * n ~ n * m, gdzie n - liczba wierszy, m - liczba kolumn, więc ostateczna złożoność 
# wynosi: O(n*m*log(n*m)). 

from zad2testy import runtests
from queue import PriorityQueue

def robot( L, A, B ):
    """tu prosze wpisac wlasna implementacje"""
    # helper function
    def increase_speed(speed):
        return V2 if speed == V2 else speed + 1
    
    # only for debug purpose
    def print_times():
        nonlocal times
        for dir in range(4):
            for speed in range(3):
                print(f"######### d: {dir}, s: {speed} #########\n")
                print(*times[dir][speed], sep="\n")
                print("\n")

    ####################
    # define constants #
    ####################

    # directions
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    # speed level
    V0 = 0
    V1 = 1
    V2 = 2
    speedToTime = (60, 40, 30)

    INF = float("inf")
    
    #############
    # main code #
    #############

    rows = len(L)
    colls = len(L[0])

    # times[direction][speedLevel][row][coll]
    times = [[[[INF for _ in range(colls)] for _ in range(rows)] for _ in range(3)] for _ in range(4)]

    # 0 - time, 1 - direction, 2 - speed, 3 - row, 4 - coll
    toCheck = PriorityQueue()
    toCheck.put((0, RIGHT, V0, A[1], A[0]))
    times[RIGHT][V0][A[1]][A[0]] = 0

    while not toCheck.empty():
        time, direction, speed, row, coll = toCheck.get()

        if row == B[1] and coll == B[0]:
            # print_times()
            return time

        nextRow = row
        nextColl = coll

        ################
        # move forward #
        ################

        match direction:
            case 0:                 # go RIGHT
                nextColl += 1
            case 2:                 # go LEFT
                nextColl -= 1
            case 3:                 # go UP
                nextRow -= 1
            case 1:                 # go DOWN
                nextRow += 1

        if 0 <= nextRow < rows and 0 <= nextColl < colls and L[nextRow][nextColl] != "X":
            nextTime = time + speedToTime[speed]
            nextSpeed = increase_speed(speed)
            if nextTime < times[direction][nextSpeed][nextRow][nextColl]:
                times[direction][nextSpeed][nextRow][nextColl] = nextTime
                toCheck.put((nextTime, direction, nextSpeed, nextRow, nextColl))

        ################
        # rotate right #
        ################

        rotateTime = time + 45
        nextDirection = (direction + 1) % 4

        if rotateTime < times[nextDirection][V0][row][coll]:
            times[nextDirection][V0][row][coll] = rotateTime
            toCheck.put((rotateTime, nextDirection, V0, row, coll))

        ###############
        # rotate left #
        ###############

        nextDirection = (direction - 1) % 4

        if rotateTime < times[nextDirection][V0][row][coll]:
            times[nextDirection][V0][row][coll] = rotateTime
            toCheck.put((rotateTime, nextDirection, V0, row, coll))
    #end while

    # print_times()

    return None

    
runtests( robot )


