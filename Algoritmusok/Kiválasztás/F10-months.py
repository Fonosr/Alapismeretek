"""F10. Ismerjük egy hónap nevét, a hónapnevek sorozata alapján mondjuk meg a sorszámát!"""
months = [
    "Január",
    "Február",
    "Március",
    "Április",
    "Május",
    "Június",
    "Július",
    "Augusztus",
    "Szeptember",
    "Október",
    "November",
    "December"
]
month = input("Adj meg egy hónapot: ")

for i in range(0,len(months)): 
    if month == months[i]:
        print(f"A hónap sorszáma: {i}")