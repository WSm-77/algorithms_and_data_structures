# Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm, 
# który oblicza minimalną ilość monet potrzebną do wydania kwoty T (algorytm zachłanny, wydający najpierw 
# największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8+5+1+1 zamiast 5+5+5).

def min_coins_to_reach_target(coins, target):
    INF = float("inf")
    minSums = [INF for _ in range(target + 1)]
    parents = [None for _ in range(target + 1)]
    minSums[0] = 0

    for cost in range(target + 1):
        for coin in coins:
            if cost - coin < 0:
                continue
            if minSums[cost - coin] + 1 < minSums[cost]:
                minSums[cost] = minSums[cost - coin] + 1
                parents[cost] = cost - coin

    return minSums[target], get_coins(parents, target)

def get_coins(parents, target):
    coins = []
    ptr = target

    while parents[ptr] != None:
        next = parents[ptr]
        coins.append(ptr - next)
        ptr = next

    return coins

def test_fun(coins, target):
    minCoins, usedCoins = min_coins_to_reach_target(coins, target)
    print("avaliable coins:", end=" ")
    print(*coins, sep=", ")
    print(f"minimal number of coins to reach target cost: {minCoins}")
    print("used coins:", end=" ")
    print(*usedCoins, sep=", ")

if __name__ == "__main__":
    tests = [([1,5,8], 15), ([1,3,8], 15), ([1,2,7], 13)]

    testIdx = 1
    for test in tests:
        print(f"\n\n######## test {testIdx} ########\n\n")
        test_fun(*test)
        testIdx += 1
