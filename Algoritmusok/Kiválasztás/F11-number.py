"""F11. Adjuk meg egy természetes szám legkisebb, 1-től különböző osztóját!"""

N = int(input("Adj meg egy számot: "))

M = [2,3,5,7]
for i in range(len(M)):
    if N % M[i] == 0:
       print(M[i])
       break 
