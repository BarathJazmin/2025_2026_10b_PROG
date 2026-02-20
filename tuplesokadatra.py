


def listaFeltoltes():
    db = int(input())
    lista = []
    for i in range(0,db,1):
        sor = input()
        st = sor.split(' ')
        tupe = (st[0],int(st[1]),int(st[2]))
        lista.append(tupe)
    return lista



def main():
    adatok = listaFeltoltes()
    print(adatok)
    adat = adatok[2]
    print(adat[0])

main()