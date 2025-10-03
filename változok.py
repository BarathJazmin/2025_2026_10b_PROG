# Változó deklarálása és incializálása
# Változó létrehozása és kezdőérték adása
# valtozoNev = "kezdoertek"
nev = "Baráth Jázmin"
osztaly = "10.b"
datum = "2025.09.08."
# "'"
# "'"
print(nev,"\n" osztaly,"\n" datum)

# operátor

# konkatenálás, concat összefűzés - két szöveget!!!!!
osszefuzes = nev+" bármi, akármi"+osztaly
print(osszefuzes)

# * töbszörözés
soknev = nev * 5
print(soknev)

"""
Típusok
- szöveg - string - strs
(- karakter)
- szám - egész (integer- int), lebegőpontis (tört) (float)
- logikai - true, false
"""

aEgesz = 123
bTort = 34.23
szSzam = "12"
logikai = true

print("a Egész:", aEgesz)
print("b Tört:", bTort)
print("sz Szam:", szSzam)
print("logikai:", logikai)

# Egesz operatorok
print("a + 2 =" aEgesz + 2)
print("a - 2 =" aEgesz - 2)
print("a + 2 =" aEgesz * 2)
print("a + 2 =" aEgesz / 2)

# DIV - egészrész, Mod - modulos(maradék)
# div - //
# mod - %

print("a div 8=", aEgesz // 8)
print("a mod 8", aEgesz % 8)

print(int(szSzam)+aEgesz)
print(szSzam+str(aEgesz))

print(aEgesz+SzSzam)
#\\ckik-pdc\kozos


