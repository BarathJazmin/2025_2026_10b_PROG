import random

#szám kitalálós játék:

gondoltszam = random.randint(10,99)

print("Melyik kétjegyű számra gondoltam?")

while(szam != gondoltszam):
    if(szam > gondoltszam):
        print("A szám nagyobb mint a gondolt szam!")
        elif(szam < gondoltszam):
        print("A szám kisebb mint a gondolt szam!")
    else:
            print("Eltaláltad!")
         szam = int(input("Próbálkozz még egyszer: "))
        probalkozasok += 1
    else: 
        print("Nem kétjegyű számot adott meg")
szam = int(input("Próbálkozz még egyszer"))





