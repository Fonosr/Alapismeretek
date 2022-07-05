"""F12. A naptárban található névnapok alapján adjuk meg legjobb barátunk (barátnőnk) névnapját! (Itt nem a „legjobbság” megfogalmazása okozza az algoritmikai problémát.)"""
N = input("Add meg a barátod nevét: ")
X = {
    "Alfonz": 23,
    "Aladár": 12,
}

for k in X:
    v = X[k]
    if N == k:
        print(f'{k} {v}')