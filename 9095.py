size = int(input())

value = []
for i in range(size):
    value.append(int(input()))

dp = [0, 1, 2, 4]

if max(value) >= 4:
    for k in range(4, max(value)+1):
        dp.append(dp[k - 3] + dp[k - 2] + dp[k - 1])

for x in value:
    print(dp[x])