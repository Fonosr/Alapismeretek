"""F20. Egy család havi bevételei és kiadásai alapján adjuk meg, hogy melyik hónapban tudtak a legtöbbet megtakarítani!"""

N = int(input("Hány hónap: "))
H = {}

for i in range(N):
    l = float(input(f'Mennyi volt a bevételed a(z) {i+1}. hónapban: '))
    v = float(input(f'Mennyi volt a kiadásod a(z) {i+1}. hónapban: '))
    H[i+1] = l-v

xl = H[1]
m = 1
for x in range(len(H)):
    if H[x+1] > xl:
        xl = H[x+1]
        m += 1
print(f'Hónap: {m} Összeg: {xl}')