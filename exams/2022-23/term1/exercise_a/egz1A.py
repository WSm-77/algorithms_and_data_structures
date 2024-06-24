# Opis algorytmu:
# Dla każdego wierzchołka wyznaczamy minimalny koszt dostania się do niego od wierzchołka "s" oraz minimalny koszt 
# dostania się do niego od wierzchołka "t", ale tym razem tak jakbyśmy okradli jakiś zamek. Dzięki temu całkowity
# minimalny koszt dostania się od wierzchołka "s" do "t" przy założeniu, że okradamy zamek "i" to minimalny koszt
# dostania się od wierzchołka "s" do zmaku "i" oraz minimalny koszt dostania się od wierzchołka "t" do wierzchołka
# "i" przy zwiększonym koszcie podróży minus wartość okradzionego złota. 

from egz1Atesty import runtests
from queue import PriorityQueue

INF = float("inf")

def dijkstra(graph, source, calcTravelCost):
  V = len(graph)

  costs = [INF for _ in range(V)]
  costs[source] = 0
  toCheck = PriorityQueue()
  toCheck.put((0, source))

  while not toCheck.empty():
    currCost, vertex = toCheck.get()
    for neighbour, travelCost in graph[vertex]:
      newCost = currCost + calcTravelCost(travelCost)
      if newCost < costs[neighbour]:
        costs[neighbour] = newCost
        toCheck.put((newCost, neighbour))
  
  return costs


def gold(G,V,s,t,r):
  # tu prosze wpisac wlasna implementacje

  # calculate normal travel cost from source to every vertex
  normalCost = dijkstra(G, s, lambda x: x)
  
  # calculate travel cost from end to every vertex after stealing gold
  stealCost = dijkstra(G, t, lambda x: 2*x + r)

  res = INF

  for i in range(len(V)):
    res = min(res, normalCost[i] + stealCost[i] - V[i])

  return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
