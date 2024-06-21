# Imię i nazwisko
# 
# Opis algorytmu:
# Na początku przechodzimy przez tablicę i odwracamy słowa jeżeli ostatni znak ma większą wartość w kodzie ASCII od pierwszego znaku.
# Dzięki temu pozbędziemy sie rewersów słów tzn. słowa typu "tok", zostną zamienione na "kot" itd. Teraz pozostaje nam posortować
# alfabetycznie nasze słowa (w tym rozwiązaniu korzystamy z radix sorta o złożoności O(N)) oraz wyznaczyć siłę najsilniejszego 
# z tych słów.

from kol1atesty import runtests

def char2index(char):
    return ord(char) - ord("a")

def g(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    print(f"\ndługość tablicy: {n}\n")

    ####################################################################
    # Pozbywamy się rewersów oraz wyznaczmy długość najdłuższego słowa #
    ####################################################################
    
    maxLen = 0

    for i in range(n):
        if ord(T[i][0]) > ord(T[i][-1]):
            T[i] = T[i][::-1]
        #end if
        if len(T[i]) > maxLen:
            maxLen = len(T[i])
        #end if
    #end for

    ###############################
    # sortujemy słowa po długości #
    ###############################
    
    wordsLenCnt = [0 for _ in range(maxLen)]

    for i in range(n):
        wordsLenCnt[len(T[i]) - 1] += 1
    #end for
    
    wordsLenRadixCnt = [wordsLenCnt[i] for i in range(maxLen)]

    i = 1
    j = maxLen - 2
    while i < maxLen:
        wordsLenCnt[i] += wordsLenCnt[i - 1]
        wordsLenRadixCnt[j] += wordsLenRadixCnt[j + 1]
        i += 1
        j -= 1
    #end while

    sortedWords = [None]*n

    for i in range(n - 1, - 1, -1):
        currentLen = len(T[i])
        wordsLenCnt[currentLen - 1] -= 1
        sortedWords[wordsLenCnt[currentLen - 1]] = T[i]
    #end for
        
    for i in range(n):
        T[i] = sortedWords[i]
    #end for
        
    #################################
    # sortujemy słowa alfabetycznie #
    #################################
        
    for letterIndex in range(maxLen - 1, -1, -1):
        lettersCnt = [0]*26
        numberOfWordsWithEnoughLetters = wordsLenRadixCnt[letterIndex]

        for i in range(numberOfWordsWithEnoughLetters):
            lettersCnt[char2index(T[n - numberOfWordsWithEnoughLetters + i][letterIndex])] += 1
        #end for
            
        for i in range(1, 26):
            lettersCnt[i] += lettersCnt[i - 1]
        #end for
            
        for i in range(numberOfWordsWithEnoughLetters - 1, -1, -1):
            currentWord = T[n - numberOfWordsWithEnoughLetters + i]
            lettersCnt[char2index(currentWord[letterIndex])] -= 1
            sortedWords[n - numberOfWordsWithEnoughLetters + lettersCnt[char2index(currentWord[letterIndex])]] = currentWord
        #end for
            
        for i in range(numberOfWordsWithEnoughLetters):
            T[n - numberOfWordsWithEnoughLetters + i] = sortedWords[n - numberOfWordsWithEnoughLetters + i]
        #end for
    #end for
            
    ##############################
    # znajdujemy maksymalną siłę #
    ##############################
        
    maxStrength = 1
    currentStrength = 1

    for i in range(1, n):
        if T[i] == T[i - 1]:
            currentStrength += 1
            maxStrength = max(maxStrength, currentStrength)
        else:
            currentStrength = 1
        #end if
    #end for
        
    return maxStrength


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
