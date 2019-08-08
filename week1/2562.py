a = list()
for i in range(0, 9):
    insert = int(input())
    if insert > 100:
        exit()
    a.append(insert)

maxValue = max(a)
print(maxValue)
print(a.index(maxValue)+1)
