"""F4. A Balaton mentén K db madarász végzett megfigyeléseket. Mindegyik megadta, hogy milyen madarakat látott. Készítsünk algoritmust, amely megadja a megfigyelések alapján a Balatonon előforduló madárfajokat!"""
K = int(input("Madarászok száma: "))
X = []
for i in range(K):
    birds = input( f"Add meg a(z) {i+1}. madár nevét: ")
    X.append(birds)

countx = 0 
frequent = ""
for y in X:
    ims = X.count(y)
    if (ims > countx):
        countx = ims
        frequent = y 
print(frequent)