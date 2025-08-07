# Rozwiązanie:
# Grzegorz odwiedza ośrodki w kolejności od tego, do którego jest najmniejszy koszt dostania się do tego o największym
# koszcie. Jest to dokładnie ten sam porządek odwidzania wierzchołków co porządek wyjmowania wierzchołków z kolejki
# priorytetowej w algorytmie Dijkstry. Dodatkowo Grzegorz nie chce przechodzić przez miasta, w których już odwiedził
# ośrodki, więc wprowadzamy dodatkową modyfikację, że jeżeli dotrzemy do miasta z ośrodkiem nie sprawdzamy sąsiadów,
# gdyż nie chcemy, aby jakakolwiek kolejna trasa przechodziła przez to miasto.

from kol2testy import runtests
from queue import PriorityQueue

INF = float('inf')

def get_v(edges):
    V = 0
    for vertex, neighbour, _ in edges:
        V = max(V, vertex, neighbour)
    return V + 1

def create_graph(edges):
    V = get_v(edges)

    graph = [[] for _ in range(V)]

    for vertex, neighbour, cost in edges:
        graph[vertex].append((neighbour, cost))
        graph[neighbour].append((vertex, cost))
    
    return graph

def lets_roll(start_city, flights, resorts):
    grpah = create_graph(flights)
    V = len(grpah)

    is_resort = [False for _ in range(V)]

    for resort in resorts:
        is_resort[resort] = True

    distances = [INF for _ in range(V)]
    visited = [False for _ in range(V)]

    queue = PriorityQueue()
    queue.put((0, start_city))
    distances[start_city] = 0

    while not queue.empty():
        cost, vertex = queue.get()

        if visited[vertex]:
            continue

        visited[vertex] = True

        if is_resort[vertex]:
            continue

        for neighbour, cost in grpah[vertex]:
            travel_cost = distances[vertex] + cost

            if visited[neighbour] or travel_cost > distances[neighbour]:
                continue

            distances[neighbour] = travel_cost

            queue.put((travel_cost, neighbour))
    
    total_cost = 0
    
    for resort in resorts:
        if visited[resort]:
            total_cost += 2 * distances[resort]

    return total_cost

runtests(lets_roll, all_tests = True)
