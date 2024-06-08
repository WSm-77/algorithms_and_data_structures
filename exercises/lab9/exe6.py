# Problem LIS (Longest Increasing Subsequence) w złożoności O(n log n).

# Rozwiązanie:
# Definiujemy funkcję f(i) jako najmniejszą liczbę, która kończy rosnący podciąg o długości i.

from random import randint

def binary_search(tab, val, key=lambda x,y: x<y):
    beg = 0
    end = len(tab) - 1

    while beg <= end:
        mid = (beg + end) // 2
        if key(tab[mid], val):
            beg = mid + 1
        else:
            end = mid - 1
    
    return beg

def longest_increaseing_subsequence(nums: list[int]) -> list[int]:
    n = len(nums)
    nums = [(nums[i], i) for i in range(n)]
    f = []
    parents = [None for _ in range(n)]

    for i in range(n):
        seqLength = binary_search(f, nums[i], lambda x, y: x[0] < y[0])

        if seqLength == len(f):
            f.append(nums[i])
        else:
            f[seqLength] = nums[i]

        parents[i] = f[seqLength - 1][1] if seqLength > 0 else None

    return get_sequence(nums, parents, f[-1][1])

def get_sequence(tab, parents, idx):
    sequence = []
    
    while idx != None:
        sequence.append(tab[idx][0])
        idx = parents[idx]

    sequence.reverse()
    return sequence

if __name__ == "__main__":
    testTab = [randint(1, 20) for _ in range(randint(8, 10))]
    print(f"tab:\n{testTab}")
    sequence = longest_increaseing_subsequence(testTab)
    print(f"\nLIS length: {len(sequence)}")
    print(f"longest increasing subseqense is:\n{sequence}")

