# Wiktor Sędzimir
#
# Opis algorytmu:
# Korzystamy dwukrotnie z algorytmu Dijkstry - najpierw do wyznaczenia najkrótszych tras od początku do wszystkich wierzchołków
# a następnie od końca do wszystkich wierzchołków. Minimalny czas to czas biegu do dowolnego wierzchołka a następnie czas jazdy
# od danego wierzchołka do końca. Czas jazdy jest równy czasowi biegu przemnożonemu przez odpowiednią wartość dla danego roweru.
# Możliwe jest również, że najszybszy będzie sam bieg, więc to również bierzemy pod uwagę.
#
# Złożoność obliczeniowa:
# O(E log V) - dwa razy korzystamy z algorytmu dijkstry a następnie liniowo wyznaczamy koszt podróży dla każdego wierzchołka

from egz1atesty import runtests
from queue import PriorityQueue

def get_number_of_verticies(edges):
  V = 0
  for vertex, neighbour, _ in edges:
    V = max(V, vertex, neighbour)
  return V + 1

def edges_to_grap(edges):
  V = get_number_of_verticies(edges)
  graph = [[] for _ in range(V)]

  for vertex, neighbour, cost in edges:
    graph[vertex].append((neighbour, cost))
    graph[neighbour].append((vertex, cost))

  return graph

def dijkstra(graph, source):
  V = len(graph)

  INF = float("inf")
  distance = [INF for _ in range(V)]
  distance[source] = 0
  toCheck = PriorityQueue()
  toCheck.put((0, source))

  while not toCheck.empty():
    currDist, vertex = toCheck.get()

    for neighbour, cost in graph[vertex]:
      newDist = currDist + cost
      if newDist < distance[neighbour]:
        distance[neighbour] = newDist
        toCheck.put((newDist, neighbour))

  return distance

def armstrong( B, G, s, t):
  # tu prosze wpisac wlasna implementacje

  INF = float("inf")
  graph = edges_to_grap(G)

  V = len(graph)

  bikesCorrection = [INF for _ in range(V)]
  for vertex, p, q in B:
    # ponieważ może być kilka rowerów w jednym wierzchołku to zawsze musimy wybrać ten najszybszy
    # czyli o najmniejszym stosunku p/q
    bikesCorrection[vertex] = min(p/q, bikesCorrection[vertex])

  distancesFromSource = dijkstra(graph, s)
  distancesFromTarget = dijkstra(graph, t)

  minDist = distancesFromSource[t]
  for vertex in range(V):
    if bikesCorrection[vertex] != INF:
      withBike = distancesFromTarget[vertex] * bikesCorrection[vertex]
      if withBike != INF:
        minDist = min(minDist, distancesFromSource[vertex] + int(withBike))

  return minDist

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
