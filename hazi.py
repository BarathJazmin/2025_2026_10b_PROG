import math 
import random 

# Számtani átlag :

szamok = [4,6,8,10]
osszeg = 0

for i in szamok:
    osszeg = osszeg + i      # Az aktualis számot hozzáadjuk az összeghez.
print(osszeg / len(szamok))   # len => hány szám van 



# Mértani átlag : 
# olyan átlag, amikor összeszorozzuk a számokat majd gyököt vonunk belőlük

szamok = [2,8]
szorzat = 1
for i in szamok:
    szorzat = szorzat * i
print(szorzat **(1 /len(szamok)))   # négyzetgyökvonás, és megszámoljuk a lennel a számok összegét


# 30db 13,17- re végzödő számokkal, hány 13-mal és 17-tel osztható van :

n = 30

lista = []
for i in range(0,n,1):
    a = random.randint(1000,9999)
    veletlen = random.randint(1,3)
    if veletlen == 1:
        lista.append(a * 10 + 13)
    else:
        lista.append(a * 10 + 17)

oszthato13 = 0
oszthato17 = 0

for szam in lista:
    if szam % 13 == 0:
        print("osztahtó 13-mal",szam)
        oszthato13 += 1
    if szam % 17 == 0:
        print("osztható 17-tel",szam)
        oszthato17 += 1
print("Lista",lista)
print("13-mal osztható",oszthato13)
print("17-tel osztható",oszthato17)

# Bekérünk egy hosszabb szöveget,és hány darab  felhasználó által megadott betű van benne :

szoveg = input("Adj meg egy szöveget:")
betu = input("Adj meg egy betüt:")

db = 0
for karakter in szoveg :
    if karakter == betu :
        db += 1
print("Ennyi darab van belőle",db)


# Kettő tizedes jegyre való kerekítés => print(round(atlag,2))

dba = 
for index in range(0,n,1):
    if(atlag>lista[index]):
        dba += 1

szorzat = 1
for elem in lista:
    szorzat *= elem 
matlag = math.pow(szorzat,1/n)

mossz = 0
for i in lista:
    if(matlag > a):
        mossz += a
print("Mértani számok alatti számok összege",mossz)

szo1 = "alma"
szo2 = "alkat"
kulonbseg = 0
minimumhossz = 0
if(len(szo1)>len(szo2)):
    minimumhossz = len(szo2)
else:
    minimumhossz = len(szo1)
for i in range(0,minimumhossz,1):
    if(szo1[i] != szo2[i]):
        kulonbseg += 1
print(kulonbseg+)


