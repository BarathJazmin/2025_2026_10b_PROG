# szeleromu.txt
# település, vármegye, tájolás, hány darab szélerőmű, szélerőművenkénti teljesítmény kw/h, mikor telepítették
# Magyarországon hány szélerőmű van?
# Írjuk ki hogy melyik településen, és mikor telepítették egyszerre a legtöbb szélerőművet?
# Kérjünk be egy település nevet, és nézzük meg hogy vane az adott helyen szélerőmű, ha nincs akkor azt írassa ki!


def adatokBeolvasasa():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(';')
        lista.append((st[0],st[1],st[2],int(st[3]), int(st[4]), int(st[5])))
    return lista



def szeleromuvekDarab(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i][3]
    return osszeg


def maximumIndexDb(lista):
    maxi = 0
    for i in range(0,len(lista),1):
        if(lista[i][3]>lista[maxi][3]):
            maxi = i
    return maxi


def vaneSzeleromuVarosban(lista,varos):
    i = 0
    while(i<len(lista) and lista[i][0] != varos):
        i += 1
    vane = i < len(lista)
    return vane



def main():
    t = adatokBeolvasasa()

    db = szeleromuvekDarab(t)
    print(db, "darab szélerőmű van Magyarországon")

    maxindex = maximumIndexDb(t)
    print( t[maxindex][0], "városban",t[maxindex][5], "évében csinálták egyszerre a legtöbb szélerőművet.")

    varos = input("Adjon meg egy várost:")
    vane = vaneSzeleromuVarosban(t,varos)
    if(vane):
        print("Ebben a városban van szélerőmű.")
    else:
        print("Ebben a városban nincs szélerőmű.")



main() 