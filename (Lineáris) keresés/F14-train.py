"""F14. A Budapest–Nagykanizsa vasúti menetrend alapján két adott állomáshoz adjunk meg egy olyan vonatot, amellyel el lehet jutni átszállás nélkül az egyikről a másikra!"""

N = int(input("Add meg az indulások számát: "))
BN = {}
for i in range(N):
    M = float(input(f"Add meg a(z) {i+1}. vonat indulási idejét: "))
    X = int(input(f"Add meg a(z) {i+1}. vonatnál van e-átszállás 0(nem) 1(igen): "))
    BN["Budapest-Nagykanizsa"] = M,X
for x in BN:
    if BN[x][1] == 0:
        print(f"Átszállás nélküli vonat időpont: {BN[x][0]}")