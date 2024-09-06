# Opis algorytmu:
# Zdefiniujmy funkcję f(i, j) ~ minimalny kosz połączenia gniazdek od "i" do "i+2*j-1" dokłanie "j" kablami.
# Do wyznaczenia wzoru tej funkcji rozważmy dwa przypadki:
# 1) bierzemy mniejszą liczbę gniazdek (od "i+1" do "i+2*j-2") i dołączamy jeden kabel do dwóch skrajnych gniazdek

# Przykład:
# +-----+                      +-----+
# | +-+ |           +-+        |     |
# | | | |    <---   | |    +   |     |
# 7 1 3 7           1 3        7     7

# 2) rozbijamy nasz ciąg gniazdek na 2 mniejsze ciągi i rozważamy je osobno

# Przykład:
# +-----+              +-----+
# | +-+ | +-+          | +-+ |     +-+
# | | | | | |   <---   | | | |  +  | |
# 7 1 3 7 2 1          7 1 3 7     2 1

# lub

# +-+ +-+ +-+         +-+ +-+     +-+
# | | | | | |   <---  | | | |  +  | |
# 7 1 3 7 2 1         7 1 3 7     2 1


# Wzór rekurencyjny na tak opisaną funkcję:
# f(i, j) = min( f(i+1, j-1), min( f(i,k) + f(i+2*k, j-k) ) ), gdzie k należy do zbioru {1, 2, ..., j - 1}

from egz2atesty import runtests

def cost(T, beg, end):
    return abs(T[beg] - T[end]) + 1

def wired( T ):
    # tu prosze wpisac wlasna implementacje
    n = len(T) // 2

    INF  = float("inf")
    dp = [[INF for _ in range(n+1)] for _ in range(2*n - 1)]

    for socketIdx in range(2*n - 1):
        dp[socketIdx][1] = cost(T, socketIdx, socketIdx + 1)

    for wires in range(2, n+1):
        for socketIdx in range(2*(n - wires) + 1):
            dp[socketIdx][wires] = dp[socketIdx + 1][wires - 1] + cost(T, socketIdx, socketIdx + 2 * wires - 1)

            for k in range(1, wires):
                dp[socketIdx][wires] = min(dp[socketIdx][wires], dp[socketIdx][k] + dp[socketIdx + 2*k][wires - k])

    return dp[0][n]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )
