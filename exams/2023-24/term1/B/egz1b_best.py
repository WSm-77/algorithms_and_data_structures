# Opis algorytmu:
# Tworzymy funkcję f(j, i) - maksymalna suma elementów kończąca się na i-tym elementcie, przy założeniu, że pominięto
# maksymalnie j elementów. W celu wyznaczenia wartości tej funkcji rozważmy dwa przypadki:
# 1) bierzemy i-ty element do naszej sumy, więc mogliśmy wykorzystać wszystkie pominięcia dla poprzednich elementów
# 2) pomijamy i-ty element w naszej sumie, więc mogliśmy wykorzystać j-1 pominięć dla poprzednich elementów
# Ostateczny wzór naszej funkcji możemy wyrazić jako:
# f(j, i) = max( 
#         max( f(j, i - 1), 0 ) + T[i],           ~ bierzemy i-ty element, ale jeżeli poprzednia suma była ujemna
#                                                   to nasz element stanowi jednoelementową sumę 
#         f(j - 1, i - 1) )                       ~ nie bierzemy i-tego elementu do naszej sumy


from egz1btesty import runtests

def kstrong( T, k):
  # tu prosze wpisac wlasna implementacje
  
  n = len(T)
  f = [[0 for _ in range(n)] for _ in range(k+1)]

  f[0][0] = T[0]

  for i in range(1, n):
    f[0][i] = max(0, f[0][i-1]) + T[i]

  for currK in range(1, k+1):
    f[currK][0] = T[0]
    for i in range(1, n):
      f[currK][i] = max(max(0, f[currK][i - 1]) + T[i], f[currK - 1][i - 1])

  return max(f[k])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
