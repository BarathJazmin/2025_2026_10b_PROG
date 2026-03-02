
def listaFeltoltes():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(' ')
        lista.append((int(st[0]), int(st[1]), st[2], st[3], st[4]))
    return lista

def kereses(lista, vn, kn):
    i = 0
    while(i<len(lista) and not (lista[i][2] == vn and lista[i][3]==kn)):
        i += 1
    if(i<len(lista)):
        return i
    else:
        return -1


def feladat4(adatok):
    szavazatokSzama = osszesSzavazat(adatok)
    mindenki = 12345
    szazalek = szavazatokSzama / mindenki * 100
    print(f"A választáson {szavazatokSzama} állampolgár,  a jogosultak {round(szazalek,2)}%-a vett részt.")


def partDarab(part):
    db = 0
    for i in range(len(adatok)):
        if(adatok[i][4] == part):
            db += 1
    return db



def feladat5(adatok):
    gyep = partDarab("Gyep")
    hep = partDarab("HEP")
    tisz = partDarab("TISZ")
    zep = partDarab("ZEP")
    fugg = partDarab("-")
    print("Gyümölcsevők Pártja",gyep)
    print("Húsevők pártja",hep)
    print("Tejivók Szövetsége",tisz)
    print("Zöldségevők Pártja",zep)
    print("Független Párt",fugg)


def maximumSzavazatok(adatok):
    maxe = adatok[0][1]
    for i in range(len(adatok)):
        if(adatok[i][1]>maxe):
            maxe = adatok[i][1]
    return maxe


def feladat6(adatok):
    maxe = maximumSzavazatok(adatok)
    for i in range(len(adatok)):
        if(adatok[i][1] == maxe):
            print(f"{adatok[i][1]} {adatok[i][3]} - {adatok[i][4]}")

def main():
    adatok = listaFeltoltes()
    print(adatok)

    # 2.feladat
    print("A helyhatósági választáson",len(adatok),"képviselőjelölt indult.")

    # 3.feladat
    vezeteknev = input("Adja meg a vezetéknevet: ")
    keresztnev = input("Adja meg a keresztnevet: ")
    index = kereses(adatok,vezeteknev,keresztnev)
    if(index >=0 ):
        print(adatok[index][1])
    else:
        print("Ilyen nevű képviselő nincs")


    


    

main()