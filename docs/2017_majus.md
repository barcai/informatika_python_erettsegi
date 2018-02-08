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

```python
# 3. feladat
bekert_azonosito = input("3. feladat: A versenyző azonosítója = ")
bekert_megoldas = versenyzok[bekert_azonosito]
print('{}   (a versenyző válasza)'.format("".join(bekert_megoldas)))
```

## 4. feladat
> Írassa ki a képernyőre a helyes megoldást! A helyes megoldás alatti sorba „+” jelet tegyen, ha az adott feladatot az előző feladatban kiválasztott versenyző eltalálta, egyébként egy szóközt! A kiírást a mintának megfelelő módon alakítsa ki!

```python
print("4. feladat:")
print('{}   (a helyes megoldás)'.format("".join(megoldas)))
jo_megoldások = list(map(lambda betu: True if betu[0] == betu[1] else False, zip(megoldas, versenyzo_megoldas)))
print("{}   (a versenyző helyes válaszai)".format("".join(map(lambda x: "+" if x else "", jo_megoldások)))
```

## 5. feladat
> Kérje be egy feladat sorszámát, majd határozza meg, hogy hány versenyző adott a feladatra helyes megoldást, és ez a versenyzők hány százaléka! A százalékos eredményt a mintának megfelelően, két tizedesjeggyel írassa ki!

## 6. feladat
> A verseny feladatai nem egyenlő nehézségűek: az 1-5. feladat 3 pontot, a 6-10. feladat 4 pontot, a 11-13. feladat 5 pontot, míg a 14. feladat 6 pontot ér. Határozza meg az egyes versenyzők pontszámát, és a listát írassa ki a pontok.txt nevű állományba! Az állomány minden sora egy versenyző kódját, majd szóközzel elválasztva az általa elért pontszámot tartalmazza!

## 7. feladat
> A versenyen a három legmagasabb pontszámot elérő összes versenyzőt díjazzák. Például 5 indulónál előfordulhat, hogy 3 első és 2 második díjat adnak ki. Így megtörténhet az is, hogy nem kerül sor mindegyik díj kiadására. Írassa ki a mintának megfelelően a képernyőre a díjazottak kódját és pontszámát pontszám szerint csökkenő sorrendben!