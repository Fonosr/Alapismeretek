"""F8. Döntsük el egy tanuló év végi osztályzatai alapján, hogy kitűnő tanuló-e!"""
N = int(input("Add meg tantárgyak számát: "))
X = []
for i in range(N):
    grade = float(input(f"Add meg a(z) {i+1}. jegyet: "))
    X.append(grade)
xs = False
limit = float(input("Mennyitől adod meg az ötöst: "))
for y in X:
    if y >= limit:
        xs = True
print(xs)