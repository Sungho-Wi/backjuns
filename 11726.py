n = int(input())

dp = [0, 1, 3, 5]

if n >= 4:
    for i in range(4, n+1):
        dp.append(((dp[i-2] * 2) + dp[i-1]) % 10007)

print(dp[n])
