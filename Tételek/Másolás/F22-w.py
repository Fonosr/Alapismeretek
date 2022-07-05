"""F23. Egy szöveg minden magánhangzóját cseréljük ki az e betűre!"""

N = int(input("Add meg a szövegek számát: "))

vowels = 'AEIOUaeiou'
X = []
Y = []

for i in range(N):
    w = input(f"Add meg a(z) {i+1}. szöveget: ")
    X += w
    Y += w
    
for i in range(len(X)):
    if X[i] in vowels:
        Y[i] = 'e'
    else:
        Y[i] = X[i]

print(Y)