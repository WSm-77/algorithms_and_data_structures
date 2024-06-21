# Wiktor Sędzimir
# 
# Opis algorytmu:
# Algorytm opiera się na zasadzie działania algorytmu Dijkstry, który wyznacza minimalne czasy dotarcia do każdego miasta
# przy danej liczbie godzin przez którą będzimy mogli jeszcze dalej wędorwać bez odpoczynku startując od tego miasta.
# Szukanym minimalnym czasem dotarcia do wierzchołka końcowego jest minimalny czas dotarcia do tego miasta przy dowolnym
# zmęczeniu wojownika. W tym algorytmie, dla każdego wierzchołka musimy sprawdzać zarówno możliwość kontunuowania podróży
# bez odpoczynku, jak i możliwość, w której wojownik odpoczywa w danym mieście a następnie kontynuuje podróż.
# 
# Złożoność obliczeniowa:
# Ponieważ algorytm opiera się na zasadzie działania algorytmu Dijkstry to jego złożoność obliczeniowa jest równa O(E log V).
# Z powodu faktu że dla danego wierzchołka możemy mieć 17 różnych stanów (wojownik będzie mógł kontynuować podróż
# przez kolejne 0 - 16 godzin) to stała będzie większa niż w przypadku zwykłego zastosowania algorymu Dijkstry, jednakże 
# w notacji wielkiego O ta stała nie ma dla nas znaczenia.
#
# Złożoność pamięciowa:
# Ponieważ tworzymy nowy graf w postaci listy sąsiedztwa to potrzebujemy wykorzystać E + V pamięci. Następnie do 
# zapamiętywania najkrótszych czasów potrzebujemy dodatkowe O(17*V) ~ O(V) pamięci. W kolejce priorytetowej możemy
# trzymać maksymalnie O(17*(V+E)) ~ O(V + E) elementów, więc ostateczna złożoność pamięciowa wynosi O(E+V)

from kol2testy import runtests
from queue import PriorityQueue

def get_number_of_verticies(edges):
  V = 0
  for vertex, neighbour, _ in edges:
    V = max(V, vertex, neighbour)

  return V + 1

def create_graph(edges, V):
  graph = [[] for _ in range(V)]

  for vertex, neighbour, cost in edges:
    graph[vertex].append((neighbour, cost))
    graph[neighbour].append((vertex, cost))
  
  return graph

def warrior( G, s, t):
  # tu prosze wpisac wlasna implementacje
  INF = float("inf")
  V = get_number_of_verticies(G)
  G = create_graph(G, V)
  
  # times[i][h] - czas dotarcia do wierzchołka "i" mogąc wędrować dalej przez "h" godzin bez odpoczynku
  times = [[INF for _ in range(17)] for _ in range(V)]
  for i in range(16):
    times[s][i] = 0

  # 0 - czas dotarcia do wierzchołka, 1 - wierzchołek, 2 - tyle możemy wędrować dalej bez przerwy
  toCheck = PriorityQueue()
  toCheck.put((0, s, 16))

  while not toCheck.empty():
    currentTime, vertex, noRestTime = toCheck.get()

    
    if times[vertex][noRestTime] < currentTime:
      continue
    
    if vertex == t:
      return currentTime

    for neighbour, cost in G[vertex]:
      # nie odpoczywa
      newNoRestTime = noRestTime - cost
      newTime = currentTime + cost
      if 0 <= newNoRestTime and newTime < times[neighbour][newNoRestTime]:
        times[neighbour][newNoRestTime] = newTime
        toCheck.put((newTime, neighbour, newNoRestTime))

      # odpoczywa
      newTime = currentTime + cost + 8
      newNoRestTime = 16 - cost
      if newTime < times[neighbour][newNoRestTime]:
        times[neighbour][newNoRestTime] = newTime
        toCheck.put((newTime, neighbour, newNoRestTime))

  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
