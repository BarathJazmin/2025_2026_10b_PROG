import random

# Generáljon egy listában 13db olyan számokat amik 3-ra 5-re és 7-re végződnek.
# Hány darab 3-ra, 5-re, és 7-re végződő szám van?

n = 13

lista = []
for i in range(0,n,1):
    a = random.randint(1000,9999)
    veletlen = random.randint(1,3)
    if(veletlen == 1):
        lista.append(a*10+3)
    elif(veletlen == 2):
        lista.append(a*10+5)
    else:
        lista.append(a*10+7)
    
print(lista)

haromra = 0
for i in range(0,len(lista),1):
    if(lista[i] % 10 == 3):
        haromra += 1
    elif(lista[i] % 10 == 5):
        otre += 1
    else:
        hetre += 1
print("Háromra végződő", haromra)
print("Ötre végződő", otre)
print("Hétre végződő", hetre)








