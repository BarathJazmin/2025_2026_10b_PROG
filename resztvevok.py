
def adatokFeltoltese():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(";")
        lista.append((st[0], st[1], st[2], int(st[3]), st[4]))
    return lista


def kereses(adatok, datum):
    i = 0
    while(i<len(adatok) and not (adatok[i][0]))


def main():
    adatok = adatokFeltoltese()
    print(adatok)

    # 5. feladat
    datum = input("Adjon meg egy dátumot: ")
    index = kereses(adatok, datum)

main()
