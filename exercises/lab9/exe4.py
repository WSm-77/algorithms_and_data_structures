# dostajemy tablice n liczb naturalnych oraz parametr t, proszę sprawdzić czy istnieje podciąg z tej tablicy, który
# sumuje się do zadanej wartości t

def is_target_sum_achivable(tab: list[int], target: int):
    achivable = [False for _ in range(target + 1)]
    achivable[0] = True

    for num in tab:
        tmp = [ele for ele in achivable]
        for i in range(target + 1 - num):
            if achivable[i]:
                tmp[i + num] = True

        achivable, tmp = tmp, achivable

    return achivable[target]

if __name__ == "__main__":
    testTab = [2,3,1,4,7]
    target = 10
    print(is_target_sum_achivable(testTab, target))
    
    testTab = [2,4,5,2]
    target = 10
    print(is_target_sum_achivable(testTab, target))
