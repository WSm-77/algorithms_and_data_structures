from zad2testy import runtests

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cutthetree(T):
    """tu prosze wpisac wlasna implementacje"""
    def min_sum(node: BNode):
        nonlocal INF
        if node == None:
            return 0
        elif(node.left == None and node.right == None):
            return INF

        return min(node.value, min_sum(node.left) + min_sum(node.right))
    #end def

    INF = float("inf")
    left = min_sum(T.left)
    right = min_sum(T.right)
    if left == INF:
        left = 0
    if right == INF:
        right = 0
    
    return left + right

    
runtests(cutthetree)


