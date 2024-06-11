# Wiktor Sędzimir
#
# Opis algorytmu:
# Tworzymy funkcję f(i, j) - minimalan wartość sumy doległości parkingów od biurowców przy założeniu, że i-ty
# biurowiec otrzymuje (i+j)-ty parking. Jeżeli mamy tak zdefiniowaną funkcję to jak łatwo zauważyć wartość tej
# funkcji dla dowolnego "i" oraz "j" można określić następującym wzorem:
#
# f(i, j) = min(f(i - 1, k)) + | X[i] + Y[i+j] |, po "k" należącym do zbioru: <0,j> (ponieważ biurowiec o indeksie
# i-1 mógł otrzymać działki: Y[i-1], Y[i], ... , Y[i+j-1] = Y[i-1+j])
#
# Zauważmy, że i-ty biurowiec nie mógł otrzymać wcześniejszej działki niż i-tą, ponieważ ozaczałoby to, że któryś
# z poprzednich biurowców nie otrzymał działki, co jest sprzeczne z założeniami zadania.
#
# W naszym algorytmie skorzystamy z tablicy pomocniczej prevMin, w której będziemy zapisywać wartości minimalne sumy
# odległości pomiędzy biurowcami a parkingami. Wartość tablicy prevMin[i][j] będzie oznaczać wartość najmniejszą sumy
# tych odległości dla zboioru biurowców od zerowego do i-tego oraz działek od zerowej do i+j-tej. Wartości z tej
# tablicy posłużą nam do szybkiego odczytania wartości "min(f(i - 1, k))" z naszgo wzoru, ponieważ będzie to po prostu
# prevMin[i-1][j].
#
# Złożoność:
# Złożoność tego algorytmu wynosi O(n*(n-m)), ponieważ tyle jest możliwych wartości funkcji f i prevMin oraz
# wyznaczenie ich wartości odbywa się w stałym czasie.

from zad8testy import runtests

def parking(X,Y):
  # tu prosze wpisac wlasna implementacje
  n = len(X)
  m = len(Y)
  difference = m - n + 1

  f = [[None for _ in range(difference)] for _ in range(n)]
  prevMin = [[None for _ in range(difference)] for _ in range(n)]

  currSum = 0
  for i in range(n):
    currSum += abs(X[i] - Y[i])
    f[i][0] = currSum
    prevMin[i][0] = f[i][0]

  for j in range(1, difference):
    f[0][j] = abs(X[0] - Y[j])
    prevMin[0][j] = min(prevMin[0][j - 1], f[0][j])

  for i in range(1, n):
    for j in range(1, difference):
      distance = abs(X[i] - Y[i+j])
      f[i][j] = prevMin[i-1][j] + distance
      prevMin[i][j] = min(prevMin[i][j - 1], f[i][j])

  return prevMin[n - 1][difference - 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
