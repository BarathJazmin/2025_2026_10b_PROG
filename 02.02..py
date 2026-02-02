# HF :

# 1., Készíts egy listát ami feltölti a francia kartya lapjaival! T - treff, K - Káró, S - Szív, P - pikk Tehát T1, T2, ..., K13, P1,P2,  ..., P13,S1,S2, ...,S13
# 2., Írjon egy függvényt, ami megkeveri  paklit (véletlen hely iválasztásával)
# index1, index2 cseréje
# segéd = index1
# index1 = index 2
# index2 = segéd
# 3., Írjon egy paraméteres függvényt, ami megadja, hogy hányadik helyen szerepel a paraméterenmegadott lap !
# 4.,  Kérjen be a felhasunálótól egy lap értéket, és adja meg hányadik helyen van.
# Írassa ki a megkevert paklit az ellenőrzéshez!


def kartyaGeneralas():
    lista = []
    for i in range(1,14,1):
        lista.append("T"+str(i))
        lista.append("P"+str(i))
        lista.append("K"+str(i))
        lista.append("S"+str(i))
    return lista







def main():
    kartyak = kartyaGeneralas



main()