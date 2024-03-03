# given an array of length n; to "rotate" an array by k means to move all elements of this array of k indexes forward e.g. 0 -> k, 1 -> k + 1, ...

from random import randint

def rotate_array(arr: list, k: int) -> None:
    n = len(arr)
    k = k % n
    if k == 0:
        return
    rest = n % k
    periodical = rest == 0
    cycles = 1
    if periodical:
        cycles = k
    for i in range(cycles):
        prev = arr[i]
        j = i
        while True:
            j += k
            j %= n
            arr[j], prev = prev, arr[j]
            if j == i:
                break
        #end while
    #end for
            
if __name__ == "__main__":
    tab = [i for i in range(randint(8, 15))]
    k = randint(-10, 10)
    print(f"before rotation:\t{tab}")
    rotate_array(tab, k)
    print(f"rotated by {k} steps:\t{tab}")
