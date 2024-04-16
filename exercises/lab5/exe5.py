# Dany jest graf G = (V,E), gdzie każda krawędź ma wagę ze zbioru {1, ..., |E|} (wagi krawędzi są parami różne). Proszę zaproponować 
# algorytm, który dla danych wierzchołków x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach 
# o coraz mniejszych wagach.

def find_way_if_exists(G, weights: list[list[int]], x, y):
    def dfs_visit(vertex, prevWeight):
        nonlocal G, weights, y, way, found
        visited[vertex] = True
        way.append(vertex)

        for neighbourIdx in range(len(G[vertex])):
        # for neighbour in G[vertex]:
            neighbour = G[vertex][neighbourIdx]
            currentWeight = weights[vertex][neighbourIdx]
            if not visited[neighbour] and currentWeight < prevWeight:
                if neighbour == y:
                    found = True
                    way.append(neighbour)
                
                dfs_visit(neighbour, currentWeight)
                
                if found:
                    return
        #end for
        way.pop()
        visited[vertex] = False
    #end def

    V = len(G)
    visited = [False]*V
    found = False
    way = []

    dfs_visit(x, float("inf"))

    return found, way

if __name__ == "__main__":
    graph15 =  [[1,2,3],
                [0,2],
                [0,1,4,5,6],
                [0,4],
                [2,3,6],
                [2,6],
                [2,4,5]]
    
    weights =  [[2,6,7],
                [2,4],
                [6,4,10,9,8],
                [7,5],
                [10,5,3],
                [9,1],
                [8,3,1]]
    
    x = 0
    y = 5
    print(find_way_if_exists(graph15, weights, x, y))