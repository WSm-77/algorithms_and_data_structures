from kolutesty import runtests
from collections import deque

def create_graph(V: int, edges: list[tuple]):
  reversedGraph = [[] for _ in range(V)]

  for neighbour, vertex in edges:
    reversedGraph[neighbour].append(vertex)

  return reversedGraph

def projects(n, L):
  # tu prosze wpisac wlasna implementacje

  def get_max_path(vertex):
    nonlocal distances, reversedGraph, visited
    if not visited[vertex]:
      for neighbour in reversedGraph[vertex]:
        distances[vertex] = max(distances[vertex], get_max_path(neighbour) + 1)

      visited[vertex] = True

    return distances[vertex]
  #end def

  V = n
  reversedGraph = create_graph(n, L)

  visited = [False]*V
  distances = [1 for _ in range(V)]

  res = 0
  for vertex in range(V):
    res = max(res, get_max_path(vertex))

  return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
