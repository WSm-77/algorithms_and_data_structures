# Skoro każdy z braci rozkład N palików zgodznie z rozkładem jednostajnym, to musimy znaleźć położenie ostatniego palika
# dla pierwszego z braci i pierwszego dla drugiego z braci. Wówczas będziemy mieli 2 tablice długości N, które będziemy mogli
# posortować liniowo. Po posortowaniu będziemy mogli przejść liniowo po wszystkich elementach porównując sąsiednie wartości
# z szerokością kombajnu.
#
# Złożoność obliczeniowa: O(n)
# 1. 2 x quick_select -> O(N) = O(n / 2)
# 2. 2 x bucket sort -> O(N) = O(n / 2)
# 3. liniowe przejście po tablicy -> O(n)

from kol1testy import runtests

def quick_select(arr, idx):
    beg = 0
    end = len(arr) - 1
    while beg <= end:
        pivot_idx = get_pivot(arr, beg, end)

        if idx == pivot_idx:
            return arr[pivot_idx]
        elif pivot_idx < idx:
            beg = pivot_idx + 1
        else:
            end = pivot_idx - 1

def get_pivot(arr, beg, end):
    i = beg
    for j in range(beg, end):
        if arr[j] <= arr[end]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[end] = arr[end], arr[i]

    return i

def select_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_val_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_val_idx]:
                min_val_idx = j
        arr[i], arr[min_val_idx] = arr[min_val_idx], arr[i]

def get_bucket_idx(value, bucket_size, min_val):
    # print(value, bucket_size, min_val)
    return int((value - min_val) / bucket_size)

def bucket_sort(arr, min_val, max_val):
    n = len(arr)

    buckets = [[] for _ in range(n)]

    bucket_size = (max_val - min_val) / n

    for value in arr:
        idx = get_bucket_idx(value, bucket_size, min_val)
        buckets[idx].append(value)

    idx = 0
    for bucket in buckets:
        select_sort(bucket)

        for val in bucket:
            arr[idx] = val
            idx += 1

    return arr

def ogrodzenie(M, D, T: list):
  # tu prosze wpisac wlasna implementacje
    n = len(T)
    sorted_T = sorted(T)

    mid2_idx = n // 2
    mid1_idx = mid2_idx - 1

    val1 = quick_select(T, mid1_idx)
    val2 = quick_select(T, mid2_idx)

    mid_val = (val1 + val2) / 2

    arr1 = bucket_sort(T[:mid1_idx + 1], 0, mid_val)
    arr2 = bucket_sort(T[mid2_idx:], mid_val, M)

    T = arr1 + arr2

    assert T == sorted_T, "oops... smth get wrong"

    res = 0

    for i in range(1, n):
        if T[i] - T[i-1] >= D:
            res += 1

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True)
