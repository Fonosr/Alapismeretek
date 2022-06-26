N = int(input(""))

X = []
for i in range(N):
    K = float(input(""))
    X.append(K)
M = 0
for y in range(len(X)):
    if X[y] > 0:
        M = M + 1
print(M)