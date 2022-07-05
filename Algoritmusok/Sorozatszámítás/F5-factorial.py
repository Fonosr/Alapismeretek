from re import I


"""F5. Adjuk meg az első N természetes szám szorzatát (N faktoriális)!"""
N = int(input("Adj meg egy számot: "))
X = 1
for i in range(1,N+1):
    X = X * i 