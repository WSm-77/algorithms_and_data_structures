# Opis algorytmu:
# Każdy przedział dzielimy na dwa Eventy: początek i koniec. Zapisujemy dla nich: id (indeks w oryginalnej tablicy)
# i długość przedziału oraz wartość punktu i czy jest on początkiem czy końcem. Następnie sortujemy tablicę tak 
# stworzonych Eventów po wartościach pola val w taki sposób jak przedstawiono poniżej:
#                     0      1      2      3
# dla przedziałów: [[0,1], [0,3], [4,5], [2,6]]
#
# chcemy otrzymać następujący układ:
#
# ^
# |                 #####           2  
# |         #################       3
# | #####                           0
# | #############                   1
# + 0 - 1 - 2 - 3 - 4 - 5 - 6 - >
#
# Tworzymy swego rodzaju "wieże", gdzie każdy "niższy" poziom zawiera "wyższe", więc każda wieża tworzy zbiór 
# "fajnych" przedziałów. Jeżeli mielibyśmy doczynienia z rozdzielnymi wieżami np.:
#
# ^
# |                      ####
# |     #####          #######
# | #############      ##############
# +----------------------------------->
#
# to zauważamy, że wszystkie z tych przedziałów są "fajne".
# 
# Z przedziałami niefajnymi mamy doczynienia dopiero, gdzy wieże zaczynają na siebie nachodzić:
#
# ^
# |       ###        #####
# |      ######   @@######
# |     ##########@@
# | ###############################
# +----------------------------------->
# 
# Miejsca gdzie wieże na siebie nachodzą oznaczono znakiem "@".
#
# W naszym algorytmie wyznaczamy jeden z przedziałów, który na pewno jest "niefajny". Następnie dla niego
# szukamy drugiego przedziału, z którym jest on niefajny, a robimy to w następujący sposób:
# 
# Dla każdego eventu w posortowanej tablicy sprawdzamy czy jest on początkiem przedział:
#
# 1) jeżeli jest to zapisujemy ile jest wcześniej rozpoczętych przedziałów a następnie zwiększamy licznik 
#    "rozpoczętych przedziałów"
#
# 2) jeżeli nie jest to zmniejszamy licznik "rozpoczętych przedziałów" a następnie sprawdzamy czy licznik 
#    rozpoczętych przedziałów zgadza się z tym zapisanym dla rozważanego przedziału - jeżeli się nie zgadza
#    to oznacza, że wieże na siebie nachodzą, więc znaleźliśmy jeden z niefajnych przedziałów; w przeciwnym 
#    przypadku kontynuujemy nasz algorytm

from egz3btesty import runtests

########################
#        Events        #
########################

class Event:
  def __init__(self, id, val, length, isBeg) -> None:
    self.id = id
    self.val = val
    self.length = length
    self.isBeg = isBeg

  def __repr__(self) -> str:
    return f"Event({self.id}, {self.val}, {self.length}, {self.isBeg})"
  
########################
#   helper functions   #
########################

def print_sorted_intervals(intervalTab: list[list], eventsTab: list[Event]):
  for event in eventsTab:
    if event.isBeg:
      print(intervalTab[event.id])

#######################
#      heap sort      #
#######################

def heapify(heap, currIdx, lastIdx, cmp):
  while True:
    maxi = currIdx
    left = 2*currIdx + 1
    right = 2*currIdx + 2

    if left <= lastIdx and cmp(heap[maxi], heap[left]) == -1:
      maxi = left
    
    if right <= lastIdx and cmp(heap[maxi], heap[right]) == -1:
      maxi = right

    if maxi == currIdx:
      break

    heap[currIdx], heap[maxi]  = heap[maxi], heap[currIdx]
    currIdx = maxi

def build_heap(heap, cmp):
  n = len(heap)

  for i in range((n - 1) // 2, -1, -1):
    heapify(heap, i, n - 1, cmp)

def heap_sort(heap, cmp):
  n = len(heap)
  build_heap(heap, cmp)
  for lastIdx in range(n - 1, -1, -1):
    heap[0], heap[lastIdx] = heap[lastIdx], heap[0]
    heapify(heap, 0, lastIdx - 1, cmp)

def cmp_events(event1: Event, event2: Event):
  if event1.val < event2.val:
    return -1
  elif event1.val > event2.val:
    return 1

  if event1.isBeg != event2.isBeg:
    return -1 if event1.isBeg else 1
  
  if event1.isBeg:
    if event1.length < event2.length:
      return 1
    elif event1.length > event2.length:
      return -1
    
    if event1.id < event2.id:
      return -1
    elif event1.id > event2.id:
      return 1
  else:
    if event1.length < event2.length:
      return -1
    if event1.length > event2.length:
      return 1
    
    if event1.id < event2.id:
      return 1
    elif event1.id > event2.id:
      return -1

  return 0

#######################
#      main part      #
#######################

def are_uncool(interval1, interval2):
  return interval1[0] < interval2[0] <= interval1[1] < interval2[1] or \
         interval2[0] < interval1[0] <= interval2[1] < interval1[1]

def uncool( P ):
  # tu prosze wpisac wlasna implementacje

  n = len(P)

  eventTab: list[Event] = []

  for i in range(n):
    beg, end = P[i]
    length = end - beg
    eventTab.append(Event(i, beg, length, True))
    eventTab.append(Event(i, end, length, False))

  heap_sort(eventTab, cmp_events)

  ######## only for debug ########
  # print_sorted_intervals(P, eventTab)

  startedIntervalTab = [None for _ in range(n)]
  startedIntervalCnt = 0

  checked = []
  uncoolEventId = None

  for event in eventTab:
    if event.isBeg:
      startedIntervalTab[event.id] = startedIntervalCnt
      startedIntervalCnt += 1
      checked.append(event.id)
    else:
      startedIntervalCnt -= 1
      if startedIntervalTab[event.id] != startedIntervalCnt:
        # found one uncool interval
        uncoolEventId = event.id
        break

  uncoolInterval = P[uncoolEventId]
  for candidateId in checked:
    candidateInterval = P[candidateId]
    if are_uncool(uncoolInterval, candidateInterval):
      return (uncoolEventId, candidateId)
  
  return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )

# dodatkowe testy
testTab = [[1,2], [1,3], [0,3], [4,5], [2,6]]  # odp: (0, 4)
print(uncool(testTab))
testTab = [[0,1], [0,3], [4,5], [2,6]]         # odp: (1, 3)
print(uncool(testTab))
