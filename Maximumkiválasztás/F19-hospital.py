"""F19. Egy kórházban megmérték minden beteg lázát, adjuk meg, hogy ki a leglázasabb!"""
N = int(input("Add meg a páciensek számát: "))
X = []
for i in range(N):
    temp = float(input(f"Adja meg a(z) {i+1}. páciens hőfokát: "))
    X.append(temp)

xl = X[0]
m = 1
for x in range(len(X)):
    if X[x] > xl:
        xl = X[x]
        m += 1
print(f'A(z) {m}. páciens hőfoka a legnagyobb: {xl}')