from random import randint

def binary_search(tab: list, number: int) -> bool:
    n = len(tab)
    beg, end = 0, n - 1

    while end - beg > 1:
        mid = (beg + end) // 2
        if number < tab[mid]:
            end = mid
        else:
            beg = mid
        #end if
    #end while

    return tab[end] == number or tab[beg] == number

if __name__ == "__main__":
    tab = sorted([randint(1, 100) for _ in range(randint(8, 15))])
    print(f"array: {tab}")
    for number in range(1, 20 + 1):
        inArray = binary_search(tab, number)
        print(f"is {number} in array?\t{inArray}")
