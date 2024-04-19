from zad4testy import runtests

def bin_search(L, elem):
  beg = 0
  end = len(L) - 1

  while beg <= end:
    mid = (beg + end) // 2
    if L[mid][0] < elem:
      beg = mid + 1
    else:
      end = mid - 1
    #end if
  #end while
  return beg


def Flight(L,x,y,t):
  # tu prosze wpisac wlasna implementacje

  def rek(currentVertex, minCeiling, maxCeiling):
    nonlocal L, y, t, n
    if currentVertex == y:
      return True
    
    idx = bin_search(L, currentVertex)
    while idx < n and L[idx][0] == currentVertex:
      currentCeilling = L[idx][2]
      newMaxCeiling = min(maxCeiling, currentCeilling + t)
      newMinCeiling = max(minCeiling, currentCeilling - t)
      if newMinCeiling <= newMaxCeiling:
        if rek(L[idx][1], newMinCeiling,  newMaxCeiling):
          return True
      idx += 1
    #end while
    return False
  #end def

  n = len(L)

  return rek(x, -float("inf"), float("inf"))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
