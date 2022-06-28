N = int(input(""))

X = []
for i in range(N):
    tem = int(input(""))
    X.append(tem)
m = 0
for y in range(len(X)):
    if X[y] < 0:
        m += 1
print(m)