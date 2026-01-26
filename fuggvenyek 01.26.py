# Eldöntés tétele:

def vaneKetjegyuListaban(lista):
    i = 0
    while (i < len(lista) and not (lista[i] >= 10 and lista[i] <= 99)):
        i += 1
    vane = i < len(lista)
    return vane



def main():
    szamok = [2,5,6,3,7,11,9,1,1]
    print(szamok)
    # van -e kétjegyű szám a listában?
    vaneKetjegyu = vaneKetjegyuListaban(szamok)
    print(vaneKetjegyu)

main()




# HF:      Jancsi és Juliska elmennek mindennap gombát gyűjtenek. 14napig folyamatosan gyűjtik majd összevetik az adatokat. Szimuláld a gyűjtést. Kosarak nagysága [2,9] közötti
#          lebegőpontos( tört szám, 2 tizedes jegy pontossággal.) Mindkettőjük adatát külön listában tárod!
#          Van -e bármelyiköjüknél 8.5 kg-nál több ? Ha igen kinél?
#          Van-e olyan közöttük, aki 4.9 -5.1 közötti kosarat gyűjtött!
#          Max,min,átlag,db(2.1-2.4)között?