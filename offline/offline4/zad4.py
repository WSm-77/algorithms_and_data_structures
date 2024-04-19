from zad4testy import runtests

def get_number_of_verticies(edgesTab):
  V = 0
  for edge in edgesTab:
    V = max(V, edge[1])
  #end for
  return V + 1

def graph_to_matrix(edgesTab, V):
  matrix = [[-1 for _ in range(V)] for _ in range(V)]
  
  for v, u, ceiling in edgesTab:
    matrix[v][u] = matrix[u][v] = ceiling
  #end for

  return matrix
  

def Flight(L,x,y,t):
  # tu prosze wpisac wlasna implementacje

  def dfs_visit(vertex, minCeiling, maxCeiling):
    nonlocal G, V, y, t
    if vertex == y:
      return True
    
    for neighbour in range(V):
      currentCeiling = G[vertex][neighbour]
      if 0 <= currentCeiling:
        newMinCeiling = max(minCeiling, currentCeiling - t)
        newMaxCeiling = min(maxCeiling, currentCeiling + t)
        if newMinCeiling <= newMaxCeiling:
          G[vertex][neighbour] = G[neighbour][vertex] = -currentCeiling
          if dfs_visit(neighbour, newMinCeiling, newMaxCeiling):
            return True
    #end if

    return False
  #end def

  V = get_number_of_verticies(L)
  G = graph_to_matrix(L, V)

  for neighbour in range(V):
    if G[x][neighbour] > 0:
      minCeiling = 0
      maxCeiling = float("inf")
      if dfs_visit(neighbour, minCeiling, maxCeiling):
        return True

  return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
