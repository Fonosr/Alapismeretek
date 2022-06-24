"""F13. Ismerjük egy üzlet egy havi forgalmát: minden napra megadjuk, hogy mennyi volt a bevétel és mennyi a kiadás. Adjunk meg egy olyan napot – ha van –, amelyik nem volt nyereséges! ⇒ A nem nyereséges nap megadása."""

Day = int(input("Add meg a napok számát: "))

B = {} # Bevétel 
N = {} # Kiadás 
for i in range(0,Day):
    bv = float(input(f"Add meg a bevételt a(z) {i + 1}. napon: "))
    k = float(input(f"Add meg a kiadást a(z) {i + 1}. napon: "))
    B[bv] = i+1
    N[k] = i+1

for (x,y) in zip(B,N):
    if x < y:
        print(f'{B[x]}. nap nem volt nyereséges ennyit veszített: {y-x}')