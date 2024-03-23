# Wiktor Sędzimir
#
# Opis algorytmu:
# Dla każdego punktu rozważamy zbiór 'X' punktów, które mają mniejszą wartość współrzędnej x (dane te są przechowywane w tablicy xStrength) oraz zbiór 'Y' 
# punktów, które mają mniejszą wartość współrzędnej y (dane te przechowujemy w tablicy yStrength). W zbiorze P mamy doczynienia z relacją porządkującą.
# Oznacza to, że szukany punkt jest elementem maksymalnym ze zbioru P w relacji porządku, zatem nie istnieje punkt, który dominowałby nasz szukany punkt.
# Ponieważ w relacji porządku może być wiele elementów maksymalnych, to bez straty ogólności możemy wprowadzić dodatkowe ograniczenie, że dla szukanego punktu
# Q=(x, y) nie istnieje punkt Q'=(x', y') należący do zbioru 'Z' punktów, które mają większą lub równą wartość współrzędnej x oraz większą lub równą wartość 
# współrzędnej y (x' >= x i y' >= y). Szukamy więc liczności zbioru |X * Y| (zbiór punków, które jednocześnie mają mniejszą wartość x oraz mniejszą 
# wartość y od punktu Q). Z działań na zbiorach wiemy, że: 
# |X + Y| = |X| + |Y| - |X * Y|, 
# zatem:
# |X * Y| = |X| + |Y| - |X + Y|. 
# Dla każdego punktu ze zbioru P mamy zależność: 
#         |P|          =        |X + Y| + 1 + |Z|
#          |                              |     
# liczba wszystkich punktów        badany punkt
# 
# więc:
# |X + Y| = |P| - |Z| - 1
#
# Jak wspomniano już wcześniej dla szukanego punktu Q: |Z| = 0, więc:
# |X * Y| = |X| + |Y| - (|P| - |Z| - 1) = |X| + |Y| - |P| + 0 + 1 = |X| + |Y| - |P| + 1

from zad3testy import runtests

def my_max(val1, val2):
  return val1 if val1 > val2 else val2

def dominance(P):
  # tu prosze wpisac wlasna implementacje
  n = len(P)

  xStrength = [0]*(n+1)
  yStrength = [0]*(n+1)

  # obliczamy ile jest punków o danej wartości współrzędnej
  for i in range(n):
    xStrength[P[i][0]] += 1
    yStrength[P[i][1]] += 1
  #end for
  
  # obliczamy ile jest punków o wartości współrzędnej mniejszej lub równej indeksowi w talicy (wyznaczamy wartość |X| i |Y| dla odpowiednich punktów)  
  for i in range(1, n + 1):
    xStrength[i] += xStrength[i - 1]
    yStrength[i] += yStrength[i - 1]
  #end for
  
  maxDominance = 0
  
  # korzystamy z wyprawodzonego wzoru
  for x, y in P:
    currentPointPseudoStrength = xStrength[x - 1] + yStrength[y - 1] - n + 1
    maxDominance = my_max(maxDominance, currentPointPseudoStrength)
  #end for

  return maxDominance

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
