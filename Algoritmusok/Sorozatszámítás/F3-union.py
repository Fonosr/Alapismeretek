"""F3. Készítsünk algoritmust, amely egy autóversenyző körönkénti ideje alapján meghatározza a versenyző egy kör megtételéhez szükséges átlagidejét!"""

N = int(input("Add meg a körök számát: "))
X = []
for i in range(N):
    ci = float(input(f"Add meg a(z) {i+1}. kör idejét: "))
    X.append(ci)
M = []
for y in range(N):
    M = list(set(M) | set(X))
for x in range(0, len(M)):
    M[i] = int(M[i])
print(sum(M)/len(M))