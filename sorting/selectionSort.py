from random import randint

def selection_sort(tab: list) -> None:
    n = len(tab)

    for i in range(n - 1):
        miniIndex = i
        for j in range(i + 1, n):
            if tab[j] < tab[miniIndex]:
                miniIndex = j
            #end if
        #end for
        tab[i], tab[miniIndex] = tab[miniIndex], tab[i]
    #end for

if __name__ == "__main__":
    tab = [randint(1, 100) for _ in range(randint(8, 16))]
    print(f"unsorted array: {tab}")
    selection_sort(tab)
    print(f"sorted array: {tab}")