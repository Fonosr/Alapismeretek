"""Egy fesztivál minden napján feljegyezték, hogy hány belépőt adtak el aznap. Készítsünk programot, amely meghatározza, hogy melyik napon voltak a legtöbben a fesztiválon!"""
"""
Alkalmazott tétel
Maximumkiválasztás
"""
N = int(input("Add meg hogy hány nap: "))
X = []
for i in range(N):
    m = int(input("Hány belépő kelt el a mai nap: "))
    X.append(m)

ml = X[0]
m = 1
for y in range(len(X)):
    if X[y] > ml:
        ml = X[y]
        m += 1
print(f'A legtöbb eladott. {m}. napon összeg: {ml}')