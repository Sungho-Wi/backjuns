a = int(input())

if a < 4:
    dp = [0 for i in range(4)]
else:
    dp = [0 for i in range(a + 1)]
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, a + 1):
    if i % 3 == 0 and i % 2 == 0:
        if dp[i -1] < dp[int(i/3)] and dp[i -1] < dp[int(i / 2)]:
            dp[i] = dp[i - 1] + 1
            continue
        if dp[int(i/3)] < dp[int(i / 2)]:
            dp[i] = dp[int(i / 3)] + 1
            continue
        else:
            dp[i] = dp[int(i / 2)] + 1
            continue
    if i % 3 == 0:
        if dp[i-1] < dp[int(i/3)]:
            dp[i] = dp[i - 1] + 1
            continue
        dp[i] = dp[int(i/3)] + 1
        continue
    if i % 2 == 0:
        if dp[i-1] < dp[int(i/2)]:
            dp[i] = dp[i - 1] + 1
            continue
        dp[i] = dp[int(i / 2)] + 1
        continue
    dp[i] = dp[i - 1] + 1

print(dp[a])
