def fajlbeolvasas():
    fajl = open("szeleromu.txt","r",encoding="utf-8")
    sorok = fajl.readlines()
    #print(sorok)
    t = []
    for sor in sorok:
        st = sor.strip().split(";")
        t.append((st[0], st[1], st[2], int(st[3]), int(st[4]), int(st[5])))
    fajl.close()
    return t

def osszes(adatok, ev):
    osszeg = 0
    for i in range(len(adatok)):
        if adatok[i][5] == ev:
            osszeg += adatok[i][3]
    return osszeg 



def main():
    adatok = fajlbeolvasas()

    ev =int(input("Adjon meg egy évet:"))
    print(ev)

    hanydb = osszes(adatok, ev)
    print(hanydb)


main()