from kol2testy import runtests

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
        


runtests (beautree, all_tests = True)
