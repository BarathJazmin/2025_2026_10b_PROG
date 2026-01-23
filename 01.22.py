# [-950,950] közötti x50-re és x00-ra végződő számok!
# [-19,19]*50
# Adja meg hány darab negatív x00-ra végződő szám van!


# eljárás - visszatérés nélküli függvény - olyan függvény, aminek nincs visszatérési értéke

import random


def veletlenlista(n):

    lista = []

    for i in range(0,n,1):
        negative = random.randint(0,1)
        vszam = random.randint(2,19)*50
        if(negative == 0):
            lista.append(-1*vszam)
        else:
            lista.append(vszam)
    return lista


def negativ00raVegzodo(barmilyenLista):
    db = 0
    for i in range(0,len(barmilyenLista),1):
        if(barmilyenLista[i] % 100 == 0):
            db += 1
    return db 




#Házifeladat:

def listaAtlaga(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    atlag = osszeg / len(lista)
    return atlag



# masodik feladat

def pozitivSzamokAtlaga(lista):
    db = 0
    osszeg = 0
    for elem in lista:       # Végig megyünk a lista összes elemén
        if elem > 0 :         # Ha pozitiv az aktuális szám,akkor
            db += 1              # a db változót növeljük 1-gyel
        osszeg += elem
    atlag = osszeg / db
    return atlag


def maximumIndex(lista):
    maxi = 0
    for i in range(1,len(lista),1):
        if (lista[i] > lista[maxi]):
            maxi = i
    return maxi


# Írjon függvényt ami viszaadja a listánk terjeelmét. Terjedelem = maximum-minimum

def terjedelem(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if (lista[i] > maxe):
            maxe = lista[i]
        if(lista[i] < mine):
            mine = lista[i]
terjedelem = maxe - mine
return terjedelem










def main():
    lista1 = veletlenlista(13)
    print(lista1)
    lista2 = veletlenlista(5)
    print(lista2)

    print(negativ00-raVegzododo(lista1))

    
    listaatlaga = listaAtlag(lista1)
    print("az elso lista atlaga: ", listaatlaga)
    print("a masodik lista átlaga. " , listaAtlaga(lista2))

    print("Az első lista pozitív számainak átlaga: ", pozitivSzamokAtlaga(lista1))
    print("Az második lista pozitív számainak átlaga: ", pozitivSzamokAtlaga(lista2))

    maxIndexLista1 = maximumIndex(lista1)
    print("Első lista legnagyobb elem helye:", maxIndexLista1+1)




main()
