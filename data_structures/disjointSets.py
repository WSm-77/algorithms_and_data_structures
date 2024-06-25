class DisjointSet:
    def __init__(self, setLen) -> None:
        self.representant: list[int] = [i for i in range(setLen)]
        self.rank: list[int] = [0]*setLen
    
    def find(self, elem):
        while self.representant[elem] != elem:
            self.representant[elem] = self.representant[self.representant[elem]]
            elem = self.representant[elem]
        #end while
        return elem
    
    def in_same_set(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        xRepr = self.find(x)
        yRepr = self.find(y)
        
        # check if x and y are in the same set
        if xRepr == yRepr:
            return
        
        if self.rank[xRepr] < self.rank[yRepr]:
            self.rank[yRepr] += self.rank[xRepr]
            self.representant[xRepr] = yRepr
        else:
            self.rank[xRepr] += self.rank[yRepr]
            self.representant[yRepr] = xRepr
        #end if

if __name__ == "__main__":
    testSet = DisjointSet(10)
            
    testSet.union(0,1)
    testSet.union(0,6)
    testSet.union(7,8)
    testSet.union(8,9)
    print(testSet.representant)
    print(testSet.in_same_set(0, 8))

    testSet.union(0,7)
    print(testSet.representant)
    print(testSet.in_same_set(0, 8))

    print(testSet.find(8))
    print(testSet.representant)