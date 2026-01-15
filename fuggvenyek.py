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



