from random import randint

def insertion_sort(tab: list) -> None:
    n = len(tab)

    for i in range(2, n):
        currenValue = tab[i]
        tab[0] = currenValue
        j = i - 1
        while currenValue < tab[j]:
            tab[j+1] = tab[j]
            j -= 1
        #end while
        tab[j+1] = currenValue
    #end for


if __name__ == "__main__":
    tab = [randint(1, 100) for _ in range(randint(8, 16))]
    print(f"unsorted array: {tab[1:]}")
    insertion_sort(tab)
    print(f"sorted array: {tab[1:]}")