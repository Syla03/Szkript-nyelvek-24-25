#Bruttó és kor alapján
print("Jövedelem számítás\n")

brutto = int(input("Kérem a brutto jövedelmét: "))
kor = int(input("Kérem adja meg a korát: "))

#szja

if kor < 25:
    if brutto < 599790:
        szja = 0
    else:
        szja = (brutto - 599790) * 0.15
else:
    szja = brutto * 0.15

#nyugdíj
nyugdij = brutto * 0.1
tb = brutto * 0.07
munkanelkuli = brutto * 0.015
netto = brutto - szja - nyugdij - tb - munkanelkuli

print("Jövedelem".center(50))
print("")
print("Brutto:".ljust(25, "_"), str(int(brutto)).rjust(25, "_"),"Ft", sep="")
print("SZJA:".ljust(25, "_"), str(int(szja)).rjust(25, "_"), "Ft", sep="")
print("Nyugdíj:".ljust(25, "_"), str(int(nyugdij)).rjust(25, "_"), "Ft", sep="")
print("TB:".ljust(25, "_"), str(int(tb)).rjust(25, "_"), "Ft", sep="")
print("Munkanélküli:".ljust(25, "_"), str(int(munkanelkuli)).rjust(25, "_"), "Ft", sep="")
print("".rjust(50, "-"))
print("Nettó:".ljust(25, "_"), str(int(netto)).rjust(25, "_"), "Ft", sep="")

#feladat
print("Számológép")
muveletjel = input("Kérem adja meg a műveleti jelet(+,-,*,/): ")
szam1 =  int(input("Kérem adja meg az első számot: "))
szam2 =  int(input("Kérem adja meg az második számot: "))

if muveletjel not in ("+", "-", "*", "/"):
    print("Rossz műveletet adott meg")
    exit()
else:
    if muveletjel in ("+"):
        print("Eredmény: ", szam1, "+", szam2, "=", szam1 + szam2)
    elif muveletjel in ("-"):
        print("Eredmény: ",szam1, "-", szam2, "=", szam1 - szam2)
    elif muveletjel in("*"):
        print("Eredmény: ",szam1, "*", szam2,"=", szam1 * szam2 )
    elif muveletjel in ("/"):
        print("Eredmény: ", szam1, "/", szam2, "=", szam1 / szam2)
