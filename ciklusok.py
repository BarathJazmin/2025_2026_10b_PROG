import random as r
"""
# Ciklusok - ismétlés - Loop

Számlálós - For ciklus
- végig mecs a megadott elemeken vagy intervallumon!

for elem in range(mettől, meddig, hányasával) :
    Ismétlendő folyamat

for karakter in szoveg:
    Ismétlendő folyamat
Tesztelős - While
"""

for elem in range(11,13,1):
    print(elem)

# első tíz darab páros szám

for elem in (0,19,2) :
    print(elem)



# szöveg betűi közé vesszőt
szoveg = "kalapács"
print(szoveg)
for karakter in szoveg :
    print(karakter)

for karakter in szoveg:
    print(karakter,end=",")

# szoveg[0]
# szoveg[1]
# szoveg[2]
for index in range(len(szoveg)-1,1):
    print(szoveg[index]+",",end="")
#print(szoveg[len(szoveg)-1])
print(szoveg[-5])

# 4-gyel egyen osztható 30-50-ig 

for elem in range (32,50,4):
    print(elem,end=" ")
print()

# 10-tol 1-ig visszafele a szamokat!

for b in range(10,1,-1):
    print(b, end=" ")
print()

# visszafele a kalapács szót írassam ki!

for index in range(len(szoveg)-1, -1, -1):
    print(szoveg[index],end=" ")
print()

# írassa ki a szöveget a helyével társítva!
# BE : kalapács
#Ki : 1k 2a 3l 4a 5p 6á 7c 8s

for index in range(0, len(szoveg), 1):
    print(str(index+1)+szoveg[index], end =" ")
print()

# írasson ki 5db véletlen karaktert a szövegből!

for db in range(0,5,1):
    szam = r.randint(0,3)
    print(szoveg[szam],end =" ")
print()





