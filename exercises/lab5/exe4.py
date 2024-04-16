# Znany operator telefonii komórkowej Pause postanowił zakończyć działalność w Polsce. Jednym z głównych elementów całej 
# procedury jest wyłączenie wszystkich stacji nadawczych (które tworzą spójny graf połączeń). Ze względów technologicnzych 
# urządzenia należy wyłączać pojedyńczo, a operatorowi dodatkowo zależy na tym, by podczas całego procesu wszyscy abonenci znajdujący się 
# w zasięgu działających stacji mogli się e sobą łączyć (czyli by graf pozostał spójny).

def turn_off(G):
    def dfs_visit(vertex):
        nonlocal V, turnOffOrder, idx, visited

        visited[vertex] = True

        for neighbour in G[vertex]:
            if not visited[neighbour]:
                dfs_visit(neighbour)
        #end for
        turnOffOrder[idx] = vertex
        idx += 1
    #end def


    V = len(G)
    visited = [False]*V
    turnOffOrder = [0]*V
    idx = 0

    dfs_visit(0)

    return turnOffOrder

def matrix_to_linked_list(G):
    V = len(G)

    newG = [[] for _ in range(V)]
    for vertex in range(V):
        for neighbour in range(V):
            if G[vertex][neighbour] == 1:
                newG[vertex].append(neighbour)

    return newG

def check_solution(G, turnOffOrder):
    def is_connected():
        nonlocal G, V, turnedOff, turnedOffCnt

        def dfs_visit(vertex):
            nonlocal G, V, turnedOff, visited, visitedCnt, turnedOffCnt

            visited[vertex] = True
            visitedCnt += 1

            for neighbour in G[vertex]:
                if not visited[neighbour] and not turnedOff[neighbour]:
                    dfs_visit(neighbour)
            #end for
        #end def

        visited = [False]*V
        visitedCnt = 0

        dfs_visit(turnOffOrder[turnedOffCnt])

        return visitedCnt == V - turnedOffCnt
    #end def
    
    V = len(G)
    turnedOff = [False]*V
    turnedOffCnt = 0

    while turnedOffCnt < V - 1:
        turnedOff[turnOffOrder[turnedOffCnt]] = True
        turnedOffCnt += 1
        if not is_connected():
            # print(turnedOffCnt)
            return False
    #end while

    return True

if __name__ == "__main__":

    ############# test 1 #############

    graph4 = [
        #0,1,2,3,4,5,6
        [0,0,0,0,1,0,0], #0
        [0,0,0,0,1,1,1], #1
        [0,0,0,0,1,1,0], #2
        [0,0,0,0,0,1,0], #3
        [1,1,1,0,0,0,0], #4
        [0,1,1,1,0,0,0], #5
        [0,1,0,0,0,0,0]  #6
             ]
    
    graph4 = matrix_to_linked_list(graph4)
    
    print("test1:")
    turnOffOrder = turn_off(graph4)
    print(turnOffOrder)
    print(check_solution(graph4, turnOffOrder))
    
    
    ############# test 1 #############
    
    graph13 = [[1,4],
               [0,2,4],
               [1,3],
               [2,4],
               [0,1,3]]
    
    print("\ntest2:")
    turnOffOrder = turn_off(graph13)
    print(turnOffOrder)
    print(check_solution(graph13, turnOffOrder))