#1.,  Írjon egy függvényt, ami bekér  a felhasználótól egy számot, [10,20] között úgy, hogyha rossz értéket adott meg ismételje meg a bekérést! Adja vissza a helyes értéket!
# 2., Írjon egy függvényt, ami visszaad egy listát. A korábban bekért szám legyen a darbszám. A számok pedig 2 jegyű, de 4-gyel nem osztható számok!
# 3., Írjon egy függvényt, ami visszaadja a listából az első 7-re végződő szám indexét, ha ilyen!

import random 

def szamBekerese():
    szam = int(input("Adjon meg egy számot [10-20] között: "))
    while(szam < 10 or szam > 20):
        print("Hibásan adta meg a számot!")
        szam = int(input("Adjon meg egy számot [10,20] között: "))
    return szam



def listaFeltolt(n):
    lista = []
    for i in range(0,n,1):
        szam = random.randint(10,99)
        lista.append(szam)
    return lista


def kereses(lista):
    while(i < len(lista) and lista[i] % 10 != 7):
        i += 1
    vane = i < len(lista)
    if(vane): return i
    else:
        return -1
    






def main():
    db = szamBekerese()
    szamokLista = listaFeltolt(db)
    print(szamokLista)

    index = kereses(lista)
    if(index == -1):
        print("Nincs a listában 7-tel osztható elem ")
    else: 
        print("Van a listában 7-tel osztható elem, az", index+1, "helyen")




main()



# HF :

# 1., Készíts egy listát ami feltölti a francia kartya lapjaival! T - treff, K - Káró, S - Szív, P - pikk Tehát T1, T2, ..., K13, P1,P2,  ..., P13,S1,S2, ...,S13
# 2., Írjon egy függvényt, ami megkeveri  paklit (véletlen hely iválasztásával)
# index1, index2 cseréje
# segéd = index1
# index1 = index 2
# index2 = segéd
# 3., Írjon egy paraméteres függvényt, ami megadja, hogy hányadik helyen szerepel a paraméterenmegadott lap !
# 4., 
