"""Egy papírgyűjtési akcióban mindenkiről feljegyezték, hogy ki hány kiló papírt hozott. Írjunk programot, amely megadja, hogy összesen mennyi papírt gyűjtöttek a résztvevők!"""
"""
Alkalmazott tétel
Sorozatszámítás
"""
N = int(input("Hány résztvevő volt: "))

T = []
for i in range(N):
    mass = float(input(f"Add meg hogy a(z) {i+1}. résztvevőnek mennyit mértek: "))
    T.append(mass)

total = 0
for x in range(len(T)):
    total = total + T[x]
print(total)