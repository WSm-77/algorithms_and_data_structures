# Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów. Proszę podać możliwie jak najszybszy algorytm,
# który znajduje indeksy i oraz j, takie że wśród elementów, A[i], A[i + 1], ... , A[j] występują wszystkie k kolorów oraz wartość
# j - i jest minimalna (innymi słowy, szukamy minimalnego przedziału z wszystkimi kolorami).

from random import randint

def find_min_interval_with_all_colors(tab, k):
    n = len(tab)
    colorsCnt = [0]*k

    for color in tab:
        colorsCnt[color] += 1
    #end for
        
    colorsCntCp = [colorsCnt[i] for i in range(k)]

    found = False
    i1 = 0
    j1 = n - 1
    while not found:
        if colorsCnt[tab[i1]] - 1 > 0:
            colorsCnt[tab[i1]] -= 1
            i1 += 1
        elif colorsCnt[tab[j1]] - 1 > 0:
            colorsCnt[tab[j1]] -= 1
            j1 -= 1
        else:
            found = True
        #end if
    #end while
            
    found = False
    i2 = 0
    j2 = n - 1
    while not found:
        if colorsCntCp[tab[j2]] - 1 > 0:
            colorsCntCp[tab[j2]] -= 1
            j2 -= 1
        elif colorsCntCp[tab[i2]] - 1 > 0:
            colorsCntCp[tab[i2]] -= 1
            i2 += 1
        else:
            found = True
        #end if
    #end while

    i, j = i1, j1
    if j2 - i2 < j1 - i1:
        i, j = i2, j2
    #end if
    
    return i, j
    

###########
# testing #
###########

def contains_all_colors(tab, k):
    colors = set()
    
    for ele in tab:
        colors.add(ele)
        if len(colors) == k:
            return True
        #end if
    return False

if __name__ == "__main__":
    k = randint(3, 7)
    n = randint(k + 5, k + 15)
    testTab = [randint(0, k-1) for _ in range(n)]
    while not contains_all_colors(testTab, k):
        testTab = [randint(0, k-1) for _ in range(n)]
    print(f"n: {n}, k: {k}")
    print(testTab)
    i, j = find_min_interval_with_all_colors(testTab, k)
    print(f"i: {i}, j: {j}\n{testTab[i:j+1]}")