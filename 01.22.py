# [-950,950] közötti 50-re és 00-ra végződő számok.
# [-19,19]*50


# eljárás - visszatérés nélküli függvény - olyan függvény, aminek nincs visszatérési értéke

import random

def veletlenlista():
    n = 13
    lista = []

    for i in range(0,n,1):
        negative = random.randint(0,1)
        vszam = random.randint(2,19)*50
        if(negative == 0):
            lista.append(-1*vszam)
        else:
            lista.append(vszam)
    print(lista)
veletlenlista()




   

        

