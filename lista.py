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