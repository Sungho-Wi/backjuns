size = int(input())

n = list(map(int, input().split()))
n.insert(0, 0)

dp = [0]
for i in range(1, len(n)):
    result = []
    for j in range(i):
        if n[i] > n[j]:
            result.append(dp[j])
    dp.append(max(result) + 1)

print(max(dp))