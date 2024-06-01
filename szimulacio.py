import random

# Kifizetési mátrix
kifizetes = {
    ('K', 'K'): (-1, -1),
    ('K', 'Á'): (-20, 0),
    ('Á', 'K'): (0, -20),
    ('Á', 'Á'): (-5, -5)
    
    
}

# Árulásra áruló stratégia
def arulasra_arul(sajat_lepesek, ellenfel_lepesei):
    if len(sajat_lepesek) == 0:
        return 'K'
    elif ellenfel_lepesei[-1] == 'Á':
        return 'Á'
    else:
        return 'K'

# Véletlenszerű stratégia
def veletlenszeru(sajat_lepesek, ellenfel_lepesei):
    return random.choice(['K', 'Á'])

# Árulásra kétszer áruló stratégia
def arulasra_arul_ketszer(sajat_lepesek, ellenfel_lepesei):
    if len(sajat_lepesek) == 0:
        return 'K'
    elif ellenfel_lepesei[-1] == 'Á':
        return 'Á'
    elif len(ellenfel_lepesei)>=2 and ellenfel_lepesei[-2] == 'Á':
        return 'Á'
    else:
        return 'K'

# Mindig áruló stratégia
def mindig_arul(sajat_lepesek, ellenfel_lepesei):
    return 'Á'

# 75 százalékban áruló stratégia
def haromnegyed_arul(sajat_lepesek, ellenfel_lepesei):
    if random.random() < 0.75:
        return 'Á'
    else:
        return 'K'

# Folyton váltakozó stratégia
def valtakozo(sajat_lepesek, ellenfel_lepesei):
    if len(sajat_lepesek) % 2 == 0:
        return 'K'
    else:
        return 'Á'

# Játékosok és stratégiáik listája
jatekosok = [
    {"nev": "Árulásra árul", "strategia": arulasra_arul},
    {"nev": "Véletlenszerűen választ", "strategia": veletlenszeru},
    {"nev": "Árulásra kétszer árul", "strategia": arulasra_arul_ketszer},
    {"nev": "Mindig árul", "strategia": mindig_arul},
    {"nev": "75 százalékban árul", "strategia": haromnegyed_arul},
    {"nev": "Váltakozva kooperál és árul", "strategia": valtakozo}
]

# Függvény a játék lejátszására két játékos között
def jatek(jatekos1, jatekos2, iteraciok):
    jatekos1_lepesek = []
    jatekos2_lepesek = []
    jatekos1_pontok = 0
    jatekos2_pontok = 0
    for iteracio in range(iteraciok):
        j1_lepes = jatekos1["strategia"](jatekos1_lepesek, jatekos2_lepesek)
        j2_lepes = jatekos2["strategia"](jatekos2_lepesek, jatekos1_lepesek)
        jatekos1_lepesek.append(j1_lepes)
        jatekos2_lepesek.append(j2_lepes)
        kifizetes_j1, kifizetes_j2 = kifizetes[(j1_lepes, j2_lepes)]
        jatekos1_pontok += kifizetes_j1
        jatekos2_pontok += kifizetes_j2
        print(f"Iteráció {iteracio + 1}: {jatekos1['nev']}: {j1_lepes}, {jatekos2['nev']}: {j2_lepes}")
    print(f"{jatekos1['nev']}: {jatekos1_pontok} pont, {jatekos2['nev']}: {jatekos2_pontok} pont\n")
    return jatekos1_pontok, jatekos2_pontok

# Függvény az összes játékos közötti játék szimulálására
def szimulacio(jatekosok, iteraciok):
    pontok = {jatekos["nev"]: 0 for jatekos in jatekosok}
    jatekosok_szama = len(jatekosok)
    for i in range(jatekosok_szama):
        jatekos1 = jatekosok[i]
        for j in range(i+1, jatekosok_szama):
            jatekos2 = jatekosok[j]
            j1_pontok, j2_pontok = jatek(jatekos1, jatekos2, iteraciok)
            pontok[jatekos1["nev"]] += j1_pontok
            pontok[jatekos2["nev"]] += j2_pontok
    return pontok

# Változtatható iterációk száma
iteraciok_szama = 1000000

# Játék szimulálása
pontok = szimulacio(jatekosok, iteraciok_szama)

# Pontok rendezése és kiírása
rendezett_pontok = sorted(pontok.items(), key=lambda x: x[1], reverse=True)
print("\nPontszámok:")
for nev, pontszam in rendezett_pontok:
    print(f"{nev}: {pontszam} pont")