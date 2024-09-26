import Labor_04_modul
from Labor_04_modul import eredmenyek_megjelenitese

# főprogram
adatok = Labor_04_modul.adatok_bekerese()
print(adatok[0], adatok[1], adatok[2])
muvelet_eredmenye = Labor_04_modul.muveletek_vegrehajtasa(adatok[0], adatok[1], adatok[2])
print(muvelet_eredmenye)

eredmenyek_megjelenitese(adatok[0], adatok[1], adatok[2], muvelet_eredmenye)
szam1 = 4
print(szam1)