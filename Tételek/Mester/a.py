"""Írj programot, amely megadja a 7. generációban megjelent konzolok gyártóinak számát és nevüket!"""
N = int(input("")) # gyártók száma 
X = []
for i in range(1,N+1):
    c = str(input(""))
    X.append(c)
L = int(input("")) # feljegyzések száma
A = []
exist = False
for n in range(L):
    gy,g,k = map(int,input().split())
    A.append([gy,g,k]) # Gyártó # Generáció # Konzolok száma
a,b = map(int(input("").split()))

G = []
cn = 0
for l in range(len(X)):
    if A[l][1] == 7:
        cn += 1
        G.append(X[l])
        exist = True 
t = ""
for l in G:
    t += l 
print(cn,t)
if not exist:
    print("0 Nincs")