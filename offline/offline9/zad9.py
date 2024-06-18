from zad9testy import runtests

def topo_sort(graph, rows, colls):
  def dfs_visit(R, C):
    nonlocal graph, visited, priority, idx

    vertex = R*colls + C
    visited[vertex] = True

    for nextR, nextC in graph[vertex]:
      if not visited[nextR*colls + nextC]:
        dfs_visit(nextR, nextC)
    
    priority[idx] = (R, C)
    idx -= 1
  #end def

  V = len(graph)

  visited = [False for _ in range(V)]
  priority = [None for _ in range(V)]
  idx = V - 1

  for R in range(rows):
    for C in range(colls):
      if not visited[R*colls + C]:
        dfs_visit(R, C)
  
  return priority

def create_graph(M, directions):
  rows = len(M)
  colls = len(M[0])

  graph = [[] for _ in range(rows*colls)]

  for R in range(rows):
    for C in range(colls):
      for x, y in directions:
        nextR, nextC = R + y, C + x
        if 0 <= nextR < rows and 0 <= nextC < colls and M[R][C] < M[nextR][nextC]:
          vertex = R*colls + C
          graph[vertex].append((nextR, nextC))

  return graph

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

  graph = create_graph(M, directions)

  priority: list[tuple[int, int]] = topo_sort(graph, rows, colls)

  longestTrip = [[None for _ in range(colls)] for _ in range(rows)]
  bestTrip = 1

  for R, C in priority:
    if longestTrip[R][C] == None:
      bestTrip = max(bestTrip, longest_trip_rek(R, C))


  return bestTrip

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )

