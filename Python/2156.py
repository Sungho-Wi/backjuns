size = int(input())
value = [0]
for i in range(size):
    value.append(int(input()))

if size == 1:
    print(max(0, value[1]))
    exit()
elif size == 2:
    print(max(0, value[1]+value[2], value[1], value[2]))
    exit()
else:
    dp = [0, value[1], value[1] + value[2]]

for k in range(3, size + 1):
    dp.append(max(dp[k-2] + value[k], dp[k-3] + value[k-1] + value[k], dp[k-1]))

print(max(dp))