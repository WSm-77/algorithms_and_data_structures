# Sprawdzić czy istnieje wierzchołek w grafie skierowanym, do którego wchodzą krawędzie wychodzące z wszystkich 
# innych wierzchołków i żadna krawędź z niego nie wychodzi (reprezentacja macierzowa)    PL

# Check whether there is a vertex in a directed graph that has edges coming from all other vertices and no edges
# leaving it (matrix representation)   ENG

# example:

# V: 0 1 2 3 4

#    0 1 1 0 1      0
#    0 0 1 0 0      1
#    0 0 0 0 0      2
#    1 0 1 0 1      3
#    1 0 1 0 0      4

# we are looking for vertex 2


# first approach:
# we pick candidate and check if there exists an neighbour vertex with bigger id; if it exists it becomes our new candidate
# we traverse through graph until we find candidate that has no neighbours with bigger id; the last step is to check if
# our candidate meets requirements

def check_version_1(G):
    V = len(G)
    candidate = 0
    nextCandidate = 1
    while nextCandidate < V:
        if G[candidate][nextCandidate] == 1:
            candidate = nextCandidate
        
        nextCandidate += 1
    
    for i in range(candidate):
        if G[i][candidate] == 0 or G[candidate][i] == 1:
            return (False, candidate)
        
    # by using 2 loops we skip G[candidate][candidate] which we konw is equal to 0
    for i in range(candidate + 1, V):
        if G[i][candidate] == 0 or G[candidate][i] == 1:
            return (False, candidate)
    
    return (True, candidate)

# second approach:
# we traverse throught matrix moving like chess king; if we stay at 0 we move right; otherwise we move down; our candidate
# is number of row on which we meet end of the board; the last step is the same as in the first approach

def check_version_2(G):
    V = len(G)
    currentRow = 0
    currentColl = 0

    while currentColl < V:
        if G[currentRow][currentColl] == 0:
            currentColl += 1
        else:
            currentRow += 1
        #end if
    #end while

    for i in range(currentRow):
        if G[i][currentRow] == 0 or G[currentRow][i] == 1:
            return (False, currentRow)
        
    # by using 2 loops we skip G[currentRow][currentRow] which we konw is equal to 0
    for i in range(currentRow + 1, V):
        if G[i][currentRow] == 0 or G[currentRow][i] == 1:
            return (False, currentRow)
    
    return (True, currentRow)


if __name__ == "__main__":
    graph7 = [[0, 1, 1, 0, 1],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [1, 0, 1, 0, 1],
              [1, 0, 1, 0, 0]]
    

    print(f"version 1: {check_version_1(graph7)}\tversion2: {check_version_2(graph7)}")


    graph8 = [
        #0 1 2 3 4 5 6 7 8
        [0,0,0,0,1,0,1,0,0], #0
        [0,0,0,1,0,1,1,0,0], #1
        [0,1,0,0,1,0,1,0,1], #2
        [0,0,0,0,1,1,1,1,0], #3
        [0,1,1,0,0,0,1,0,0], #4
        [0,1,0,1,0,0,1,0,0], #5
        [0,0,0,0,0,0,0,0,0], #6
        [0,0,1,0,0,0,1,0,0], #7
        [0,0,1,0,0,0,1,1,0]  #8
        ]
    
    print(f"version 1: {check_version_1(graph8)}\tversion2: {check_version_2(graph8)}")

    graph9 = [
        #0 1 2 3 4 5 6
        [0,1,0,0,1,0,0], #0
        [1,0,0,1,1,1,1], #1
        [0,0,0,0,1,1,0], #2
        [0,0,0,0,0,1,0], #3
        [0,1,1,0,0,0,0], #4
        [0,1,0,1,0,0,0], #5
        [0,0,0,0,0,0,0]  #6
        ]
    
    print(f"version 1: {check_version_1(graph9)}\tversion2: {check_version_2(graph9)}")