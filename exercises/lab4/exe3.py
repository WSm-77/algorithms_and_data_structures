# Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, każde nad alfabetem długości k,
# sprawdza czy A i B są swoimi anagramami.
# 1. Proszę zaproponować rezwiązanie działające w czasie O(n+k)
# 2. Proszę zaproponować rozwiązanie działające w czasie O(n) (proszę zwrócić uwagę, że k może być dużo większe od 
# np. dla alfabetu UNICODE; złożoność pamięciowa może być rzędu)

def char2index(char):
    return ord(char) - ord("a")

# AD1
def is_anagram(A, B, k):
    if len(A) != len(B):
        return False
    
    tab = [0]*k

    for char in A:
        tab[char2index(char)] += 1

    for char in B:
        tab[char2index(char)] -= 1
        if tab[char2index(char)] < 0:
            return False
        
    return True

# AD2
# korzystamy z biblioteki numpy: np.empty(), aby nie wypełniać tablicy k-elementowej startowymi wartościami
# podpunktu przechodzimy najpierw przez tablicę A i wyzerowujemy te elementy (aby pozbyć się śmieci) a potem kontynuujemy

import numpy as np

def is_anagram_2(A, B, k):
    n = len(A)
    if len(B) != n:
        return False
    
    lettersCnt = np.empty(k)

    for char in A:
        lettersCnt[ord(char)] = 0

    for char in A:
        lettersCnt[ord(char)] += 1

    for char in B:
        lettersCnt[ord(char)] -= 1
        if lettersCnt[ord(char)] < 0:
            return False
    
    return True


if __name__ == "__main__":
    word1 = "kotle"
    word2 = "lotek"
    numberOfLettersInAplhabet = 26
    print(f"{word1} {word2} {is_anagram(word1, word2, numberOfLettersInAplhabet)}")

    word1 = "abb"
    word2 = "aab"
    print(f"{word1} {word2} {is_anagram(word1, word2, numberOfLettersInAplhabet)}")