

megoldas = []
adat = {}

def pontszam(helyes_megoldas, versenyzo_megoldas):
    jo_megoldasok = map(lambda x: True if x[0] == x[1] else False, zip(helyes_megoldas, versenyzo_megoldas))
    pass
    

# Adatstruktura
# versenyzok = {
#   versenyzoazonosito: [megoldas, pontszam]
# }

# 1. feladat
print("1. feladat: Az adatok beolvasása")
with open("valaszok.txt") as f:
    megoldas = list(f.readline().strip())
    for sor in f:
        sor = sor.strip().split()
        adat[sor[0]] = list(sor[1])

# from pprint import pprint
# pprint(adat)
"""
# 2. feladat
print("2. feladat: A vetélkedőn {} versenyző indult.".format(len(adat)))

# 3. feladat
versenyzo_azonosito = input("3. feladat: A versenyző azonosítója = ")
versenyzo_megoldas = adat[versenyzo_azonosito]
print('{} (a versenyző válasza)'.format("".join(versenyzo_megoldas)))

# 4. feladat
print("4. feladat:")
print('{} (a helyes megoldás)'.format("".join(megoldas)))
megoldas_matrix = map(lambda x: "+" if x[0] == x[1] else " ", zip(megoldas, versenyzo_megoldas))
print("{} (a versenyző helyes válaszai)".format("".join(megoldas_matrix)))

# 5. feladat
feladat_szama = int(input("5. feladat: A feladat sorszáma = "))
helyes_valaszok = 0
for azonosito, valaszok in adat.items():
    if megoldas[feladat_szama] == valaszok[feladat_szama]:
        helyes_valaszok += 1
print("A feladatra {} fő, a versenyzők {:.2f}%-a adott helyes választ.".format(helyes_valaszok, (helyes_valaszok/len(adat))*100 ))"""

# 6. feladat
print("6. feladat: A versenyzők pontszámának meghatározása")
pontozas = [3 if num < 6 else (4 if num < 11 else 5) for num in range(1, 14) ] + [6]
print(sum(pontozas))
with open("pontok.txt", "w") as f:
    for azonosito, valaszok in adat.items():
        osszpont = sum(map(lambda y: y[0] * y[1], zip(pontozas, map(lambda x: 1 if x[0] == x[1] else 0, zip(megoldas, valaszok)))))
        f.write("{} {}\n".format(azonosito, osszpont))