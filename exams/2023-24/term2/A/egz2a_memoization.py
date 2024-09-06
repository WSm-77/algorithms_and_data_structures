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

    dp = {}

    def backtrack(socketIdx, wiresCnt):
        key = (socketIdx, wiresCnt)
        if key not in dp:
            if wiresCnt == 1:
                dp[key] = cost(T, socketIdx, socketIdx + 1)
            else:
                minVal = backtrack(socketIdx + 1, wiresCnt - 1) + cost(T, socketIdx, socketIdx + 2 * wiresCnt - 1)

                for wires in range(1, wiresCnt):
                    minVal = min(minVal, backtrack(socketIdx, wires) + backtrack(socketIdx + 2*wires, wiresCnt - wires))

                dp[key] = minVal

        return dp[key]

    return backtrack(0, n)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )

