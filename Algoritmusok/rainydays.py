N = int(input(""))
X = []
for i in range(N):
    mm = int(input(""))
    X.append(mm)

a = 0
for x in range(len(X)):
    if X[x] > 0:
        a += 1
print(a)