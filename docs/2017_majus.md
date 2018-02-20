# 2017 májusi programozás megoldás

## Kezdetek

Lássuk mit hozott nekünk a 2017-es májusi érettségi.

Lejjebb megtalálod az egyes feladatok megoldásait és miértjét, illetve az oldal alján pár érdekes megoldási lehetőséget, amennyiben egy pöppet jobban belevetnéd magad a python érdekességeibe.

Indulás!

## 0. feladat

Mint mindig, most is érdemes átolvasni a feladat egészét, hiszen az adatstruktúránkat és ebből kifolyólag a programunkat nem szeretnénk minden egyes feladat előtt-közben-után újraírni.

Ugyan véleményem szerint a probléma nem kíván egy nagyon komplex adatstruktúrát, de több alternatívánk is van. Én a dictionary alapú megoldásokat kedvelem, így itt is azt használtam, de találhatsz listával is megoldást többek között
[PythonIdomár](https://pythonidomar.wordpress.com/2018/01/23/tesztverseny-a-2017-majusi-emelt-szintu-informatika-erettsegi-programozas-feladatanak-megoldasa/)
videóiban. Lássuk a dictionary-s megoldás hogy is néz ki:


```python hl_lines="8 9 11"
versenyzok = {}
# Adatstruktura
# versenyzok = {
#   versenyzoazonosito: megoldas
# }
# Példa:
versenyzok = {
    'AB123': 'BXCDBBACACADBC',
    'AH97': 'BCACDBDDBCBBCA',
    # ...
    'ZZ240': 'ABBCDADDCACDDD'
}

```


!!! hint "Dokumentáció"
    Bármelyik adattípus mellett döntesz, a Python Interacive Shell-jében tudsz segítséget kapni ha elakadsz. Egyszerűen indítsd el az interpreter-t és írd be, hogy help(). Ezután a kurzorod a megszokott >>>  helyett help>-re vált és innen beírva a "topics" parancsot, a shell ki fogja adni a nyelvel kapcsolatos elérhető témákat, amelyek közül bármelyiket kiválaszthatod. Amennyiben a dictionary-kra vagy kíváncsi, írd be, hogy "DICTIONARIES".

## 1. feladat

> Olvassa be és tárolja el a valaszok.txt szöveges állomány adatait!

Miután döntöttünk az adatstruktúránkkal kapcsolatban ideje feltörlteni azt adattal. Ez szerencsére nagyon egyszerű Pythonban. Lássuk is:

```python
# Feladat számának kiírása
print("1. feladat: Az adatok beolvasása")

# Beolvassuk a valaszok.txt fájlt soronként
with open("valaszok.txt") as f:
    # Első sor lesz a helyes megoldás, őt külön változóba mentjük
    megoldas = f.readline().strip()
    for sor in f:
        # Soronként átmegyünk a fájlon
        sor = sor.strip().split()
        # Felbontjuk egy két elemű listára
        # sor = [azonosító, megoldás]
        versenyzok[sor[0]] = sor[1]
        # Végül lementjük a dictionary-nkbe
```

Nézzük át mit is csináltunk.

Először, mint ahogy le is van írva a feladatlapban, kiírjuk a képernyőre, hogy hányadik feladaton dolgozunk. Ez kötelező és a többi feladatnál már nem ejtek róla szót.

Ezután egy olyan kulcsszóval találkozunk amit sokan nem ismernek, vagy csak és kizárólag fájlbeolvasásnál látták. Ez a **with** kulcsszó. Ez egy úgy nevezett [context manager](https://docs.python.org/3/reference/datamodel.html#context-managers), aminek az a dolga, hogy ami a blokkban történik, annak gyakorlatilag egy környezetet hoz létre és kezeli az abba való be- és kilépést illetve bármit változtathat ezen a környezeten, opcionálisan változókat is adhat ebbe a környezetbe. Ezt kicsit egyszerűbben a példa segítségével átfogalmazva azt láthatjuk, hogy az [open](https://docs.python.org/3/library/functions.html#open) függvény által visszaadott értéket egy _f_ nevű változóba adja át. Ez az _f_ változó, amíg ennek a __with__ blokkban vagyunk, elérhető és olvasható.

Következő részben pedig jön a fájl olvasása. Érdemes megfigyelni, hogy minden sor beolvasása után használom a [strip](https://docs.python.org/3/library/stdtypes.html#str.strip) függvényt. Ez abban segít, hogy lecsippantja a sor elején és végén levő új sor karaktert illetve extra szóközöket és tabokat. Ezek csak zavarnának a további munkában úgyhogy szabaduljunk meg tőlük. Ezek után beolvassuk az első sort a [readline](https://docs.python.org/3/library/io.html#io.TextIOBase.readline) függvénnyel, ami már csak a nevéből kitalálhatóan egy sort olvas be. A feladat leírása szerint ez lesz a megoldásunk.
Ezek után pedig átmegyünk minden egyes soron és elmentjük a versenyzők közé az adatot asszociálva a versenyző kódját annak megoldásával.

## 2. feladat

> Jelenítse meg a képernyőn a mintának megfelelően, hogy hány versenyző vett részt a tesztversenyen!

A második feladatunk, hogy számoljuk meg, összesen hány versenyzőnk van. Itt egy egyszerű feladatot kaptunk amit a beépített [len]() függvénnyel tudunk legkönnyebben megoldani.

Lets see:

```python
print("2. feladat: A vetélkedőn {} versenyző indult.".format(len(versenyzok)))
```

## 3. feladat

> Kérje be egy versenyző azonosítóját, és jelenítse meg a mintának megfelelően a hozzá eltárolt válaszokat! Feltételezheti, hogy a fájlban létező azonosítót adnak meg.

Annak köszönhetően, hogy az adatstruktúránknak a dictionary adattípust választottuk, a megoldásunk erre a feladatra meglehetősen könnyű lesz. Mivel minden megoldást egy versenyző azonosítóval asszociálunk így csak a felhasználótól bekért adatot egy az egybe átadhatjuk az asszociatív tömbünknek és ő hatalmas örömünkre ki is köpi a megoldást.

Lássuk ezt hogyan is csináljuk:

```python
# 3. feladat
bekert_azonosito = input("3. feladat: A versenyző azonosítója = ")
bekert_megoldas = versenyzok[bekert_azonosito]
print('{}   (a versenyző válasza)'.format("".join(bekert_megoldas)))
```

## 4. feladat

> Írassa ki a képernyőre a helyes megoldást! A helyes megoldás alatti sorba „+” jelet tegyen, ha az adott feladatot az előző feladatban kiválasztott versenyző eltalálta, egyébként egy szóközt! A kiírást a mintának megfelelő módon alakítsa ki!

Nos, ez a feladat kicsit elgondolkodtatóbb, én csináltam is rá egy kér soros megoldást, de ez kicsit magasabb szintű és nem szükséges ahhoz, hogy meg tudd oldani a feladatot, de amennyiben érdekel, megosztom az oldal alján ezt is.

A feladatot leglogikusabban úgy lehet megközelíteni, ha átmegyünk rajta soronként. A problémánk paramétereiként megkapjuk az aranyifjúnk megoldását, illetőleg a megoldókulcsot és ki kéne magából köpni két egymást követő sorra a megoldást és hogy miket találtunk el. Ezek közül az első egyszerű, hiszen a megoldást külön változóba beolvastuk a feladatlap 0.feladataként. A másodikra megoldásként pedig tudunk adni egy Pythonikus és egy kevésbe Pythonikus megoldást. A második az, ahogyan a legtöbb nyelvben megoldanád, az első pedig, mint Python fejlesztő, az én plusz pontjaimmal örvendeztetne a helyes megoldáson kívül.

**Lássuk is őket:**

Pythonikus:

```python
print("4. feladat:")
# Kiírjuk a helyes megoldást
print('{}   (a helyes megoldás)'.format(megoldas))

# Ez lehetne lista is amit a végén összefűzünk, de legyen most string típusú
helyesseg = ""
for jo_betu, versenyzo_betu in zip(megoldas, bekert_megoldas):
    if jo_betu == versenyzo_betu:
        helyesseg += "+"
    else:
        helyesseg += " "

print("{}   (a versenyző helyes válaszai)".format(helyesseg)
```

Gyors info a Pythonikus megoldásról. Ugye itt mi a zip beépített függvényt használtuk. Ez azt fogja nekünk csinálni, hogy a két (vagy több) szekvenciánkból egy listát fog összerakni, amiben az egyes elemek két (vagy amennyiben több szekvenciát adtunk meg bemeneti paraméterként, több) elemű listáká alakulnak (tuple-ek lesznek, de ez most nem számít) amiket ilyen nagyon szépen a for ciklusunkban két változóba tudunk bepakolni. Ez a Python nyelv egyik nagyon szép megoldása, ami ebben a feladatban nagyon sokat nem fog változtatni, de nagyobb szoftverekben sokat segíthet a kód megértésében és tisztán tartásában.

Illetve lássuk a kevésbé Pythonikusat:

```python
print("4. feladat:")
# Kiírjuk a helyes megoldást
print('{}   (a helyes megoldás)'.format(megoldas))

# Ez lehetne lista is amit a végén összefűzünk, de legyen most string típusú
helyesseg = ""
for index in range(megoldas):
    if megoldas[index] == bekert_megoldas[index]:
        helyesseg += "+"
    else:
        helyesseg += " "

print("{}   (a versenyző helyes válaszai)".format(helyesseg)
```

Természetesen ezzel a megoldással sincs semmi gond. Itt egyszerűen átmegyünk a két string indexein és azokat hasonlítjuk össze.

Mind a két megoldás pontosan ugyan azzal az eredménnyel fog végződni, ami a jó megoldás.

*u.i.:* 3 soros megoldás *(magyarázat erre az összegzés után)*:

```python
print("4. feladat:")
print('{}   (a helyes megoldás)'.format(megoldas))
print("{}   (a versenyző helyes válaszai)".
      format("".
      join(map(lambda x: "+" if  x[0]==x[1] else " ",
           zip(megoldas, bekert_megoldas))))
```

*u.u.i.:* Technikailag 5 soros, de csak a jobban olvashatóság kedvéért.

## 5. feladat

> Kérje be egy feladat sorszámát, majd határozza meg, hogy hány versenyző adott a feladatra helyes megoldást, és ez a versenyzők hány százaléka! A százalékos eredményt a mintának megfelelően, két tizedesjeggyel írassa ki!

Következő feladatunk egy egészen egyszerű statisztikai kérdés lesz. Ha szeretnénk, megírhatjuk ezt a feladatot a következő sorokban is, de én egy gyors függvény felvázolása mellett döntöttem, hiszen arra példát még nem is láttunk. Ugyebár a függvényünkben gyakorlatilag egyetlen lokális változóra lesz szükségünk, ami a helyes válaszok mennyiségét tartja majd nekünk számon, hiszen a paraméterként megkapott versenyzők megadják az összes versenyzőnek a számát. Nézzük is meg hogy is írjuk meg a függvényünk:     íííííí

```python
# Függvény az 5. feladathoz
def (feladat_szama, megoldas, versenyzok):
    helyes_valaszok_szama = 0

    for azonosito, valaszok in adat.items():
        if megoldas[feladat_szama] == valaszok[feladat_szama]:
            helyes_valaszok_szama += 1

    return helyes_valaszok_szama


```

A program következő sorában pedig meg is hívjuk a függvényt:

```python
feladat_szama = int(input("5. feladat: A feladat sorszáma = "))
```

A két tizedesjeggyel való kiíráshoz pedig két féle módon ugorhatunk neki. Az egyik megoldás a string adattípussal érkező format függvény. Ő millió és egy dolgot tud neked csinálni, érdemes utánanézni. Én amikor érettségiztem, lusta voltam ezzek közül kikeresni, de kétség kívül a format-tal lehetne szépen és elegánsan megoldani. A másik propozált variáció ami hirtelen még a fejembe ötlött az a beépített round függvény, ami adott mennyiségű tizedesjegyre kerekíti a számod, ha megadsz a hívásakor egy második paramétert. Nézzük is meg mind a kettőt:

```python
# Format beépített lehetőségeivel kreált megoldás
print("A feladatra {} fő, a versenyzők {:.2f}%-a adott helyes választ.".
      format(helyes_valaszok, (helyes_valaszok/len(adat))*100 ))

# round függvénnyel létrehozott megoldás
print("A feladatra {} fő, a versenyzők {}%-a adott helyes választ.".
      format(helyes_valaszok, round((helyes_valaszok/len(adat))*100) ))
```

## 6. feladat

> A verseny feladatai nem egyenlő nehézségűek: az 1-5. feladat 3 pontot, a 6-10. feladat 4 pontot, a 11-13. feladat 5 pontot, míg a 14. feladat 6 pontot ér. Határozza meg az egyes versenyzők pontszámát, és a listát írassa ki a pontok.txt nevű állományba! Az állomány minden sora egy versenyző kódját, majd szóközzel elválasztva az általa elért pontszámot tartalmazza!

```python

```

## 7. feladat

> A versenyen a három legmagasabb pontszámot elérő összes versenyzőt díjazzák. Például 5 indulónál előfordulhat, hogy 3 első és 2 második díjat adnak ki. Így megtörténhet az is, hogy nem kerül sor mindegyik díj kiadására. Írassa ki a mintának megfelelően a képernyőre a díjazottak kódját és pontszámát pontszám szerint csökkenő sorrendben!

```python

```