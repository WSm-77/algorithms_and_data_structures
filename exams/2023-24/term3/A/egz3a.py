# Opis algorytmu:
# Dla każdego drzewa zapisujemy czas zakażenia oraz numer grzyba. Następnie korzystamy ze zmodyfikowanej wersji
# algorytmu BFS, w którym symulujemy rozprzestrzenianie się choroby. Najpierw umieszczamy wszystkie zakażone drzewa
# w kolejce i zapisujemy czas ich zarażenia na 0. Następnie tak jak w algorytmie BFS wyjmujemy kolejne drzewa z kolejki
# i sprawdzamy sąsiadów i jeżeli nie są jeszcze zarażeni, to zarażamy ich tym samym grzybem, a w przeciwnym przypadku
# sprawdzamy czy zostali zarażeni w obecnej jednostce czasu (czas zarażenia obecnego drzewa + 1) oraz zmieniamy rodzaj
# grzyba, którym zostali zarażeni (jeżeli ma on mniejszy numer porządkowy).
#
# Złożoność:
# O(V + E) - złożoność zwykłego BFS'a

from egz3atesty import runtests
from collections import deque

def mykoryza( G,T,d ):
  # tu prosze wpisac wlasna implementacje

  V = len(G)
  INF = float("inf")
  NOT_INFECTED = -1
  infectionTime = [INF for _ in range(V)]
  infected = [NOT_INFECTED for _ in range(V)]

  diseaseSpread = deque()

  for diseaseId, treeId in enumerate(T):
    diseaseSpread.append(treeId)
    infectionTime[treeId] = 0
    infected[treeId] = diseaseId

  while diseaseSpread:
    treeId = diseaseSpread.popleft()
    for neighbour in G[treeId]:
      if infected[neighbour] == NOT_INFECTED:
        infected[neighbour] = infected[treeId]
        infectionTime[neighbour] = infectionTime[treeId] + 1
        diseaseSpread.append(neighbour)
      # different diseases reached current tree at the same time
      elif infectionTime[neighbour] == infectionTime[treeId] + 1 and infected[treeId] < infected[neighbour]:
        infected[neighbour] = infected[treeId]

  result = 0

  for disease in infected:
    if disease == d:
      result += 1

  return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
