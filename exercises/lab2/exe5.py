# czy istnieje liczba "x" tzw. lider w tablicy, który wystepuje na ponad połowie pozycji w tablicy

def lider(tab: list):
    lider = tab[0]
    cnt = 0
    liderExists = False
    for ele in tab:
        if ele == lider:
            cnt += 1
            liderExists = True
        else:
            cnt -= 1
            if cnt == 0:
                lider = ele
                liderExists = False
                cnt = 1
            #end if
        #end if
    #end for
                
    return lider, liderExists

if __name__ == "__main__":
    tab = [1,1,1,1,1,1,2,3,4,5,6]
    print(lider(tab))

    tab = [1,2,3,4,5,6]
    print(lider(tab))

    tab = [1,2,1,3,1,1]
    print(lider(tab))
