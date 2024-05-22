from kol2testy import runtests

############
# sposób I #
############

# Złożoność O(VE log* E)

class FindUnion:
    def __init__(self, V):
        self.representants = [i for i in range(V)]
        self.ranks = [0 for _ in range(V)]

    def find(self, ele):
        if self.representants[ele] != ele:
            self.representants[ele] = self.find(self.representants[ele])

        return self.representants[ele]

    def union(self, ele1, ele2):
        repr1 = self.find(ele1)
        repr2 = self.find(ele2)

        if repr1 == repr2:
            return

        if self.ranks[repr1] < self.ranks[repr2]:
            self.representants[repr1] = repr2
        else:
            self.representants[repr2] = repr1
            if self.ranks[repr1] == self.ranks[repr2]:
                self.ranks[repr1] += 1

    def reset(self):
        V = len(self.representants)

        for vertex in range(V):
            self.representants[vertex] = vertex
            self.ranks[vertex] = 0

    def __repr__(self) -> str:
        return f"FindUnion({self.representants})"
# FindUnion

def graph_to_edges(G):
    V = len(G)
    edges = []

    for vertex in range(V):
        for neighbour, weight in G[vertex]:
            if neighbour < vertex: 
                continue
            edges.append((vertex, neighbour, weight))

    return edges


def beautree( G ):
    V = len(G)
    edges = graph_to_edges(G)
    E = len(edges)

    edges.sort(key=lambda x: x[2])

    sets = FindUnion(V)

    for edgeIdx in range(E - V + 1):
        sets.reset()
        weightsSum = 0
        visitedAllVerticies = True
        for i in range(V - 1):
            vertex, neighbour, weight = edges[edgeIdx + i]
            if sets.find(vertex) == sets.find(neighbour):
                visitedAllVerticies = False
                break
            else:
                sets.union(vertex, neighbour)
            weightsSum += weight
        
        if visitedAllVerticies:
            return weightsSum
        
    return None
        
#############
# sposób II #
#############

# Złożoność O(VE)

# Sortujemy krawędzie po najmniejszych wagach, a następnie tworzymy podgraf o V - 1 krawędziach z minimalnymi wagami
# i sprawdzamy czy jest on drzewem: jeżeli tak, to znaleźliśmy minimalne piękne drzewo, w przeciwnym wypadku usuwamy 
# z naszego podgrafu krawędź o najmniejszej wadze i dodajemy kolejną krawędź o najmniejszej wadze z oryginalnego grafu
# i ponownie sprawdzamy czy jest on drzewem. Postępujemy tak do czasu znalezienia drzewa. Jeżeli nie znaleźliśmy żadnego
# to oznacza to, że nie istnieje żadne piękne drzewo.

def is_tree(treeCandidate):
    def dfs(vertex):
        nonlocal treeCandidate, visited, visitedCnt

        visited[vertex] = True
        visitedCnt += 1

        for neighbour in treeCandidate[vertex]:
            if not visited[neighbour]:
                dfs(neighbour)
    #end def

    V = len(treeCandidate)
    visited = [False for _ in range(V)]
    visitedCnt = 0
    
    dfs(0)

    return visitedCnt == V

def beautree2( G ):
    V = len(G)
    edges = graph_to_edges(G)
    E = len(edges)
    edges.sort(key = lambda x: x[2])
    treeSum = 0
    tree = [[] for _ in range(V)]

    # create graph from V - 1 least weighted edges
    for edgeIdx in range(V - 1):
        vertex, neighbour, weight = edges[edgeIdx]
        tree[vertex].append(neighbour)
        tree[neighbour].append(vertex)
        treeSum += weight

    if is_tree(tree):
        return treeSum

    for edgeIdx in range(E - V):
        oldVertex, oldNeighbour, oldWeight = edges[edgeIdx]
        oldNeighbourIdx = 0
        oldVertexIdx = 0

        while tree[oldVertex][oldNeighbourIdx] != oldNeighbour:
            oldNeighbourIdx += 1
        while tree[oldNeighbour][oldVertexIdx] != oldVertex:
            oldVertexIdx += 1
        
        tree[oldVertex].pop(oldNeighbourIdx)
        tree[oldNeighbour].pop(oldVertexIdx)

        newVertex, newNeighbour, newWeight = edges[edgeIdx + V - 1]

        tree[newVertex].append(newNeighbour)
        tree[newNeighbour].append(newVertex)

        treeSum = treeSum - oldWeight + newWeight

        if is_tree(tree):
            return treeSum
    #end for

    return None

# runtests (beautree, all_tests = True)
runtests (beautree2, all_tests = True)
