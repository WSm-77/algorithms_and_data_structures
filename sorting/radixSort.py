# check offline/offline3/6.py for improved version of radix sort (sorts words with different length)

def char2index(char):
    return ord(char) - ord("a")

def radix_sort(words: list[str]):
    n = len(words)
    wordLen = len(words[0])

    for letterIndex in range(wordLen - 1, -1, -1):

        # we consider only latin alphabet
        letterCnt = [0]*26
        sortedWords = [None]*n

        for wordIndex in range(n):
            letterCnt[char2index(words[wordIndex][letterIndex])] += 1
        #end for
        for i in range(1, 26):
            letterCnt[i] += letterCnt[i - 1]
        #end for
        for wordIndex in range(n - 1, -1, -1):
            currentWord = words[wordIndex]
            charIndex = char2index(currentWord[letterIndex])
            letterCnt[charIndex] -= 1
            sortedWords[letterCnt[charIndex]] = currentWord
        #end for

        words = sortedWords
    #end for
            
    return words




if __name__ == "__main__":
    testWords = ["kra", "art", "kot", "kit", "ati", "kil", "ala", "kac", "koc", "kis", "aka"]
    print(testWords)
    testWords = radix_sort(testWords)
    print(testWords)
