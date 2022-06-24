"""F1. Egy osztály N db tanuló osztályzatának ismeretében adjuk meg az osztály átlagát!"""

N = int(input("Add meg az osztálylétszámát: "))
X = []
for i in range(N):
    grades = float(input( f"Add meg a(z) {i + 1}. jegyet: "))
    X.append(grades)
M = 0 
for y in range(N):
    M += X[y]
print(f'{M/N}')
