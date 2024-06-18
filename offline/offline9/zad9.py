# Wiktor Sędzimir
#
# Opis algorytmu:
# Określamy funkcję longestTrip(r, c) - najdłuższa wycieczka kończąca się w punkcie (r, c). Wartość tej funkcji
# wyznaczamy znajdując maksimum z najdłuższych wycieczek kończących się w punktach, z których możemy w jednym kroku
# dostać się na pole (r, c).
# Złożoność:
# Złożoność obliczeniowa wynosi O(rows*colls), ponieważ dla każdego pola musimy wyznaczyć wartość funkcji
# longestTrip(r, c) a wyznaczenie tej wartości jest realizowane w czasie stałym, gdyż sprawdzamy wartości funkcji
# longestTrip(nr, nc) dla maksymalnie 4 sąsiadów. Złożoność pamięciowa również wynosi O(rows*colls).


from zad9testy import runtests

def trip(M):
  # tu prosze wpisac wlasna implementacje
  def longest_trip_rek(R, C):
    if longestTrip[R][C] != None:
      return longestTrip[R][C]

    tripLen = 1

    for x, y in directions:
      nextR, nextC = R + y, C + x
      if 0 <= nextR < rows and 0 <= nextC < colls and M[nextR][nextC] < M[R][C]:
        tripLen = max(tripLen, longest_trip_rek(nextR, nextC) + 1)

    longestTrip[R][C] = tripLen

    return longestTrip[R][C]

  rows = len(M)
  colls = len(M[0])

  directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

  longestTrip = [[None for _ in range(colls)] for _ in range(rows)]
  bestTrip = 1

  for R in range(rows):
    for C in range(colls):
      if longestTrip[R][C] == None:
        bestTrip = max(bestTrip, longest_trip_rek(R, C))

  return bestTrip

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )

