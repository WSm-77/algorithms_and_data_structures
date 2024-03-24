# Dana jest tablica A zawierająca n parami różnyc liczb. Proszę zaproponować algorytm, który znajduje takie dwie 
# liczby x i y z A, że y - x jest jak największa oraz w tablicy nie ma żadnje liczby z takiej, że, x<z<y (innymi słoway, 
# po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i + 1] dla których A[i + 1] - A[i] jest największe). 

# najpierw znajdujemy minimum i maksimum, następnie tworzymy n kubełków każdy szerokości (max - min)/n, przechodzimy przez tablicę
# i wrzucamy te liczby do kubełków (w tych kubełkach utrzymujemy minimum i maksimum). Teraz mamy dwa przypadki:
# 1. w każdym kubełku jest po jednym elemencie, wtedy liczby są posortowane, więc przechodzimy przez tablicę i znajdujemy szukaną różnicę
# 2. jeżeli jakiś kubełek jest pusty to znajdujemy różnicę pomiędzy maksimum z jednego kubełka z minmum z innego kubełka

from random import randint

class Bucket:
    def __init__(self) -> None:
        self.maxVal = -float("inf")
        self.minVal = float("inf")

    def add(self, val):
        if val > self.maxVal:
            self.maxVal = val

        if val < self.minVal:
            self.minVal = val

        

def val_to_bucket_index(val, minVal, maxVal, tabSize):
    return ((val - minVal)*tabSize) // (maxVal - minVal)

def find_min_max(tab):
    n = len(tab)

    minVal = float("inf")    
    maxVal = -float("inf")    

    for i in range(1, n, 2):
        if tab[i] > tab[i - 1]:
            if tab[i] > maxVal:
                maxVal = tab[i]
            
            if tab[i - 1] < minVal:
                minVal = tab[i - 1]
        else:
            if tab[i] < minVal:
                minVal = tab[i]

            if tab[i - 1] > maxVal:
                maxVal = tab[i - 1]
        #end if
    #end for
                
    if n % 2 == 1:
        if tab[n - 1] > maxVal:
            maxVal = tab[n - 1]
        else:
            if tab[n - 1] < minVal:
                minVal = tab[n - 1]
        #en dif
    #end if
                
    return minVal, maxVal

def find_max_difference(tab):
    n = len(tab)

    minVal, maxVal = find_min_max(tab)
                
    buckets: list[Bucket] = [Bucket() for _ in range(n+1)]

    for ele in tab:
        backetIndex = val_to_bucket_index(ele, minVal, maxVal, n)
        buckets[backetIndex].add(ele)
    #end for
        
    bucketIndex = 0

    while bucketIndex < n + 1 and buckets[bucketIndex].maxVal == -float("inf"):
        bucketIndex += 1
    #end while
    
    maxDifference = 0
    prevMax = buckets[bucketIndex].maxVal

    while bucketIndex < n + 1:
        while bucketIndex < n + 1 and buckets[bucketIndex].maxVal == -float("inf"):
            bucketIndex += 1
        #end while
        currentDifference = buckets[bucketIndex].minVal - prevMax
        maxDifference = max(maxDifference, currentDifference)
        prevMax = buckets[bucketIndex].maxVal
        bucketIndex += 1
    #end while
        
    return maxDifference
        

if __name__ == "__main__":
    print("test1\n")
    testTab = [4, 2, 3, 7, 8, 9, 1, 13]
    print(testTab)
    print(sorted(testTab))
    print(find_max_difference(testTab))

    print("\ntest2\n")
    testTab = [randint(1, 30) for _ in range(randint(5, 10))]
    print(testTab)
    print(sorted(testTab))
    print(find_max_difference(testTab))
