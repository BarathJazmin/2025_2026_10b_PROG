
def fajlbeolvasas():
    fajl = open("resztvevok.txt","r", encoding = "utf-8")
    elso = fajl.readline()
    sorok = fajl.readlines()

    lista = []
    for sor in sorok:
        st = sor.strip().split(";")
        lista.append((st[0], st[1], st[2], int(st[3]), st[4]))
    fajl.close()
    return lista[0], elso

def main():
    adatok = fajlbeolvasas()
    print(adatok)
    lista = adatok[0]
    elso = adatok[1]


main()