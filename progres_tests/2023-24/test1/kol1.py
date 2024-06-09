# Wiktor Sędzimir
# 
# opis algorytmu:
# Algorytm działa na bazie merge sorta. Na poczatku przypisujemy każdemu elementowi z tablicy unikalne id równe indeksowi w tablicy
# pod którym się pierwotnie znajduje (id będzie nam potrzebne do obliczenia rangi danego elementu). Następnie tworzymy talicę 
# zawierającą rangi poszczególnych elementów z tablicy. Kolejny krok to posortowanie naszej tablicy z wykorzystaniem algorytmu 
# merge sort. W trakcie łącznia tablic następuje faktyczne zliczanie rangi danego elementu. W trakcie scalania rangę danego elementu
# możemy zwiększyć, tylko, jeżeli dany element pochodzi z prawej tablicy (jeżeli pochodzi z lewej tablicy to jego rangę zwiększaliśmy)
# w poprzednich wywołaniach rekurencyjnych funkcji sortującej. Rozważmy przykład:
# dana jest tablica: [5, 3, 9, 4]
# po podzieleniu tabilc na mniejsze posortowane części otrzymujemy kolejno:
# t1: [5]    t2: [3]    t3: [9]    t4: [4]
# po złączeniu: 
# t1: [3, 5]      t2: [4, 9]        -  tutaj nie zwiększamy żadnej rangi
# ostatecznie:
# t: [3, 4, 5, 9]                   -  tutaj zwiększamy rangę "4" o 1 a "9" o 2
#
# Przy każdym łączeniu tablic dla danego elementu liczby, które mogą mieć od niego zarówno mniejszy indeks jak i wartość (a nie były już
# zliczane) znajdują się w lewej części tablicy. Dlatego przy każdym złączaniu tablic zwiększamy wartość elementu z prawej tablicy
# o liczbę elementów z lewej tablicy, które mają mniejszą wartość (bo na pewno mają już mniejszy indeks, co wynika z charakterystyki 
# dzielenia tablicy w merge sorcie).
# Po wyznaczeniu rangi każdego elementu wystarczy liniowo przejść po wszystkich elementach z tablicy rang i wyznaczyć maksimum.
# Algorytm ma złożoność O(n log n) ze względu na wykorzystanie lekko zmodyfikowanej wersji merge sorta.

from kol1testy import runtests

def merge(leftTab, rightTab, rankTab):
  n1 = len(leftTab)
  n2 = len(rightTab)

  resultTab = [0]*(n1 + n2)
  resIdx = 0

  i1 = 0
  i2 = 0

  while i1 < n1 and i2 < n2:
    if leftTab[i1][0] >= rightTab[i2][0]:
      rankTab[rightTab[i2][1]] += i1
      resultTab[resIdx] = rightTab[i2]
      i2 += 1

    else:
      resultTab[resIdx] = leftTab[i1]
      i1 += 1
    #end if
    resIdx += 1
  #end while

  if i1 >= n1:
    while i2 < n2:
      rankTab[rightTab[i2][1]] += i1
      resultTab[resIdx] = rightTab[i2]
      i2 += 1
      resIdx += 1
  else:
    while i1 < n1:
      resultTab[resIdx] = leftTab[i1]
      i1 += 1
      resIdx += 1

  return resultTab
      

def modified_merge_sort(T, rankTab):
  n = len(T)
  if n <= 1:
    return T
  
  mid = n // 2
  leftTab = modified_merge_sort(T[:mid], rankTab)
  rightTab = modified_merge_sort(T[mid:n], rankTab)

  return merge(leftTab, rightTab, rankTab)

def maxrank(T):
  # tu prosze wpisac wlasna implementacje  
  n = len(T)
  T = [(T[i], i) for i in range(n)]
  rankTab = [0]*n
  T = modified_merge_sort(T, rankTab)

  result = 0
  for ele in rankTab:
    if ele > result:
      result = ele

  return result 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True)
