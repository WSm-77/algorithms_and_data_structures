from kol1testy import runtests

def ogrodzenie(M, D, T: list):
  # tu prosze wpisac wlasna implementacje
    n = len(T)

    T.sort()
    print(str(T)[:150] + "[za długie]..")

    res = 0

    for i in range(1, n):
        if T[i] - T[i-1] >= D:
            res += 1

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = False)
