# na imprezę firmową wybierają się pracownicy pewnej firmy, przy czym istnieje zasada, że żaden manager nie idzie na 
# tę imprezę ze swoimi bezpośrednimi podwładnymi; każda osoba ma przypisany współczynnik imprezowości; znaleźć zbiór
# pracowników tej firmy, dla którego suma współczynników imprezowości będzie jak największa

class TreeNode:
    def __init__(self, fun, idx, left = None, right = None) -> None:
        self.fun = fun
        self.left = left
        self.right = right
        self.atParty = -1
        self.notAtParty = -1
        self.idx = idx

    def __repr__(self) -> str:
        return f"TreeNode(fun: {self.fun}, idx: {self.idx})"

def build_binary_tree_from_dict(valDict: dict[int, int]):
    def rek(idx):
        nonlocal valDict
        if idx not in valDict:
            return None
        
        node = TreeNode(valDict[idx], idx, rek(2*idx + 1), rek(2*idx + 2))

        return node
    # end def

    return rek(0)

def print_tree(root: TreeNode, key = lambda x: x):
    if root == None:
        return
    
    print(f"{key(root)}")
    print_tree(root.left, key)
    print_tree(root.right, key)

def party(root: TreeNode) -> int:
    def at_party(node: TreeNode):
        if node == None:
            return 0

        if node.atParty == -1:
            node.atParty = node.fun + not_at_party(node.left) + not_at_party(node.right)

        return node.atParty
    #end def

    def not_at_party(node: TreeNode):
        if node == None:
            return 0
        
        if node.notAtParty == -1:
            bothChildrenAtParty = at_party(node.left) + at_party(node.right)
            if node.notAtParty < bothChildrenAtParty:
                node.notAtParty = bothChildrenAtParty
            leftChildAtParty = not_at_party(node.right) + at_party(node.left)
            if node.notAtParty < leftChildAtParty:
                node.notAtParty = leftChildAtParty
            rightChildAtParty = not_at_party(node.left) + at_party(node.right)
            if node.notAtParty < rightChildAtParty:
                node.notAtParty = rightChildAtParty
            bothChildrenNotAtParty = not_at_party(node.left) + not_at_party(node.right)
            if node.notAtParty < bothChildrenNotAtParty:
                node.notAtParty = bothChildrenNotAtParty

        return node.notAtParty
    #end def

    return max(at_party(root), not_at_party(root))

def get_set(root: TreeNode):
    def rek(node: TreeNode, currentAtParty: bool):
        nonlocal result
        if node == None:
            return
        
        leftAtPartySum = 0 if node.left == None else node.left.atParty
        leftNotAtPartySum = 0 if node.left == None else node.left.notAtParty
        rightAtPartySum = 0 if node.right == None else node.right.atParty
        rightNotAtPartySum = 0 if node.right == None else node.right.notAtParty

        leftAtParty = False
        rightAtParty = False
        currentSum = leftNotAtPartySum + rightNotAtPartySum

        if not currentAtParty:
            if leftNotAtPartySum + rightAtPartySum > currentSum:
                leftAtParty = False
                rightAtParty = True
                currentSum = leftNotAtPartySum + rightAtPartySum
            if leftAtPartySum + rightNotAtPartySum > currentSum:
                leftAtParty = True
                rightAtParty = False
                currentSum = leftAtPartySum + rightNotAtPartySum
            if leftAtPartySum + rightAtPartySum > currentSum:
                leftAtParty = True
                rightAtParty = True
        else:
            result.append(node)

        rek(node.left, leftAtParty)
        rek(node.right, rightAtParty)


    result = []
    if root.atParty > root.notAtParty:
        rek(root, True)
    else:
        rek(root, False)

    return result

def test(testTree):
    root = build_binary_tree_from_dict(testTree)
    print("tree:")
    print_tree(root)
    print(f"\nbest party factor: {party(root)}")
    bestPartyParticipants = get_set(root)
    print(f"best party members:")
    print(*bestPartyParticipants, sep="\n")


if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    testTree = {0: 10,
                1: 3,
                2: 6,
                4: 5}
    test(testTree)

    print("\n\n######## test 2 ########\n\n")

    testTree = {0: 10,
                1: 3,
                2: 6,
                4: 5,
                5: 1,
                6: 1}
    
    test(testTree)

    print("\n\n######## test 3 ########\n\n")

    testTree = {0: 10,
                1: 3,
                2: 6,
                4: 5,
                5: 1,
                6: 1,
                11: 12,
                12: 10,
                13: 8,
                14: 3}
    
    test(testTree)