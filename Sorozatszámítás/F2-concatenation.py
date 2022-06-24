"""F2. Egy M elemű betűsorozat betűit fűzzük össze egyetlen szöveg típusú változóba!"""

X = int(input("Add meg az összeget: "))
M = []
for i in range(X):
    wrds = input(f"Add meg a(z) {i + 1}. szót: ")
    M.append(wrds)
F = "" 
for i in range(X):
    F = F + M[i]
print(F)