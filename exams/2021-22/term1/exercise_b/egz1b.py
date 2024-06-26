# Opis algorytmu:
# Najpierw musimy wyznaczyć, na którym poziomie mają finalnie znajdować się wszystkie liści. W tym celu korzystamy
# z algorytmu BFS do wyznaczenia liczby node'ów na każdym poziomie drzewa. Następnie znajdujemy poziom, na którym
# jest najwięcej node'ów - na tym poziomie będą znajdować się nasze liści. Kolejny krok to zaznaczenie czy dany node
# będzie znajdował się w naszym uciętym drzewie czy nie. Korzystamy z pola "x" w klasie "Node" do zapisania tej 
# informacji. Ostatni krok to wyliczenie liczby cięć: dla każdego noda jeżli znajduje się on w drzewie to musimy
# usunąć wszystkich jego synów, którzy w tym drzewie się nie znajdą.
# 
# Złożoność obliczeniowa:
# Przechodzimy po drzewie 3 krotnie odwiedzając każdego noda oraz przechodzimy jednokrotnie po tablicy z zapisaną
# liczbą node'ów na każdym poziomie (ta tablica ma długość równą wysokości drzewa, która nie może przekroczyć liczby 
# node'ów), więc złożoność obliczeniowa wynosi: O(n), gdzie n - liczba node'ów


from egz1btesty import runtests
from collections import deque

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def get_number_of_nodes_at_each_level(root: Node):
  toCheck: deque[tuple[int, Node]] = deque()
  toCheck.append((0, root))
  nodesCnt = 0
  prevLevel = 0
  level = 0
  eachLevelCnt = []

  while toCheck:
    level, node = toCheck.popleft()
    if level != prevLevel:
      eachLevelCnt.append(nodesCnt)
      nodesCnt =  0
      prevLevel = level
    nodesCnt += 1
    
    if node.left:
      toCheck.append((level + 1, node.left))
    if node.right:
      toCheck.append((level + 1, node.right))

  eachLevelCnt.append(nodesCnt)
  
  return eachLevelCnt

def find_max_height_of_widthest_tree(eachLevelCnt: list[int]):
  n = len(eachLevelCnt)
  maxNodes = 0
  maxNodesIdx = n - 1

  for i in range(n - 1, -1, -1):
    if maxNodes < eachLevelCnt[i]:
      maxNodes = eachLevelCnt[i]
      maxNodesIdx = i
  
  return maxNodesIdx

def get_number_of_removals(level, root):
  def mark_nodes(node: Node, currLevel):
    nonlocal level
    if currLevel == level:
      node.x = True
      if node.left:
        node.left.x = False
      if node.right:
        node.right.x = False
      return
    
    node.x = False
    if node.left:
      mark_nodes(node.left, currLevel + 1)
      node.x = node.left.x 

    if node.right:
      mark_nodes(node.right, currLevel + 1)
      node.x = node.x or node.right.x
  #end def
  
  def cnt_removals(node: Node):
    if not node.x:
      return 1
    
    res = 0
    if node.left:
      res += cnt_removals(node.left)
    if node.right:
      res += cnt_removals(node.right)
    return res
  #end def
      
  mark_nodes(root, 0)

  return cnt_removals(root)

def wideentall( T ):
    # tu prosze wpisac wlasna implementacje

    eachLevelCnt = get_number_of_nodes_at_each_level(T)
    leavesLevel = find_max_height_of_widthest_tree(eachLevelCnt)

    return get_number_of_removals(leavesLevel, T)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )
