from random import randint

def bubble_sort(tab: list) -> None:
    n = len(tab)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]

if __name__ == "__main__":
    tab = [randint(1, 100) for _ in range(randint(8, 16))]
    print(f"unsorted array: {tab}")
    bubble_sort(tab)
    print(f"sorted array: {tab}")