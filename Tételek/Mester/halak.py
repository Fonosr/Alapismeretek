N = int(input(""))

Count = {}

for i in range(1,N+1):
    fish = int(input(""))
    Count[i] = (fish)

exist = False 

for (k,v) in enumerate(Count.items()):
    if v[1][1] < 1:
        print(v[1][0])
        exist = True
        break

if not exist:
    print("-1")