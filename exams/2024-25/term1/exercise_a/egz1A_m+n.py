# Rozwiązanie:
# Tworzymy listę "battlefield", która reprezentuje pole bitwy. Uzupełniamy tę listę informacją czy dane pole jest puste
# czy zajmowane przez katapultę lub procesor. Następnie tworzymy stos, na którym przechowujemy infromacje o katapultach,
# które jeszcze nie oddały strzału. Przechodząc po kolejnych polach listy "battlefield" wykonujemy następujące akcje:
#
# 1) jeśli pole jest puste - nie robimy nic
# 2) jeśli na polu jest katapulta odkładamy ją na szczyt stosu katapult, które jeszcze nie wykonały strzału
# 3) jeśli na polu jest procesor to ściągamy katapulty ze stosu dopóki nie znajdziemy katapulty mającej zasięg na obecny
#    procesor albo stos się nie wyczerpie
#
# dzięki temu mamy gwarancję, że strzały z katapult się nie krzyżują, bo po napotkaniu procesora wybieramy najbliższą 
# katapultę, która nie oddała strzału i ma wystarczający zasięg. Jest to najbardziej optymalny wybór, gdyż w procesie
# ściągania katapult ze stosu eliminujemy katapulty, które nie mają zasięgu na najbliższy jeszcze nie zniszczony procesor,
# więc nie mają również zasięgu na dalsze procesory. Wybieranie najbliższego jeszcze niezniszczonego procesora 
# maksymalizuje liczbę zniszczeń, ponieważ jeśli nie wybralibyśmy najbliższego niezniszczonego procesora, to poprzednia
# katapulta, która jeszcze nie strzelała nie mogłaby do niego strzelić, gdyż ogień by się krzyżował, więc musiałaby wybrać
# dalszy procesor, co mogłoby spowodować, że nie będzie miała na niego zasięgu.
#
# Analiza złożoności:
# Stworzenie tablicy "battlefield" długości O(4m + 4n) ~ O(m + n)
# Wypełnienie tablicy "battlefield" O(m + n)
# Analiza poszczególnych pól "battlefield" O(m + n)
# Utrzymanie stosu O(m) (dokładanie do stosu) + O(m) (odkładanie ze stosu) ~ O(m)
# Sumarycznie O(m + n)

from egz1Atesty import runtests
from collections import deque

EMPTY = 0
PROCESSOR = 1
CATAPULT = 2

def battle(P,K,R):
    processors = P
    catapults = K
    catapults_ranges = {catapult : catapult_range for catapult, catapult_range in zip(K, R)}
    
    n = len(catapults)
    m = len(processors)

    battlefield = [EMPTY for _ in range(4 * n + 4 * m)]

    for processor in processors:
        battlefield[processor] = PROCESSOR
    
    for catapult in catapults:
        battlefield[catapult] = CATAPULT
    
    shoots_stack = deque()
    res = 0

    for idx, field in enumerate(battlefield):
        if field == EMPTY:
            continue
        elif field == CATAPULT:
            shoots_stack.append(idx)
        elif field == PROCESSOR:
            while shoots_stack:
                last_catapult = shoots_stack.pop()
                distance = idx - last_catapult
    
                if distance <= catapults_ranges[last_catapult]:
                    res += 1
                    break

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=True )