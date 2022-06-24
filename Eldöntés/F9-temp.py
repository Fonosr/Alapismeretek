"""F9. Júniusban minden nap délben megmértük, hogy a Balaton Siófoknál hány fokos. Döntsük el a mérések alapján, hogy a víz hőfoka folyamatosan emelkedett-e!"""

N = int(input("Hány nap: "))
X = []
for i in range(N):
    temp = float(input(f"Add meg a(z) {i+1}. értéket: "))
    X.append(temp)
I = 1
for y in range(N - 1):
    if X[y] <= X[y + 1]:
        I = I + 1
print(I>N-1)