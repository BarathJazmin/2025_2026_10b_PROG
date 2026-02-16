import math

def prime(szam):
    a = 2
    while(a < szam/2 and szam % a != 0):
        a += 1
    return a >= math.sqrt(szam)

def LNKO(szam1, szam2):
    kisebb = szam1
    if(szam1 > szam2):
        kisebb = szam2
    while(kisebb >= 1 and not (szam1 % kisebb == 0 and szam2 % kisebb == 0 )):
        kisebb -= 1
    return kisebb

def LNKO(a,b):
    if a == b:
        return a
    if b < a:
        c = a
        a = b
        b = c
    while(0 < a):
        a, b = b % a, a
    return b

def main():
    a = 13
    b = 26 
    print(prime(a))
    print(LNKO(a,b))

    

main()