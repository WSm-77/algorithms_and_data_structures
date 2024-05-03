def quick_select(tab, position):
    beg = 0
    end = len(tab) - 1

    while beg <= end:
        pivot = parition(tab, beg, end)
        if pivot == position:
            return tab[pivot]
        elif pivot < position:
            beg = pivot + 1
        else:
            end = pivot - 1

def parition(tab, beg, end):
    i = beg
    for j in range(beg, end):
        if tab[j] <= tab[end]:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
    
    tab[i], tab[end] = tab[end], tab[i]
    return i

if __name__ == "__main__":
    # Example usage
    arr = [12, 23, 17, 23, 9, 16, 7, 45, 6, 42, 33]
    k = 6
    kth_largest = quick_select(arr, len(arr) - k)
    print(sorted(arr))
    print(f"The {k}th largest element is: {kth_largest}")