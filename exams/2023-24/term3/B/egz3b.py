# Opis algorytmu:
# Typowe rozwiązanie dynamiczne.
#
# Złożoność:
# O(n) - przechodzimy stałą liczbę razy liniowo po tablicy

from egz3btesty import runtests


def kunlucky(T, k):
  # tu prosze wpisac wlasna implementacje

  n = len(T)

  isKUnfortunate = [False for _ in range(n + 1)]

  unfortunate = k
  i = 1
  while unfortunate <= n:
    isKUnfortunate[unfortunate] = True
    unfortunate += (unfortunate % i) + 7
    i += 1

  # dp[m][i] ~ max length of sequence containing up to "m" k-unfortunate numbers that ends at i-th number
  dp = [[0 for _ in range(n)] for _ in range(3)]
  dp[0][0] = int(isKUnfortunate[T[0]])

  for i in range(1, n):
    if isKUnfortunate[T[i]]:
      dp[0][i] = 0
    else:
      dp[0][i] = dp[0][i - 1] + 1

  for m in range(1, 3):
    for i in range(n):
      if isKUnfortunate[T[i]]:
        dp[m][i] = dp[m - 1][i - 1] + 1
      else:
        dp[m][i] = dp[m][i - 1] + 1

  return max(dp[2])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True)
