import csv
import re
import unicodedata
from string import printable
import sys

NOPRINT_TRANS_TABLE = {
    i: None for i in range(0, sys.maxunicode + 1) if not chr(i).isprintable()
}


def puhdistus(string):
    _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
    string = _RE_COMBINE_WHITESPACE.sub(" ", string).strip()
    return string.translate(NOPRINT_TRANS_TABLE)

huoltsikat = ["NESTE", "ABC", "SHELL", "TEBOIL", "SEO"]
elektro = ["POWER ", "GIGANTTI"]
games = ["STEAM", "STEAMGAMES"]
ruokakauppa = ["SALE", "LIDL", "CITY", "PRISMA ", "MARKET"]
pikaruoka = ["MCD", "PIZZ", "GRILL", "BAARI", "RAVIN","BURGER"]
lainat = ["FI05", "FI27", "LEHTINEN","KORTTIYHT"]
tililista = []
paikkalista = []
kulutuslista = []
bensakulutus, elektrokulutus, pelikulutus, ruokakulutus, pikaruokakulutus, lainakulutus = 0,0,0,0,0,0



with open("/home/lehmik/Downloads/tilitapahtumat.csv", "r") as tiliote:
    for row in csv.reader(tiliote):
        paikka = str(puhdistus(row[2].upper()))
        tililista.append([row[1], paikka])

for r in tililista:
    if int(r[0]) < 0:
        if r[1] not in paikkalista:
            paikkalista.append(r[1])


for paikka in paikkalista:
    kulutus = 0
    for tilitapahtuma in tililista:
        if paikka in tilitapahtuma:
            kulutus = (kulutus + int(tilitapahtuma[0]))

    kulutuslista.append([puhdistus(paikka), kulutus])

for idx,row in enumerate(kulutuslista):

    for h in huoltsikat:
        if str(h).rstrip() in row[0]:
            bensakulutus = bensakulutus + int(row[1])
            kulutuslista.pop(idx)

for idx, row in enumerate(kulutuslista):
    for e in elektro:
        if str(e).rstrip() in row[0]:
            elektrokulutus = elektrokulutus + int(row[1])
            kulutuslista.pop(idx)

for idx, row in enumerate(kulutuslista):
    for g in games:
        if str(g).rstrip() in row[0]:
            pelikulutus = pelikulutus + int(row[1])
            kulutuslista.pop(idx)

for idx, row in enumerate(kulutuslista):
    for r in ruokakauppa:
        if str(r).rstrip() in row[0]:
            ruokakulutus = ruokakulutus + int(row[1])
            kulutuslista.pop(idx)

for idx, row in enumerate(kulutuslista):
    for p in pikaruoka:
        if str(p).rstrip() in row[0]:
            pikaruokakulutus = pikaruokakulutus + int(row[1])
            kulutuslista.pop(idx)

for idx, row in enumerate(kulutuslista):
    for l in lainat:
        if str(l).rstrip() in row[0]:
            lainakulutus = lainakulutus + int(row[1])
            kulutuslista.pop(idx)

print("Bensa: " +str(bensakulutus))
print("Lainat: "+str(lainakulutus))
print("Elektroniikka: "+str(elektrokulutus))
print("Pelikulutus: " +str(pelikulutus))
print("Pikaruoka: " +str(pikaruokakulutus))
print("Ruokakulutus: "+ str(ruokakulutus))
for i in kulutuslista:
    print(i)

