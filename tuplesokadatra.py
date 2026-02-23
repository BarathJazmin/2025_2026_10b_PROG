


def listaFeltoltes():
    db = int(input())
    lista = []
    for i in range(0,db,1):
        sor = input()
        st = sor.split(' ')
        tupe = (st[0],int(st[1]),int(st[2]))
        lista.append(tupe)
    return lista


# Írjon egy függvényt, ami visszaadja az öszetett szerkezetből, hogy összesen hány mázsa gyümölcs van!

def mazsaOsszegzese(adatok):
    osszeg = 0
    for i in range(0,len(adatok),1):
        osszeg += adatok[i][1]
    return osszeg


 # Írjon egy függvényt, ami visszaadja a paraméterben megadott értéktől nagyobb összeggel rendelkező gyümölcsök darabszámát!

def hanyArNagyobb(adatok,ar):
    db = 0
    for i in range(0,len(adatok),1):
        if(adatok[i][2]>ar):
            db += 1
    return db

def maxindexSuly(adatok):
    maxi = 0
    for i in range(len(adatok)):
        if(adatok[i][2]>adatok[maxi][2]):
            maxi = i
    return maxi

def gyumolcsKereses(adatok, gyumNev):
    i = 0
    while(i<len(adatok) and adatok[i][0] != gyumNev):
        i += i
    vane = i < len(adatok)
    if(vane):
        return i
    else:
        return -1






def main():
    adatok = listaFeltoltes()
    print(adatok)
    adat = adatok[2]
    print(adat[0])
    osszesen = mazsaOsszegzese(adatok)
    print(osszesen,"q gyümülcsünk van.")
    ar = 1000
    db = hanyArNagyobb(adatok, ar)
    print(db,"gyümölcs ára nagyobb,mint",ar)

    index = maxindexSuly(adatok)
    print("Legdrágább gyümölcs:",adatok[index][0])

    gyumNev = input("Adja meg a keresett gyümölcs nevét:")
    keresesindex = gyumolcsKereses(adatok, gyumNev)
    if(keresesidex < 0):
        print("Nincs ilyen gyümölcs a listában.")
    else:
        print(adatok[keresesindex][2],"q,",adatok[keresesindex][2],"Ft/kg")


main()