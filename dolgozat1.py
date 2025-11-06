import random
import math

# 1. feladat

szerencse = random.randint(0,9)
if(szerencse == 1 or szerencse == 6):
    print("labda")
elif(szerencse == 2 or szerencse == 7)
    print("ceruza")
elif(szerencse == 3 or szerencse == 8)
    print("színes papír")
elif(szerencse == 4 or szerencse == 9)
    print("bicikli")
else:
    print("nem nyert")


# 2. feladat
# 891 óra

ora = int(input("Adja meg a tenger alatt tötött időt, órában: "))
het = ora // 168
nap = (ora - het *168) // 24
ora2 = (ora - het * 168) - nap * 24
print("Átszámolva:"het,"hét", nap,"nap",ora2,"óra")

# 3. feladat

szam = radom.randint(100,999)
print("Generált háromjegyű szám:", szam )
elso = szam // 100
masodik = (szam - elso * 100) // 10
harmadik = szam % 10
if(elso ** 3 + masodik ** 3 + harmadik ** 3 == szam) : 
    print("A szám Armstrong szám")
else:
    print("A szám nem Armstrong szám")


# 4. feladat

a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)
print("Véletlen számok:",a,b,c)
if(a != 0 and b != 0 and c != 0):
    harmonk = 3 / (1/a + 1/b + 1/c)
elif( a == 0 and b != 0 and c != 0):
    harmadik = 3 / (1/a + 1/b + 1/c)
elif( a == 0 and b != 0 and c != 0):
    harmadik = 3 / (1/a + 1/b + 1/c)
elif( a == 0 and b != 0 and c != 0):
    harmadik = 3 / (1/a + 1/b + 1/b)
elif( a == 0 and b != 0 and c != 0):
    harmadik = 3 / (1/a + 1/b + 1/a)
else:
    print("nincs megoldás")
print("Harmonikus közép:", round(harmonk,3))


