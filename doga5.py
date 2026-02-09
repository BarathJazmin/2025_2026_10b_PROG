# Shrek és Fióna kiruccannak a Kacifánt Kaszinóba kockázni. Két darab 18 oldalú kockával 
# dobnak, ahol a számok 1-18ig vannak. A játékosok egymás után dobják a két kockát egyszerre
# és felírják a saját lapjukra egymás után a kidobott értékek összegét. A játék 7 körös és utána 
# derül ki, hogy ki nyert vagy esetleg a játék eredménye döntetlen. Fióna kezdi mindig a játékot.
# A nyertes a 7 kör kidobott összege alapján dől el.


# 1. Írjon egy függvényt, ami visszatér egy olyan listával, ami paraméterként megkap egy 
# darabszámot és a feladatban leírtak alapján kigenerál annyi véletlen számot! Majd 
# hozzon létre két listát felhasználva a függvényt a feladatban megadott darabszámmal! 
# Ha nem sikerült megírnia a függvényt, akkor használja a következő két listát:
# Shrek: [31,20,12,22,34,4,7]
# Fióna: [9,19,2,2,22,14,6]

import random


def listaFeltolt(db):
    lista = []
    for i in range(0,db,1):
        szam = random.randint(2,36)
        lista.append(szam)
    return lista





# 2. Írjon egy függvényt, ami megadja egy lista elemeinek összegét! (összegzés tétele)

def osszegzes(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    return osszeg


#  3. Írjon egy eljárást, ami a mintának megfelelően kiíratja egy lista elemeit és összegét. A 
# folyamatnak függenie kell egy listától és a lista összegétől!   

def kiiratas(lista, osszeg):
    for i in range(0, len(lista),1):
        print(lista[i], end =" + ")
    print(lista[len(lista),-1], end =" ")
    print("=", osszeg)




# 4. Írjon egy függvényt, ami megadja, hogy a játékot ki nyert! Shrek, Fióna vagy Döntetlen 
# lehet a kimenetel! Írassa ki a mintának megfelelően!


def kinyert(slista,flista):
    if(slista > flista):
        return "Shrek nyert"




# 5. Írjon egy függvényt, ami megadja, hogy volt-e olyan kör, amikor mindkét játékos ugyan 
# azt a számot dobta! Mindkét játékos dobására szükség van a függvényben! A mintának 
# megfelelően írja ki az eredményt!

def volteEgyezoKor(slista,flista):
    i = 0
    while(i < len(lista) and slista[i] != flista[i]):


def main():
    shrek = listaFeltolt(7)
    fiona = listaFeltolt(7)
    print(shrek)
    print(fiona)
    
    shrekOsszeg = osszegzes(shrek)
    fionaOsszeg = osszegzes(fiona)
    print(shrekOsszeg)
    print(fionaOsszeg)
    kiirata(shrek,shrekOsszeg)
    kiiratas(fiona,fionaOsszeg)
    if(volteEgyezoKor(shrek,fiona)):
        print("Volt egyezés")
    else:
        print("Nem volt egyezés")





main()