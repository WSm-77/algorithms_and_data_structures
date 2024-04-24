# Sprawdź czy istnieje wierzchołek zwany "dobrym początekiem", z którego każdy inny wierzchołek jest osiągalny
# check if there exists a vertex called "good begening" from which every other vertex is achivable

# Wybieramy naszego kandydata na bycie dobrym początkiem i wywołujemy dfs; sprawdzamy czy wszystkie wierzchołki zostały 
# odwiedzone; jeżeli tak to znaleźliśmy dobry początek; w przeciwnym wypadku na nowego kandydata wybieramy pierwszy 
# wierzchołek, który nie został jeszcze odwiedzony (jeżeli dany wierzchołek został odwiedzony, a nie został odwiedzony 
# dowolny inny wierzchołek, to ten wierzchołek nie jest "dobrym początkiem", ponieważ nie ma ścieżki łączącej go z niedowiedzonym)
# wierzchołkiem); ponownie wywołujemy dfs, jednakże nie odwiedzamy wierzchołków które zostały już odwiedzone; powtarzamy ten proces
# dopóki nie znajdziemy ostatniego kandydata, dla którego wywołanie dfs'a powoduje odwiedzenie wszystkich wierzchołków;
# pozostaje nam sprawdzić czy dany wierzchołek jest dobrym początkiem (realizujemy to przy użyciu zwykłego wywołania dfs);
# 
# Dowód poprawności:
# Rozważmy ostatniego kandydata. Załużmy, że nie jest on dobrym początkiem oraz że dobry początek istnieje; oznaczałoby to, 
# że istnieje inny wierzchołek który nie został odwiedzony (gdyby został odwiedzony to nasz obecny kandydat nie mógłby zostać 
# kandydatem, ponieważ zostałby wcześniej odwiedzony); to z kolei oznaczałoby, że istnieje kolejny kandydat, więc nasz obecny
# nie jest ostatnim kandydatem ~ sprzeczność; oznacza to, że tylko ostatni kandydat (lub dowolny wierzchołek, który posiada ścieżkę
# prowadzącą do tego kandydata) może być dobrym początkiem  

def good_begening(G):
    def dfs_visit(vertex):
        nonlocal G, V,  visited, visitedCnt

        visited[vertex] = True
        visitedCnt += 1

        for neighbour in G[vertex]:
            if not visited[neighbour]:
                dfs_visit(neighbour)

    V = len(G)


    visited = [False]*V
    visitedCnt = 0
    for candidate in range(V):
        if not visited[candidate]:
            dfs_visit(candidate)
            if visitedCnt == V:
                break
            #end if
        #end if
    #end for

    result = None
    visitedCnt = 0
    visited = [False]*V
    dfs_visit(candidate)
    if visitedCnt == V:
        result = (True, candidate)
    else:
        result = (False, candidate)

    return result

if __name__ == "__main__":

    ####### test 1 #######

    print("test 1")

    graph21_list_modified = [[7],
                             [5, 9],
                             [3],
                             [4],
                             [2, 5],
                             [2],
                             [2, 10],
                             [1],
                             [3, 6],
                             [0],
                             [9, 8]]

    print(good_begening(graph21_list_modified))
    
    ####### test 2 #######

    print("\ntest 2")
    
    graph22_list = [[1],
                    [2],
                    [4],
                    [2],
                    [1, 5],
                    [6],
                    [7],
                    [8],
                    [9],
                    [6]]
    
    print(good_begening(graph22_list))

    ####### test 3 #######

    print("\ntest 3")

    graph22_list_modified = [[1, 3],
                             [2],
                             [4],
                             [2],
                             [1, 5],
                             [6],
                             [7],
                             [8],
                             [9],
                             [6]]
    
    print(good_begening(graph22_list_modified))