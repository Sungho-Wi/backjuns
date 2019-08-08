list = []
for i in range(0, 10):
    a = int(input())
    b = a % 42
    if (b in list) == True:
        continue
    else:
        list.append(b)

print(len(list))