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

def fix_matrix(matrix):
  n = len(matrix)
  for i in range(n):
    for j in range(n):
      matrix[i][j] = abs(matrix[i][j])

def does_intersect(interval1beg, interval1end, interval2beg, interval2end):
  return interval1beg <= interval2beg <= interval1end \
      or interval1beg <= interval2end <= interval1end \
      or interval2beg <= interval1beg <= interval2end \
      or interval2beg <= interval1end<= interval2end 

def Flight(L,x,y,t):
  # tu prosze wpisac wlasna implementacje

  def dfs_visit(vertex, minCeiling, maxCeiling):
    nonlocal G, V, y, t, way
    if vertex == y:
      nonlocal minCeilingMain, maxCeilingMain
      minCeilingMain = minCeiling
      maxCeilingMain = maxCeiling
      return True
    
    for neighbour in range(V):
      currentCeiling = G[vertex][neighbour]
      if 0 <= currentCeiling:
        if does_intersect( minCeiling, maxCeiling, currentCeiling - t, currentCeiling + t):
          way.append((neighbour, G[vertex][neighbour]))
          newMinCeiling = max(minCeiling, currentCeiling - t)
          newMaxCeiling = min(maxCeiling, currentCeiling + t)
          
          G[vertex][neighbour] = G[neighbour][vertex] = -currentCeiling


          if dfs_visit(neighbour, newMinCeiling, newMaxCeiling):
            return True
          
          way.pop()
    #end if

    return False
  #end def

  V = get_number_of_verticies(L)
  G = graph_to_matrix(L, V)
  way = [x]

  for neighbour in range(V):
    if G[x][neighbour] > 0:
      minCeilingMain = G[x][neighbour] - t
      maxCeilingMain = G[x][neighbour] + t
      way.append((neighbour, G[x][neighbour]))
      if dfs_visit(neighbour, minCeilingMain, maxCeilingMain):
        print(f"ceiling: {minCeilingMain} ~ {maxCeilingMain}")
        print(*way, sep=" -> ")

        return True
      #end if
      way.pop()
  return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
