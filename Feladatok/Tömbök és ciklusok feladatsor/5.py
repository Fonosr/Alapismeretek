"""Egy T fős baráti társaság egy nyaralás minden napján feljegyezte, hogy aznap mennyit költöttek. Készítsünk programot, amely meghatározza, hogy hány olyan nap volt, amikor fejenként 100 eurónál is többet költöttek!"""
"""
Alkalmazott tétel
Megszámolás
"""
T = int(input("Add meg hányan voltatok: "))
N = int(input("Add meg hány napot voltatok ott: "))

X = []
for x in range(N):
    spn = float(input(f"{x+1}. Nap add meg költést: "))
    X.append(spn)
m = 0
for i in range(len(X)):
    if X[i]/T>100:
        m += 1
print(m)