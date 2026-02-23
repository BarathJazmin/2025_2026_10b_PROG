# szeleromu.txt
# település, vármegye, tájolás, hány darab szélerőmű, szélerőművenkénti teljesítmény kw/h, mikor telepítették
# Magyarországon hány szélerőmű van?
# Írjuk ki hogy melyik településen, és mikor alapították...


def adatokBeolvasasa():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(';')
        lista.append(st[0],st[1],st[2],int(st[3]),int(st[4]),int(st[5]))
    return lista




def main():
    t = adatokBeolvasasa()
    print(t)


main()