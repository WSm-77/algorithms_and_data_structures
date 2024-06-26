# Opis algorytmu:
# Rozwiązaniem zadania jest znalezienie najdłuższej ścieżki w DAGu. Robimy to najpierw sortując topologicznie
# wierzchołki w grafie. W ten sposób otrzymamy kolejność przechodzenia po wierzchołkach w grafie. Następnie
# korzystając z algorytmu Bellmana-Forda relaksujemy krawędzie, pamiętając że szukamy najdłuższej ścieżki.
# Złożoność obliczeniowa:
# O(n + m), gdzie n - liczba projektów, m - liczba zależności

from kolutesty import runtests

def create_graph(V: int, edges: list[tuple]):
  graph = [[] for _ in range(V)]

  for neighbour, vertex in edges:
    graph[vertex].append(neighbour)

  return graph

def topo_sort(graph):
  def dfs_visit(vertex):
    nonlocal graph, visited, topoSorted

    visited[vertex] = True

    for neighbour in graph[vertex]:
      if not visited[neighbour]:
        dfs_visit(neighbour)

    topoSorted.append(vertex)
  #end def

  V = len(graph)
  visited = [False]*V
  topoSorted = []

  for vertex in range(V):
    if not visited[vertex]:
      dfs_visit(vertex)
  
  topoSorted.reverse()
  return topoSorted

def projects(n, L):
  # tu prosze wpisac wlasna implementacje

  V = n

  # we create graph where edge vertex -> neighbour means that task vertex must be completed before neighbour task
  graph = create_graph(n, L)

  # we use topological sort to determine order of completing tasks
  topoSort = topo_sort(graph)

  distances = [1 for _ in range(V)]

  # we use Bellman-Ford relaxation approach to get longest path in DAG 
  for vertex in topoSort:
    for neighbour in graph[vertex]:
      if distances[neighbour] < distances[vertex] + 1:
        distances[neighbour] = distances[vertex] + 1

  # we return longest distance between any pair of connected verticies in graph
  return max(distances)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
