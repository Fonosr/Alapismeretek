"""F14. A Budapest–Nagykanizsa vasúti menetrend alapján két adott állomáshoz adjunk meg egy olyan vonatot, amellyel el lehet jutni átszállás nélkül az egyikről a másikra!"""
M = int(input("Hány állomás van: "))
BN = {}
for i in range(M):
    L = input(f"Add meg a(z) {i+1} állomást: ")
    K = int(input("Add meg hogy átkell szállni 1(igen) 0(nem): "))
    BN[L] = K

VN = []
for m in BN:
    if BN[m] == 0:
        VN.append(m)

print(f'{VN[0]}-ból eljuthatsz - {VN[-1]}-be átszállás nélkül.')
