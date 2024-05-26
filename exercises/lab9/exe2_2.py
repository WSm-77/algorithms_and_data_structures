# na imprezę firmową wybierają się pracownicy pewnej firmy, przy czym istnieje zasada, że żaden manager nie idzie na 
# tę imprezę ze swoimi bezpośrednimi podwładnymi; każda osoba ma przypisany współczynnik imprezowości; znaleźć zbiór
# pracowników tej firmy, dla którego suma współczynników imprezowości będzie jak największa

class TreeNode:
    def __init__(self, id, fun, employee) -> None:
        self.id = id
        self.fun = fun
        self.employee = employee
        self.bestParty = -1
        self.excludedBestParty = -1

    def __repr__(self) -> str:
        return f"TreeNode{self.id}({self.fun})"
#TreeNode

def build_tree(testTree: dict[int, tuple[int, list[int]]]) -> TreeNode:
    def rek(nodeId):
        node = TreeNode(nodeId, testTree[nodeId][0], [rek(id) for id in testTree[nodeId][1]])
        return node
    
    return rek(0)
    
def print_tree(node, key = lambda x: x):
    print(key(node))
    for employee in node.employee:
        print_tree(employee, key)

def party(root):
    def best_party(node):
        if node.bestParty != -1:
            return node.bestParty
        
        bestIncluded = node.fun
        for employee in node.employee:
            bestIncluded += excluded_best_party(employee)

        node.bestParty = excluded_best_party(node)
        if node.bestParty < bestIncluded:
            node.bestParty = bestIncluded

        return node.bestParty
        
    def excluded_best_party(node):
        if node.excludedBestParty != -1:
            return node.excludedBestParty
        
        bestExcluded = 0
        for employee in node.employee:
            bestExcluded += best_party(employee)

        node.excludedBestParty = bestExcluded

        return node.excludedBestParty
    
    bestParty = best_party(root)

    return bestParty, get_members(root)

def get_members(root: TreeNode):
    def rek(node: TreeNode, isMember):
        nonlocal members

        if isMember:
            members.append(node)
            for employee in node.employee:
                rek(employee, False)
        else:
            for employee in node.employee:
                rek(employee, employee.bestParty != employee.excludedBestParty)
            
    
    members = []
    rek(root, root.bestParty != root.excludedBestParty)

    return members

def test(testTree):
    root = build_tree(testTree)
    print("tree:")
    print_tree(root)
    bestParty, members = party(root)
    print(f"\nbest party factor: {bestParty}")
    print(f"best party members:")
    print(*sorted(members, key=lambda x: x.id), sep="\n")

if __name__ == "__main__":
    testTree = {0: (1, [1]),
                1: (15, [2,3,4]), 
                2: (10, [5,6]), 
                3: (15, [7,8]),
                4: (12, [9]),
                5: (8, []),
                6: (1, []),
                7: (10, [10]),
                8: (3, [11]),
                9: (6, []),
                10: (9, []),
                11: (7, [])}
    
    test(testTree)
