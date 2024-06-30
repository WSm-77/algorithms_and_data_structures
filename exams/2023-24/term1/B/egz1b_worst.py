# Wiktor Sędzimir
#
# Opis algorytmu:
# W tym algorytmie, dla każdego przedziału elementów od i-tego do j-tego wyznaczamy sumę elementów z tego przedziału
# oraz umieszczamy wszystkie elementy z tego przedziału w kopcu binarnym. Następny krok to wyciągnięcia maksymalnie k
# elementów z kopca binarnego i sprawdzanie czy są one mniejsze od zera. Jeżeli są, to możemy powiększyć naszą sumę
# o wartość bezwzględną z wyciągniętego elementu. Szukaną maksymalną sumą jest maksimum z sum elementów z przedziału
# powiększona o wartość bezwzględną z sumy elementów wyciągniętych z kopca.
# 
# Złożoność obliczeniowa:
# Ponieważ dla każdego przedziału umieszczamy wszystkie elementy w kopcu to musimy wykonać n (wyznaczenie początku 
# przedziału) * n (wyznaczenie końca przedziału) * n log n (umieszczenie maksymalnie n elementów w kopcu) operacji
# co daje nam złożoność O(n^3 log n). 

from egz1btesty import runtests
import heapq


def kstrong( T, k):
  # tu prosze wpisac wlasna implementacje
  n = len(T)

  prefixSums = [0]*n
  prefixSums[0] = T[0]
  for i in range(n):
    prefixSums[i] = prefixSums[i - 1] + T[i]
  
  INF = float("inf")
  maxSum = -INF

  for beg in range(n):
    for end in range(beg, n):
      heap = []
      for i in range(beg, end + 1):
        heapq.heappush(heap, T[i])

      sumInRange = prefixSums[end]
      if beg != 0:
        sumInRange -= prefixSums[beg - 1]

      for _ in range(k):
        if len(heap) == 0:
          break
        val = heapq.heappop(heap)

        if val >= 0:
          break
        sumInRange -= val
        maxSum = max(maxSum, sumInRange)

  return maxSum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
