n = int(input())

list = []

for i in range(n):
    list.append(int(input()))

max_value = max(list)

result = [0] * (max_value + 1)

for v in list:
    result[v] += 1

for k in range(len(result) - 1, 0, -1):
    for m in range(result[k]):
        print(k, end=' ')