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


def main():
    lista1 = veletlenlista(13)
    print(lista1)
    lista2 = veletlenlista(5)
    print(lista2)

    negativ00ravegzodo(lista1)

main()




   

        

