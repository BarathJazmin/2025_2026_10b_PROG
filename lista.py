import random
"""
lista - dinaamikus
    - tudunk bele új elemet rakni, ezzel nő az elemszáma
    - tudunk belőle törölni, ezzel csökken az elemsáma
    - lekérhető bármelyik eleme
    -módosítható bármelyik elem
deklarálás + inicializálás:
létrehozás + kezdőérték adás:
lista_neve =[]
új elem hozzáadása:
lista_neve.append(uj elem)
elem törlése:
lista_neve.remove(elem)
beégett lista:
lista_neve = [3,2,5,7,1]
lista hossza:
len(lista_neve)
"""
szamok = [3,2,5,7,1]
print(szamok)
print("első elem:", szamok[0])
print("lista hossza:",len(szamok))
print("utolsó elem:", szamok[len(szamok)-1])



# Töltsön fel egy 13 elemű listát [0,20] közötti véletlen számmal

#elemszam
n = 13

lista = []
for index in range(0,n,1) :
    a = random.randint(0,20)
    lista.append(a)

# Egy lépésben:
#lista.append(random.randint(0,20))

print(lista)

# Számok átlaga (összeadjuk a számokat és elosszuk az összeget a számok darabszámával)

for index in range(0,len(lista),1):
    osszeg += lista[index]
print(osszeg)
























# A szövegben van e sz betű?
szoveg ="poros"
dube = "ny"       #duplabetu
print(szoveg)
#if "sz" in szoveg:
#    print("van benne sz betű")
#else:
#    print("nincs benne sz betű")

index = 0 
while(index < len(szoveg)  and (szoveg[index] == dube[0] and szoveg[index+1] == dube[1])):
    index+1
if(index<len(szoveg)-1):
    print("Van benne" ,dube, "betű")
else:
    print("nincs bnne" ,dube,  "betű")

# palidrom -e?
ujszoveg = ""
for index in range(len(szoveg)-1, -1, -1):
    ujszoveg +=szoveg[index]
if(ujszoveg == szoveg):
    print("A szoveg palindrom")
else:
    print("A szoveg nem palidrom")

j = 0
while(j<len(szoveg)/2 and szoveg[j] == szoveg[len(szoveg)-1-j]):
    j+=1
if(j<len(szoveg)/2):
    print("A szoveg nem palidrom")
else: 
    print("A szoveg palindrom")