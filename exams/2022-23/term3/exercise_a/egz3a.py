# Bardzo podobny algorytm został opisany w progress_tests/2023-24/test2/kol2_worse.py

from egz3atesty import runtests
from queue import PriorityQueue

def matrix_to_graph(matrix):
  V = len(matrix)
  graph = [[] for _ in range(V)]

  for vertex in range(V):
    for neighbour in range(vertex + 1, V):
      distance = matrix[vertex][neighbour]
      if distance != -1:
        graph[vertex].append((neighbour, distance))
        graph[neighbour].append((vertex, distance))

  return graph

def goodknight( G, s, t ):
  # tu prosze wpisac wlasna implementacje

  INF = float("inf")
  G = matrix_to_graph(G)
  V = len(G)

  # distances[vertex][inTravel]
  distances = [[INF for _ in range(17)] for _ in range(V)]
  distances[s][0] = 0

  # toCheck: 0 - currentDistance, 1 - how many hours knight has been traveling without rest, 2 - vertex
  toCheck = PriorityQueue()
  toCheck.put((0, 0, s))

  while not toCheck.empty():
    currDist, timeWithoutRest, vertex = toCheck.get()

    if vertex == t:
      return currDist

    # continue travle without rest
    for neighbour, cost in G[vertex]:
      newTimeWithoutRest = timeWithoutRest + cost
      
      # knight can't travel for more than 16 hours without rest
      if newTimeWithoutRest <= 16:
        travelTime = currDist + cost
        if travelTime < distances[neighbour][newTimeWithoutRest]:
          distances[neighbour][newTimeWithoutRest] = travelTime
          toCheck.put((travelTime, newTimeWithoutRest, neighbour))

    # rest in current vertex
    newTimeWithoutRest = 0
    travelTime = currDist + 8
    if travelTime < distances[vertex][newTimeWithoutRest]:
      distances[vertex][newTimeWithoutRest] = travelTime
      toCheck.put((travelTime, newTimeWithoutRest, vertex))

  return min(distances[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
