"""F17. Egy futóverseny végeredménye határozzuk meg, hogy a versenyzők hány százaléka teljesítette az olimpiai induláshoz szükséges szintet!"""

N = int(input("Hány futó vett részt a versenyen: "))
min = float(input("Add meg az olimpiai induláshoz szükséges szintet: "))
X = {}
for i in range(N):
    time = float(input(f"Add meg a(z) {i+1} futó végeredményét: "))
    X[i+1] = time 
DB = 0
for y in X:
    if X[y] < min:
        DB += 1
print(f'Százalék: {100*DB/N}% Összesen: {DB} futó jutott tovább.')