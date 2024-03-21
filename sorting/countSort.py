from random import randint

# sorting numbers 0, 1, 2, ..., k-1
def count_sort(tab, k):
    n = len(tab)
    countTab = [0]*k
    sortedTab = [0]*n

    for ele in tab:
        countTab[ele] += 1
    
    for i in range(1, k):
        countTab[i] += countTab[i - 1]

    for i in range(n - 1, -1, -1):
        countTab[tab[i]] -= 1
        sortedTab[countTab[tab[i]]] = tab[i]

    return sortedTab

if __name__ == "__main__":
    n = 10
    k = 5
    testTab = [randint(0, k - 1) for _ in range(n)]
    print(testTab)
    testTab = count_sort(testTab, k)
    print(testTab)
