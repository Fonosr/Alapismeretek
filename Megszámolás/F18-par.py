"""F18. Adjuk meg egy szöveg magánhangzóinak számát!"""

Par = input("Adj meg egy szöveget: ")

n = 0
for i in Par:
    if i in "AÁEÉIÍOÓÖŐUÚÜŰYaáeéiíoóöőuúüűy":
        n += 1
print(f'Magánhangzók száma: {n}')