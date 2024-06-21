# Wiktor Sędzimir
# 
# opis algorytmu:
# Dla każdego elementu wyznaczamy jego "rangę" sprawdzając każdy element występujący przed nim w tablicy i jeżeli jego wartość jest
# mniejsza to zwiększamy rangę naszego elementu. Po wyznaczeniu rangi danego elementu aktualizujemy wartość maksymalnej rangi.
# Algorytm działa w czasie O(n^2).

from kol1testy import runtests

def maxrank(T):
  # tu prosze wpisac wlasna implementacje
  n = len(T)

  result = 0

  for i in range(1, n):
    currRank = 0
    for j in range(0, i):
      if T[j] < T[i]:
        currRank += 1

    #end for
    if currRank > result:
      result = currRank

  return result 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True)
