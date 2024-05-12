# Proszę zaimplementować domknięcie przechodnie grafu skierowanego w reprezentacji macierzowej (należy do grafu dodać wszystkie
# krawędzie, łączące wierzchołek z wszystkimi wierzchołkami, które są osiągalne z tego wierzchołka)

def transitiv_closure(G):
    V = len(G)
    for i in range(V):
        for v in range(V):
            for n in range(V):
                if G[v][n] == 1:
                    continue

                G[v][n] = G[v][i] * G[i][n]

    return G

def list_to_matrix(G):
    V = len(G)
    matrix = [[0 for _ in range(V)] for _ in range(V)]

    for vertex in range(V):
        for neighbour in G[vertex]:
            matrix[vertex][neighbour] = 1
    
    return matrix

def matrix_to_list(matrix):
    V = len(matrix)
    graph = [[] for _ in range(V)]

    for vertex in range(V):
        for neighbour in range(V):
            if matrix[vertex][neighbour]:
                graph[vertex].append(neighbour)

    return graph


def test(testGraph):
    matrixGraph = list_to_matrix(testGraph)
    resultGraphMatrix = transitiv_closure(matrixGraph)
    print("result graph:")
    print(*matrix_to_list(resultGraphMatrix), sep="\n")

if __name__ == "__main__":
    print("######### test 1 #########\n\n")

    graph1_list = [[1,2],
                   [4],
                   [3,5],
                   [4],
                   [5],
                   [6],
                   [7],
                   []]
    
    test(graph1_list)

    print("\n\n######### test 2 #########\n\n")

    graph2_list = [[1,2],
                   [],
                   [],
                   [6],
                   [],
                   [3,4],
                   [5]]
    
    test(graph2_list)

    print("\n\n######### test 3 #########\n\n")

    graph17_list = [[1,3,7],
                [2],
                [3,5,8],
                [4,6],
                [5],
                [6,7,8],
                [7],
                [8,9],
                [9],
                [10],
                []]
    
    test(graph17_list)