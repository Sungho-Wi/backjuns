test = int(input())

for i in range(test):
    size = int(input())
    value = list(map(int, input().split()))
    value.insert(0, 0)
    dp = [0]
    dp.append(value[1])
    dp.append(value[1] + value[2])
    for n in range(3, size+1):
        if n % 2 != 0:
            dp.append(dp[n-1] + value[n])
        else:
            dp.append(((dp[n-2] + (value[n-1] + value[n])) * 2))

    print(dp)