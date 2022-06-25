"""F16. Családok létszámának, illetve jövedelmének alapján állapítsuk meg, hogy hány család él a létminimum alatt!"""

N = int(input("Add meg a családok számát: "))
mn = float(input("Mennyi a létminimum: "))
X = {}
for i in range(N):
    n = float(input(f"Add meg a(z) {i+1} család keresetét: "))
    X[i+1] = n 
B = 0
for m in X:
    if X[m] <= mn:
        B += 1
print(f'{B} család él létminimum alatt.')