# Wiktor Sędzimir
#
# Opis algorytmu:
# Definiujemy funkcję f(i, s) jako maksymalna liczba drzew ze zbioru od zerowego do i-tego drzewa (włącznie),
# dla których sumaryczna liczba jabłek na tych drzewach jest liczbą podzielną przez s. Tworzymy dodatkow funkcję
# pomocniczą isSumPossible(i,s), która informuje nas czy możliwe jest wybranie ze zbioru "i" pierwszych drzew, 
# takich drzew, dla których liczba jabłek na tych drzewach sumuje się do liczby podzielnej przez s. Dla tak zdefiniowanych 
# funkcji możemy w łatwy sposób wyznaczyć ich wzór jako: 
# 1) f(i,s) = max(f(i-1, s), f[i-1][ (s-T[i]) % m] + 1) (drugi argument funkcji max bierzemy tylko jeżeli możliwe jest 
# otrzymanie sumy (jabłek) podzielnej przez wartość (s-T[i]) % m ze zbioru i-1 pierwszych drzew).
# 2) isSumPossible(i,s) = isSumPossible(i-1, s) or isSumPossible(i-1, (s-T[i]) % m)
# Wzory te oznaczają, że albo pomijamy i-te drzewo, albo berzemy to drzewo i rozważamy i-1 pierwszych drzew, dla których
# suma jabłek jest pomniejszona odpowiednio o liczbę jabłek na obecnie rozważanym drzewie.
# Ostatecznym rozwiązaniem zadania jest ogólna liczba drzew pomniejszona o maksymalną liczbę drzew których sumaryczna 
# liczba jabłek jest podzialna przez m (wartość tę znajdziemy w tablicy f[n - 1][0]).
# 
# Złożoność obliczeniowa:
# W naszym algorytmie musimy obliczyć wartość dla n*m elementów 2 talic a wyliczenie tych wartości odbywa się w czasie 
# stałym, więc finalna złożoność wynosi O(n*m) ~ O(n*7*n) ~ O(n^2).
# Złożoność pamięciowa:
# Ponieważ, tworzymy 2 tablice o rozmiarach n*m to złożoność pamięciowa wynosi O(n^2).



from kol3testy import runtests


def orchard(T, m):
    # tu prosze wpisac wlasna implementacje

    n  = len(T)

    f = [[0 for _ in range(m)] for _ in range(n)]
    isSumPossible = [[False for _ in range(m)] for _ in range(n)]

    f[0][T[0]%m] = 1
    isSumPossible[0][0] = True
    isSumPossible[0][T[0]%m] = True

    for currTreeIdx in range(1, n):
        for appleSum in range(m):
            prevTreeIdx = currTreeIdx - 1
            f[currTreeIdx][appleSum] = f[prevTreeIdx][appleSum]
            isSumPossible[currTreeIdx][appleSum] = isSumPossible[prevTreeIdx][appleSum]
            prevAppleSum = (appleSum - T[currTreeIdx]) % m
            if isSumPossible[prevTreeIdx][prevAppleSum]:
                isSumPossible[currTreeIdx][appleSum] = True
                f[currTreeIdx][appleSum] = max(f[currTreeIdx][appleSum], f[prevTreeIdx][prevAppleSum] + 1)


    return n - f[n - 1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)

