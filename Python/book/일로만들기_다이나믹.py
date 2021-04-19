x = int(input())

list = [0] * (x + 1)

list[0] = 0
list[1] = 0

for i in range(2, x + 1):
    list[i] = list[i-1] + 1
    if i % 5 == 0:
        list[i] = min(list[i], list[i // 5] + 1)
    if i % 3 == 0:
        list[i] = min(list[i], list[i // 3] + 1)
    if i % 2 == 0:
        list[i] = min(list[i], list[i // 2] + 1)

print(list[x])