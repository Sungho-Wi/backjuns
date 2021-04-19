n = int(input())
k = list(map(int, input().split()))

result = []

result.append(k[0])
result.append(max(k[0], k[1]))

for i in range(2, n):
    result.append(max(result[i - 1], result[i - 2] + k[i]))

print(result[n-1])
