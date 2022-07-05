"""F7. Döntsük el egy szóról a hónapnevek sorozata alapján, hogy egy hónap neve-e!"""
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
    "Deberecen"
]
month = input("Add meg a hónap nevét: ")

for x in range(0,12): 
    if month == months[x].lower() or month == months[x] or month == months[x].upper():
        print("True")
    else:
        print("False")