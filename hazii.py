import random

#Jancsi és Juliska elmennek mindennap gombát gyűjtenek. 14napig folyamatosan gyűjtik majd összevetik az adatokat. Szimuláld a gyűjtést. Kosarak nagysága [2,9] közötti
#    lebegőpontos( tört szám, 2 tizedes jegy pontossággal.) Mindkettőjük adatát külön listában tárod!
#    Van -e bármelyiköjüknél 8.5 kg-nál több ? Ha igen kinél?
#    Van-e olyan közöttük, aki 4.9 -5.1 közötti kosarat gyűjtött!
#    Max,min,átlag,db(2.1-2.4)között?





def listaFeltolt(n):
    lista = []
    for i in range(0,n,1):
        lista.append(random.randint(200,900)/100)
    return lista

def vaneSzamnalNagyobb(szam, lista):
    index = 0
    listaFeltolt(14)
    while(index < len(lista) and lista[index] <= szam):  
        index += 1
    vane = index < len(lista)            
    return vane

def vaneKetszamKozott(a,b,lista):
    index = 0
    listaFeltolt(14)
    while(index < len(lista) and (lista[index] < a or lista[index] < b)):
        index += 1
    vane = index < len(lista)            
    return vane




def main():
    jancsi = []
    juliska = []
    
    # listaFeltolt(14)
    # print(listaFeltolt(14))

    juliska = listaFeltolt(14)
    jancsi = listaFeltolt(14)
    print("Juliska", juliska)
    print("Jancsi", jancsi)

    vaneJuliska = vaneSzamnalNagyobb(8.5,juliska)
    if(vaneJuliska):
        print("Van Juliskánál 8.5-nél nagyobb")
    else:
        print("Nincs Juliskánál 8.5-nél nagyobb")

    vaneJancsi = vaneSzamnalNagyobb(8.5,jancsi)
    if(vaneJuliska):
        print("Van Jancsinál 8.5-nél nagyobb")
    else:
        print("Nincs Jancsinál 8.5-nél nagyobb")

    vaneJuliskaKozott = vaneKetszamKozott(4.9, 5.1, juliska)
    if(vaneJuliskaKozott):
        print("Juliskának van 4.9 és 5.1 közötti értéke")
    else:
        ("Juliskának nincs 4.9 és 5.1 közötti értéke")

    vaneJancsiKozott = vaneKetszamKozott(4.9, 5.1, jancsi)
    if(vaneJancsiKozott):
        print("Jancsinak van 4.9 és 5.1 közötti értéke")
    else:
        ("Jancsinak nincs 4.9 és 5.1 közötti értéke")



main()