# Készítsen egy függvényt, ami db számtól függ, és visszaad egy feltöltött listát[-10,50]közötti számokkal!

import random

def listaFeltolt(db):
    lista = []
    for i in range(0,db,1):
        szam = random.randint(-10,50)
        lista.append(szam)
    return lista

lista = listaFeltolt(13)
print(lista)


# Készítsen egy függvényt, ami bármilyen lista elemeit megvizsgálva visszaadja, hogy hány db pozitív szám van!


def pozitivDB(szamokLista):
    darab = 0
    #ciklus i = 0- tól (n-1)-ig egyesével  


def main():          # => Fő eljárás
    #Lista feltöltés
    lista = listaFeltolt(13)
    print(lista)

main()




