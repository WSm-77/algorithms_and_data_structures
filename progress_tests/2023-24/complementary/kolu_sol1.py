# Opis algorytmu:
# Rozwiązaniem zadania jest znalezienie najdłuższej ścieżki w DAGu, w którym zależności pomiędzy projektami są krawędziami.
# Definiujemy funkcję distance(vertex) - najdłuższa ścieżka w DAGu, kończąca się w wierzchołku "vertex". Aby wyznaczyć
# wartość tej funkcji musimy znaleźć najdłuższą ścieżkę prowadzącą, do każdego z wierzchołków, z których możemy dostać
# się do wierzchołka "vertex" a następnie przedłużyć ją o jedną krawędź.
# Złożoność obliczeniowa:
# O(n + m), gdzie n - liczba projektów, m - liczba zależności

from kolutesty import runtests

def create_reversed_graph(V: int, edges: list[tuple]):
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
  reversedGraph = create_reversed_graph(n, L)

  visited = [False]*V
  distances = [1 for _ in range(V)]

  res = 0
  for vertex in range(V):
    res = max(res, get_max_path(vertex))

  return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
