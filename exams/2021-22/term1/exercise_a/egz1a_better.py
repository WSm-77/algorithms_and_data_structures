# Opis algorytmu:
# Chcemy zebrać jak najwięcej śniegu, więc zawsze bierzemy najwięcej jak się da, dopóki nie okaże się, że wzieliśmy
# cały śnieg albo cały śnieg stopniał. Zauważmy jednak, że w ten sposób wyznaczamy tylko zbiór pól, z których będziemy
# zbierać śnieg. W rzeczywistości śnieg będziemy zbierać w kolejności występowania tych elementów z zachodniej lub
# wschodniej stronie wąwozu, ale interesuje nas wyłącznie suma elementów z wyznaczonego zbioru. Musimy też pamiętać
# aby pomniejszyć otrzymaną sumę o liczbę ton, która zdążyła stopnieć w czasie, kiedy zbieraliśmy śnieg. Możemy 
# zauważyć, że liczba straconego śniegu w kolejnych dniach tworzy ciąg arytmetyczny o różnicy 1, zatem liczba stopionego
# śniegu jest równa sumie wyrazów z tego ciągu arytmetycznego.
#
# Złożoność obliczeniowa:
# O(n log n)

from egz1atesty import runtests

def snow( S ):
    # tu prosze wpisac wlasna implementacje
    n = len(S)
    S.sort(reverse=True)
    daysLeft = 0
    snowSum = 0
    while daysLeft < n and S[daysLeft] > daysLeft:
        snowSum += S[daysLeft]
        daysLeft += 1

    return snowSum - (daysLeft*(daysLeft - 1)) // 2

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
