# Wiktor Sędzimir
# 
# Opis algorytmu:
# Algorytm opiera się na zasadzie działania algorytmu Dijkstry (ale wykorzystuje algorytm BFS), który wyznacza minimalne 
# czasy dotarcia do każdego miasta przy danej liczbie godzin przez którą wojownik będzie mógł jeszcze dalej wędorwać bez odpoczynku 
# startując od tego miasta. Szukanym minimalnym czasem dotarcia do wierzchołka końcowego jest minimalny czas dotarcia do tego
# miasta przy dowolnym zmęczeniu wojownika. W tym algorytmie, dla każdego wierzchołka musimy sprawdzać zarówno możliwość 
# kontunuowania podróży bez odpoczynku, jak i możliwość, w której wojownik odpoczywa w danym mieście a następnie kontynuuje 
# podróż. Aby osiągnąć lepszą złożoność czasową niż w przypadku algorytmu Dijkstry korzystamy z modyfikacji algorytmu BFS,
# w której do kolejki dodajemy dodtakowy licznik, który zlicza nam ile jeszcze godzin wojownik musi iść, aby dotrzeć do 
# kolejnego miasta. Jeżeli licznik ten spadnie do zera, to dopiero wtedy rozpatrujemy dane miasto tak, jakby wojownik
# się w nim znajdował i planował dalszą podróż. W przeciwnym wypadku oznacza to, że nasz wojownik jest dalej w drodze 
# (nie znajduje się w żadnym mieście), więc musimy zmniejszyć licznik czasu potrzebnego do dotarcia do kolejnego miasta
# o 1 i spowrotem wrzucić dane miasto wraz z pozostałymi parametrami do kolejki. Ponieważ dany wierzchołek przy danych parametrach
# możemy rozpatrywać maksymalnie 17 razy to finalnie złożoność algorytmu BFS zwiększa się jedynie o stałą.
# 
# Złożoność obliczeniowa:
# Ponieważ algorytm opiera się na zasadzie działania algorytmu BFS to jego złożoność obliczeniowa jest równa O(E + V).
# Z powodu faktu że dla danego wierzchołka możemy mieć 17 różnych stanów (wojownik będzie mógł kontynuować podróż
# przez kolejne 0 - 16 godzin) to stała będzie większa niż w przypadku zwykłego zastosowania algorymu BFS, jednakże 
# w notacji wielkiego O ta stała nie ma dla nas znaczenia.
#
# Złożoność pamięciowa:
# Ponieważ tworzymy nowy graf w postaci listy sąsiedztwa to potrzebujemy wykorzystać E + V pamięci. Następnie do 
# zapamiętywania najkrótszych czasów potrzebujemy dodatkowe O(17*V) ~ O(V) pamięci. W kolejce priorytetowej możemy
# trzymać maksymalnie O(17*(V+E)) ~ O(V + E) elementów, więc ostateczna złożoność pamięciowa wynosi O(E+V)

from kol2testy import runtests
from collections import deque

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

  # 0 - czas dotarcia do wierzchołka, 1 - wierzchołek, 2 - tyle możemy wędrować dalej bez przerwy, 3 - ile razy
  # trzeba będzie wyjąć ten wierzchołek z kolejki
  toCheck = deque()
  toCheck.append((0, s, 16, 0))

  while toCheck:
    currentTime, vertex, noRestTime, cnt = toCheck.popleft()

    if cnt == 0:
      if times[vertex][noRestTime] < currentTime:
        continue

      for neighbour, cost in G[vertex]:
        # nie odpoczywa
        newNoRestTime = noRestTime - cost
        newTime = currentTime + cost
        if 0 <= newNoRestTime and newTime < times[neighbour][newNoRestTime]:
          times[neighbour][newNoRestTime] = newTime
          toCheck.append((newTime, neighbour, newNoRestTime, cost - 1))

        # odpoczywa
        newTime = currentTime + cost + 8
        newNoRestTime = 16 - cost
        if newTime < times[neighbour][newNoRestTime]:
          times[neighbour][newNoRestTime] = newTime
          toCheck.append((newTime, neighbour, newNoRestTime, cost - 1))
    else:
      toCheck.append((currentTime, vertex, noRestTime, cnt - 1))

  minTime = times[t][0]
  for i in range(1, 17):
    if times[t][i] < minTime:
      minTime = times[t][i]

  return minTime

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
