"""F21. Egy osztály tanulói nevei alapján adjuk meg a névsorban legelső tanulót!"""

N = int(input("Adja meg hány diák van: "))
X = []
for i in range(N):
    m = input(f"Adja meg a(z) {i+1}. tanuló nevét: ").lower()
    X.append(m)

L = []

while X:
    mn = X[0]
    for y in X:
        if y < mn:
            mn = y
    X.remove(mn)
    L.append(mn)
print(f"Az első tanuló neve: {L[0]}")        