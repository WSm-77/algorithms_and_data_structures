# also works as binary search
def find_insert_index(tab, val):
    beg, end = 0, len(tab) - 1
    while beg <= end:
        mid = (beg + end) // 2
        if tab[mid] == val:
            return mid
        elif val >= tab[mid]:
            beg = mid + 1
        else:
            end = mid - 1
    return beg


# Example usage
if __name__ == "__main__":
    tab = [1, 5, 6, 6, 8, 9]
    print(tab)
    for val in range(1, 13):
        insert_index = find_insert_index(tab, val)
        print(f"val: {val}, insert index: {insert_index}")
