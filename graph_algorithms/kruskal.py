class FindUnion():
    def __init__(self, V):
        self.representants = [i for i in range(V)]
        self.rank = [0 for _ in range(V)]

    def find(self, ele):
        if self.representants[ele] != ele:
            self.representants[ele] = self.find(self.representants[ele])

        return self.representants[ele]

    def union(self, set1, set2):
        rep1 = self.find(set1)
        rep2 = self.find(set2)

        if rep1 == rep2:
            return

        if self.rank[rep1] < self.rank[rep2]:
            self.representants[rep1] = rep2
        else:
            self.representants[rep2] = rep1
            if self.rank[rep1] == self.rank[rep2]:
                self.rank[rep1] += 1
    
    def __repr__(self) -> str:
        return f"FindUnion({self.representants})"


def get_number_of_verticies(edges: list):
    V = 0
    for vertex, neighbour, _ in edges:
        V = max(V, vertex, neighbour)

    return V + 1

def kruskal(edges: list):
    V = get_number_of_verticies(edges)

    edges.sort(key = lambda x: x[2])

    sets = FindUnion(V)

    MST = []

    for vertex, neighbour, weight in edges:
        if sets.find(vertex) == sets.find(neighbour):
            continue

        sets.union(vertex, neighbour)
        MST.append((vertex, neighbour, weight))

    return MST

if __name__ == "__main__":

    print("########### test 1 ###########\n\n")

    testGraph = [(0, 1, 2), (0, 2, 3), (0, 3, 7), (0, 4, 12), (1, 0, 2), (1, 2, 4), (1, 5, 2), (2, 0, 3), (2, 1, 4),
                (2, 4, 2), (2, 5, 9), (2, 6, 5), (3, 0, 7), (3, 4, 5), (4, 0, 12), (4, 2, 2), (4, 3, 5), (4, 6, 3),
                (5, 1, 2), (5, 2, 9), (5, 6, 1), (6, 2, 5), (6, 4, 3), (6, 5, 1)]

    print(f"MST (edges): {kruskal(testGraph)}")

    print("\n\n########### test 2 ###########\n\n")

    testGraph = [(0, 1, 1), (0, 2, 2), (1, 0, 1), (1, 3, 3), (1, 4, 2), (2, 0, 2), (2, 3, 1), (2, 6, 7), (3, 1, 3), 
                (3, 2, 1), (3, 5, 2), (3, 7, 3), (4, 7, 5), (5, 3, 3), (5, 6, 1), (5, 8, 8), (6, 2, 7), (6, 5, 1), 
                (6, 8, 4), (7, 3, 2), (7, 4, 5), (7, 8, 1), (8, 5, 8), (8, 6, 4), (8, 7, 1)]
    
    print(f"MST (edges): {kruskal(testGraph)}")