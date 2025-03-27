from kol1testy import runtests

def select_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_val_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_val_idx]:
                min_val_idx = j
        arr[i], arr[min_val_idx] = arr[min_val_idx], arr[i]

def get_bucket_idx(value, bucket_size):
    return int(value / bucket_size)

def bucket_sort(arr, M):
    n = len(arr)

    buckets = [[] for _ in range(n)]

    bucket_size = M / n

    for value in arr:
        idx = get_bucket_idx(value, bucket_size)
        buckets[idx].append(value)

    # print("before sorting")
    # print(buckets)

    # print("after sorting")
    idx = 0
    for bucket in buckets:
        select_sort(bucket)

        # print(bucket)

        for val in bucket:
            arr[idx] = val
            idx += 1

def ogrodzenie(M, D, T: list):
  # tu prosze wpisac wlasna implementacje
    n = len(T)
    sorted_T = sorted(T)
    bucket_sort(T, M)

    assert T == sorted_T, "oops... smth get wrong"

    # print(str(T)[:150] + "[za długie]..")

    res = 0

    for i in range(1, n):
        if T[i] - T[i-1] >= D:
            res += 1

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True)
