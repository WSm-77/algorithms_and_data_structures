# Jak posortować ciąg słów o różnych długościach w czasie proporcjonalnym do sumy długości tych słow?

def char2index(char):
    return ord(char) - ord('a')

def words_sort(words: list[str]):
    n = len(words)

    wordMaxLen = 0

    # najpierw musimy posortować słowa po ich długościach
    # przygotowujemy sobie też od razu tablicę zawierającą liczbę słów, które mają więcej niż (indeks w tablicy) - liczbę liter

    for word in words:
        wordLen = len(word)
        if wordLen > wordMaxLen:
            wordMaxLen = wordLen
        #end if
    #end for

    wordsLengthCnt = [0 for _ in range(wordMaxLen)]

    for word in words:
        wordsLengthCnt[len(word) - 1] += 1
    #end for
    
    letterIndexWordCnt = [wordsLengthCnt[i] for i in range(wordMaxLen)]
        
    i = 1
    j = wordMaxLen - 2
    while i < wordMaxLen:
        wordsLengthCnt[i] += wordsLengthCnt[i - 1]
        letterIndexWordCnt[j] += letterIndexWordCnt[j + 1]
        i += 1
        j -= 1
    #end for
        
    sortedWords = [None for _ in range(n)]

    for i in range(n - 1, -1, -1):
        currentWordIndex = len(words[i]) - 1
        wordsLengthCnt[currentWordIndex] -= 1
        sortedWords[wordsLengthCnt[currentWordIndex]] = words[i]
    #end for
    
    words = sortedWords

    # sortujemy wykorzystując radix sort, biorąc tylko te słowa, które mają na tyle liter aby je prównywać
    for letterIndex in range(wordMaxLen - 1 , -1, -1):
        lettersCnt = [0]*26
        wordsWithIlength = letterIndexWordCnt[letterIndex]
        sortedWords = [words[n - wordsWithIlength + i] for i in range(wordsWithIlength)]

        for i in range(wordsWithIlength):
            currentWord = words[n - wordsWithIlength + i]
            lettersCnt[char2index(currentWord[letterIndex])] += 1
        #end for
            
        for i in range(1, 26):
            lettersCnt[i] += lettersCnt[i - 1]
        #end for
            
        for i in range(wordsWithIlength - 1, -1, -1):
            currentWord = words[n - wordsWithIlength + i]
            charIndex = char2index(currentWord[letterIndex])
            lettersCnt[charIndex] -= 1
            sortedWords[lettersCnt[charIndex]] = currentWord
        #end for
        
        for i in range(wordsWithIlength):
            words[n - wordsWithIlength + i] = sortedWords[i]
        #end for
    #end for
            
    return words

        
if __name__ == "__main__":
    print("set1\n")
    wordsTab = ["kot", "jak", "owca", "kotlet", "kurczak", "pierogi", "kompot"]
    print(*words_sort(wordsTab), sep='\n')

    print("\nset2\n")
    english_words = [
        "apple", "banana", "orange", "grape", "kiwi", "strawberry", "blueberry", "pineapple", "watermelon", "peach",
        "pear", "plum", "cherry", "apricot", "mango", "lemon", "lime", "raspberry", "blackberry", "cranberry",
        "pomegranate", "fig", "nectarine", "avocado", "coconut", "papaya", "melon", "tangerine", "guava", "dragonfruit",
        "persimmon", "date", "lychee", "passionfruit", "cantaloupe", "nectar", "kiwifruit", "mandarin", "mulberry",
        "gooseberry", "apricot", "boysenberry", "honeydew", "elderberry", "grapefruit", "tamarind", "starfruit",
        "clementine", "durian", "acai", "kumquat", "rhubarb", "jackfruit", "quince", "pumpkin", "zucchini", "carrot",
        "potato", "tomato", "cucumber", "pepper", "onion", "garlic", "lettuce", "spinach", "broccoli", "cauliflower",
        "cabbage", "celery", "asparagus", "greenbean", "eggplant", "mushroom", "peas", "corn", "artichoke", "squash",
        "beetroot", "radish", "turnip", "kale", "sweetpotato", "raddicchio", "brusselsprout", "parsnip", "okra",
        "fennel", "leek", "rutabaga", "chard", "collardgreens", "endive", "watercress", "arugula", "bokchoy", "tatsoi",
        "basil", "thyme", "oregano", "rosemary", "sage", "parsley", "mint", "coriander", "cilantro", "dill", "chives", 
        "water"
    ]
    print(*words_sort(english_words), sep="\n")
