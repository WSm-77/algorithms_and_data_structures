# Wiktor Sędzimir

# Opis algorytmu:
# Zdefiniujmy kilka funkcji:
# f(r, c) ~ maksymalna liczba komnat, które Jonasz może odwiedzić dowolnie docierając do komnaty (r, c)
# (oczywiście z uwzględnieniem zasad poruszania się)
# up(r, c) ~ maksymalna liczba komnat, które Jonasz może odwiedzić docierając do komnaty (r, c) przychodząc z "górnej" komnaty
# down(r, c) ~ maksymalna liczba komnat, które Jonasz może odwiedzić docierając do komnaty (r, c) przychodząc z "dolnej" komnaty
# left(r, c) ~ maksymalna liczba komnat, które Jonasz może odwiedzić docierając do komnaty (r, c) przychodząc z "lewej" komnaty
#
# Rozważając po kolei te funkcje otrzumjemy ich wzory:
# f(r, c) = max(up(r, c), down(r, c), left(r, c)) ~ do komnaty możmy wejść w dowolny sposób
#
# up(r, c) = max(up(r - 1, c), left(r - 1, c)) + 1 ~ do komanty dostjemy się z górnej komnaty, do której mogliśmy się dostać przychodząc
# z góry albo z lewej (jeżeli przyszlibyśmy z dołu to w następnym kroku cofnelibyśmy się do komnaty (r, c) co jest niedozwolone)
#
# down(r, c) = max(down(r + 1, c), left(r + 1, c)) + 1 ~ do komanty dostjemy się z górnej komnaty, do której mogliśmy się dostać przychodząc
# z dołu albo z lewej (jeżeli przyszlibyśmy z góry to w następnym kroku cofnelibyśmy się do komnaty (r, c) co jest niedozwolone)
#
# left(r, c) = f(r, c - 1) + 1 ~ do komnaty dostajemy się z lewej komnaty, do której mogliśmy się dostać w dowolny sposób
#
# Algorytm wyznacza wartości tych funkcji dla każdej komnaty z uwzglęnieniem komnat, że jeżeli nie możemy dostać się do komnaty (r, c)
# poruszając się w dany sposób (przychodząc z góry, lewej bądź z dołu w zależności od rozważanej funkcji) to wartość tej funkcji jest
# równa -1.
#
# Złożoność:
# Algorytm ma złożoność zarówno obliczeniową jak i pamięciową równą O(n^2), ponieważ tworzymy 4 macierze n x n a następnie przechodzimy
# po wszystkich wierszach w każdej kolumnie labiryntu po dwa razy (idąc wierszami najpierw w dół a potem do góry).

from zad7testy import runtests

def maze( L ):
    n = len(L)

    # UP[R][C] - we enter (R, C) square from "UP"
    UP = [[None for _ in range(n)] for _ in range(n)]

    # DOWN[R][C] - we enter (R, C) square from "DOWN"
    DOWN = [[None for _ in range(n)] for _ in range(n)]

    # LEFT[R][C] - we enter (R, C) square from "LEFT"
    LEFT = [[None for _ in range(n)] for _ in range(n)]

    # F[R][C] - max visited chambers
    F = [[None for _ in range(n)] for _ in range(n)]

    F[0][0] = UP[0][0] = DOWN[0][0] = LEFT[0][0] = 0

    for R in range(1, n):
        F[R][0] = -1 if L[R][0] == "#" or F[R - 1][0] == -1 else R
        UP[R][0] = F[R][0]
        DOWN[R][0] = -1
        LEFT[R][0] = -1

    for C in range(1, n):
        UP[0][C] = -1
        LEFT[0][C] = F[0][C - 1] + 1 if F[0][C - 1] != -1 and L[0][C] != "#" else -1
        F[0][C] = LEFT[0][C]

        for R in range(1, n):
            if L[R][C] == "#":
                F[R][C] = UP[R][C] = DOWN[R][C] = LEFT[R][C] = -1
            else:
                LEFT[R][C] = F[R][C - 1] + 1 if F[R][C - 1] != -1 else -1
                maxVisitedUp = max(UP[R - 1][C], LEFT[R - 1][C])
                UP[R][C] = maxVisitedUp + 1 if maxVisitedUp != -1 else -1

        F[n - 1][C] = max(UP[n - 1][C], LEFT[n - 1][C])
        DOWN[n - 1][C] = -1
        for R in range(n - 2, -1, -1):
            if L[R][C] == "#":
                continue
            maxVisitedUp = max(DOWN[R + 1][C], LEFT[R + 1][C])
            DOWN[R][C] = maxVisitedUp + 1 if maxVisitedUp != -1 else -1
            F[R][C] = max(UP[R][C], DOWN[R][C], LEFT[R][C])


    return F[n - 1][n - 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )