# Opis algorytmu:
# Najpierw należy zauważyć, że opłaca nam się wykonać maksymalnie jeden lot (jeżeli wykonalibyśmy loty z A -> B oraz 
# C -> D, to mogliśmy od razu przelecieć z A -> D). Teraz minimlaną trasą jest albo bezpośrednia trasa z s -> t albo
# minimalna trasa z s -> A + start z A + przylot do B + minimalna trasa B -> t, gdzie A i B są dowolnymi wierzchołkami 
# w grafie. Do wyznaczenia minimalnych tras wykorzystujemy 2 razy algorytm Dijkstry dla wierzchołków s oraz t.
# 
# Złożoność:
# O(E log V) 

from kol3btesty import runtests
from queue import PriorityQueue

INF = float("inf")

def dijkstra(graph, source):
    V = len(graph)
    distance = [INF for _ in range(V)]
    distance[source] = 0
    toCheck = PriorityQueue()
    toCheck.put((0, source))

    while not toCheck.empty():
        dist, vertex = toCheck.get()
        for neighbour, cost in graph[vertex]:
            newDist = dist + cost
            if newDist < distance[neighbour]:
                distance[neighbour] = newDist
                toCheck.put((newDist, neighbour))
    
    return distance

def airports( G, A, s, t ):
    # tu prosze wpisac wlasna implementacje

    distFromSource = dijkstra(G, s)
    distFromTarget = dijkstra(G, t)

    minDist = distFromSource[t]
    minDistFromSource = INF
    minDistFromTarget = INF

    for i in range(len(A)):
        distFromSource[i] += A[i]
        distFromTarget[i] += A[i]
        if distFromSource[i] < minDistFromSource:
            minDistFromSource = distFromSource[i]
        if distFromTarget[i] < minDistFromTarget:
            minDistFromTarget = distFromTarget[i]

    return min(minDist, minDistFromSource + minDistFromTarget)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )
