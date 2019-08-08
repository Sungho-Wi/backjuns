size = input()
size = int(size)
list = list(map(float, input().split()))

maxValue = max(list)
avg = 0.0

for i in range(0, size):
    if list[i] == maxValue:
        avg += list[i]
        continue
    avg += (list[i] / maxValue) * 100

print(avg / size)