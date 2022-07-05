"""F15. Egy tetszőleges (nem 1) természetes számnak adjuk meg egy osztóját, ami nem az 1 és nem is önmaga."""

N = int(input("Adj meg egy tetszőleges számot: "))
Y = [2,3,5,7]
if N == 1:
    raise("Sajnálom a szám nem lehet 1.")

for i in range(len(Y)):
    if N % Y[i] == 0 and N != Y[i]:
        print(Y[i])
    elif N == Y[i]:
        raise("A szám csak önmagával osztható.")