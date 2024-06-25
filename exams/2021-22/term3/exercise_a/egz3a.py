# Opis algorytmu:
# Dzielimy każdy przedział na dwa eventy: początek i koniec. Sortujemy tablicę powstałych eventów po wartościach, 
# a jeżeli dane eventy mają te same wartości to wcześniej występują te eventy, które są początkami jakiegoś przedziału.
# Przechodzimy po tak posortowanej tablicy eventów śledząc aktualną wysokość śniegu: jeżeli napotkamy początek 
# przediału to zwiększamy licznik wysokości śniegu a jeżli spotakmy koniec przedziału to zmniejszamy nasz licznik.
# Rozwiązaniem jest maksymalna wysokość śniegu.

from egz3atesty import runtests

class Event:
    def __init__(self, val, isBeg) -> None:
        self.val = val
        self.isBeg = isBeg
    
    def __repr__(self) -> str:
        return f"Event({self.val},{self.isBeg})"

def snow( T, I ):
    eventsTab: list[Event] = []
    for beg, end in I:
        eventsTab.append(Event(beg, True))
        eventsTab.append(Event(end, False))
    
    eventsTab.sort(key=lambda x: (x.val, -int(x.isBeg)))

    maxSnow = 0
    snowAmount = 0

    for event in eventsTab:
        if event.isBeg:
            snowAmount += 1
            maxSnow = max(maxSnow, snowAmount)
        else:
            snowAmount -= 1

    return maxSnow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
