import random

"""
Függvények
(scratch blokk)

Előre definiált,megírt,megfogalmazott folyamatok,amik külső értéktől függően végrehajtják a belső utasításokat!

def fuggvenyNev:
    #Fügvény tartalma

fuggvenyNev():
    # Függvény meghívása
"""

# Visszatérési érték nélküli függvények - eljárás
# Általában kiírás során használjuk.
# Összeadás függvény definiálása:

def osszeadas():
    a = 12
    b = 17
    print(a+b)

# Összeadás külső értékektől függően PARAMÉTEREN keresztül
def osszeadasParam(a,b):
    c = a + b
    print(c)

# Összeadás függvény meghívása:

osszeadas()
osszeadasParam(12,17)


# Visszatéréssel rendelkező függvények
def kettoAtizediken():
    a = 2**10                        # => a = math.pow(2,10)
    return a 

valtozo = kettoAtizediken()
print(valtozo)

def osszeadasVisszateressel(a,b):
    c = a + b
    return c

print(osszeadasVisszateressel(13,17))
print(osszeadasVisszateressel(11,10))



# Definálj egy olyan eljárást(nem tér vissza értékkel), aminek a paraméterében bekerül egy darabszám, és a függvény kiír ennyi darab véletlen számot egymás mellé!


def veletlenszamKiiratas(db):
    for i in range(0,db,1):
        print(random.randint(100,999),end=" ")

veletlenszamKiiratas(5)

# Készítsen egy eljárást, ami függ egy szövegtől, és kiírja a szót visszafele!

def szovegVisszafele(szoveg):
    for index in range(len(szoveg)-1,-1,-1):
        print(szoveg[index],end="")
    print()

szovegVisszafele("kalapács")


# Készítsen egy függvényt, ami függ a szövegtől, és visszaadjaa szót visszafele!

def szovegVisszafeleFv(szoveg):
    visszaSzoveg = ""
    for index in range(len(szoveg)-1,-1,-1):
        visszaSzoveg += szoveg[index]
    return visszaSzoveg

print(szovegVisszafeleFv("kalapács"))


# Írjon egy függvényt, ami egy szóról eldönti, hogy palindrom-e és visszaadja válaszul?(Visszafele ugyanaz)!

def palindromszoveg(palszoveg):
    if(palszoveg == szovegVisszafeleFv(palszoveg)):
        return True
    else:
        return False

print(palindromszoveg("abba"))


    








