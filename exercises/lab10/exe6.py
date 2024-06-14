# Zadanie 6 (ścieżka w drzewie) Dane jest drzewo ukorzenione T, gdzie każdy wierzchołek v ma potencjalnie ujemną 
# wartość value (v). Proszę zaproponować algorytm, który znajduje wartość najbardziej wartościowej ścieżki w drzewie T.

# Rozwiązanie:
# Definiujemy funkcję f(node) - ścieżka o maksymalnej sumie wartości wierzchołków wychodząca z wierzchołka node w poddrzewie
# gdzie node jest korzeniem. Wartość takiej funkcji możemy obliczyć jako: node.val + max(0, f(node.left), f(node.right)).
# Szukaną wartością najbardziej wartościowej ścieżki jest max z wartości: max(0, f(node), f.val +f(node.left) + f(node.right)), 
# wyznaczony dla każdego wierzchołka w drzewie. Następujący wzór otrzymujemy, ponieważ możemy mieć 3 możliwe przypadki:
# 1) wszystkie wierzchołki mają wartości ujemne, więc ścieżka zawierająca 0 wierzchołków ma najlepszą wartość równą zero
# 2) najlepsza ścieżka wychodzi z jednego wierzchołka i "idzie" tylko w jedną stronę (w prawo lub w lewo)
# 3) najlepsza ścieżka zawiera się w pewnym podrzewie i przechodzi przez korzeń tego poddrzewa (możemy tą ścieżkę potraktować
# jako "rozgałęzienie dwóch ścieżek wychodzących z jednego wierzchołka") 

class TreeNode:
    def __init__(self, val = None, left = None, right = None) -> None:
        self.left = left
        self.right = right
        self.val = val

def max_path(node: TreeNode) -> int:
    if node is None:
        return 0
    
    nodePath = calculate_max_path_from_given_node(node)
    fLeft = calculate_max_path_from_given_node(node.left)
    fRight = calculate_max_path_from_given_node(node.right)
    bestLocalSum =  max(0, nodePath, node.val + fLeft + fRight)

    return max(bestLocalSum, max_path(node.left), max_path(node.right))


def calculate_max_path_from_given_node(node: TreeNode) -> int:
    if node is None:
        return 0
    elif hasattr(node, "f"):
        return node.f
    
    leftPath = calculate_max_path_from_given_node(node.left)
    rightPath = calculate_max_path_from_given_node(node.right)
    node.f = node.val + max(0, leftPath, rightPath)

    return node.f

if __name__ == "__main__":
    print("######## test 1 ########\n\n")

    # Tree:
    #             5
    #            / \
    #          -2   3
    #                \
    #                 10

    u = TreeNode(-2)
    z = TreeNode(10)
    w = TreeNode(3, right=z)
    v = TreeNode(5, u, w)

    print(f"max path in this tree has value: {max_path(v)}")

    print("\n\n######## test 2 ########\n\n")

    # you can see this tree graph_algorithms/graphs/tree2.png

    root = TreeNode(-4, 
            TreeNode(10,
                TreeNode(7,
                    TreeNode(8,
                        TreeNode(1,
                            TreeNode(-5,
                                TreeNode(-4)
                            )
                        ),
                        TreeNode(-7, 
                            right=TreeNode(1)
                            )
                    )
                ),
                TreeNode(-5,
                     TreeNode(-100),
                     TreeNode(2,
                          TreeNode(20),
                          TreeNode(7)
                         )
                    )
                ),
            TreeNode(-8)
            )

    print(f"max path in this tree has value: {max_path(root)}")

