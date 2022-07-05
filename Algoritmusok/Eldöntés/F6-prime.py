"""F6. Döntsük el egy számról, hogy prímszám-e!"""
N = int(input("Mennyi akarsz megadni: "))

y = [2,3,5,7]
sw = False 
for k in y:
    if k <= N - 1 and not sw:
        if N % k == 0:
            sw = True 
        y = k + 1
if not sw:
    print("True")
