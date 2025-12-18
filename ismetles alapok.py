"""
Utasítás (szekvencia)
-menj előre
-fordulj 
-szívd be a levegőt
-fújd ki a levegőt
- ...
- írasd ki - print()
- tárold el - változónév = érték
- számold ki - változónév = <képlet>
- kérd be - input("Add meg:")

Elágazás - (szelekció)
- ha piros a lámpa akkor megállok
- ha zöld a lámpa akkor elindulok
- ha fal van előttem elfordulok
- ha tudom hogy nem megy akkor gyakorolok 
- ...
- ha a bekért szám páros akkor kiíratom, hogy páros különben kiíratom, hogy páratlan
- ha a dobókocka értéke 5 akkor előre lépek 5-öt

Ismétlés - ciklus - (literáció)
- Addig menj, amíg a tábla van 
- Addig dobáld az aprót a gépbe, amíg el nem éred az összeget
- Üss vbele 3 tojást 
- Addig gyakorlok, amíg nem értem 
- Addig fog a tanár piszkálni, amíg nem látja, hogy értem

"""

db = 12
print("szám",db)
# a szám utolsó számjegye páros-e?
utolso_szamjegy = db % 10
print("utolsó számjegy:", utolso_szamjegy)

if(db % 2 == 0):
    print("páros")
else:
    print("páratlan")

# db-nyi almát szeretnék látni
for kiskutya in range(0,db,1):
    print(kiskutya+1,"Alma" ) 

# for karakter in szöveg:

db = 0
szoveg = "kalapács"
print(szoveg)
for karakter in szoveg:
    db+1
    print(db,karakter)