N = int(input(""))

X = []
Y = []
M = list(map(int,input("").split()))
V = list(map(int,input("").split()))
X.append(M)
X.append(V)
S = input("").split()
for m in range(len(S)):
    S[m] = int(S[m])

Y.append([S[0],S[1]])

for i in range(N-1):
    S[0],S[1] = S[0],S[1] + X[0][i]
    if S[1] > 60:
        S[1] = S[1] - 60
        S[0] += 1
    Y.append([S[0],S[1]])

