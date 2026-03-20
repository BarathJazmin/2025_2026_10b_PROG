
def fajlbeolvasas():
    fajl = open("gyumolcsok.txt","r",encoding="utf-8")

    db = int(file.readline())
    print(db)

    t = []
    for i in range(db):
        sor = fajl.readline()
        sor2 = sor.strip().split(' ')
        t.append(((sor2[0]), int(sor2[1]), int(sor2[2])))


    fajl.close()
    return t




def main():
    fajlbeolvasas()


main()