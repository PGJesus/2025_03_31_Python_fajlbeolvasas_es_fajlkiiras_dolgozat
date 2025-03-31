"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""
adatok = []
szam = 0

with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        nev, csapat, wins, done_matches = sor.strip().split(';')
        # print(nev, csapat, wins, done_matches)
        adatok.append([nev, csapat, int(wins), int(done_matches)])

    for sor in adatok:
        szam += 1

legtobbet_nyert = max(adatok, key=lambda x: x[2])

legtobbet_versenyzet = max(adatok, key=lambda x: x[3])

atlag_futamszam = 0
for versenyzo in adatok:
    atlag_futamszam += versenyzo[3]

with open('./kiirt_adatok/statisztika.txt', 'w', encoding='utf-8') as celfajl:
    print(f"A beolvasott fájlban összesen {szam} versenyző szerepel.", file=celfajl)
    print(f"A legtöbb futamot nyert versenyző: {legtobbet_nyert[0]}", file=celfajl)
    print(f"A legtöbb futamot teljesített versenyző: {legtobbet_versenyzet[0]}", file=celfajl)
    print(f"Az átlagos futamszám: {atlag_futamszam / len(adatok)}", file=celfajl)
