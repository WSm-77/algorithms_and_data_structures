# Wiktor Sędzimir
# 
# Opis algorytmu:
# Najpierw zamieniamy tablicę krawędzi na graf reprezentowany w postaci tablicy sąsiedztwa. Następnie dla każdej krawędzi
# wychodzącej z wierzchołka startowego uruchamiamy dfs, który dodatkowo pilnuje, żeby samolot leciał na stałej wysokości.
# Wybranie pierwszej krawędzi dla naszego samolotu determinuje nam zakres, w której ostateczna wysokość przelotu musi się 
# zmieścić. Przy przechodzeniu przez kolejne krawędzie grafu zakres wysokości nam się zawęża w zależności od dopuszczalnej
# wysokości przelotu. Jeżeli dla pewnej krawędzi wychodzącej z wierzchołka startowego znajdziemy trasę pomiędzy x a y to 
# kończymy wykonywanie algorytmu.

from zad4testy import runtests

def get_number_of_verticies(edgesTab):
  V = 0
  for edge in edgesTab:
    V = max(V, edge[1])
  #end for
  return V + 1

def edges_to_graph(edgesTab, V):
  graph = [[] for _ in range(V)]
  
  for v, u, ceiling in edgesTab:
    graph[v].append((u, ceiling))
    graph[u].append((v, ceiling))
  #end for

  return graph

def does_intersect(interval1beg, interval1end, interval2beg, interval2end):
  return interval1beg <= interval2beg <= interval1end \
      or interval1beg <= interval2end <= interval1end \
      or interval2beg <= interval1beg <= interval2end \
      or interval2beg <= interval1end<= interval2end 

def Flight(L,x,y,t):
  # tu prosze wpisac wlasna implementacje

  def dfs_visit(vertex, minCeiling, maxCeiling):
    nonlocal G, V, y, t, way, visited
    if vertex == y:
      return True
    
    visited[vertex] = True
    
    for neighbour, currentCeiling in G[vertex]:
      if not visited[neighbour]:
        if does_intersect( minCeiling, maxCeiling, currentCeiling - t, currentCeiling + t):
          newMinCeiling = max(minCeiling, currentCeiling - t)
          newMaxCeiling = min(maxCeiling, currentCeiling + t)

          if dfs_visit(neighbour, newMinCeiling, newMaxCeiling):
            return True
    #end if

    return False
  #end def

  V = get_number_of_verticies(L)
  G = edges_to_graph(L, V)

  way = [x]

  for neighbour, ceiling in G[x]:
    visited = [False]*V
    visited[x] = True

    minCeilingMain = ceiling - t
    maxCeilingMain = ceiling + t

    way.append((neighbour, ceiling))
    if dfs_visit(neighbour, minCeilingMain, maxCeilingMain):
      return True
    #end if
  return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
