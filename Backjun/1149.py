size = int(input())

dp = []
total = []
dp.append([0, 0, 0])
for i in range(size):
    dp.append(list(map(int, input().split())))
total.append([-1, 0]) #total[0]
total.append([dp[1].index(min(dp[1])), min(dp[1])]) # 첫 최소값

for j in range(2, size+1):
    if total[j-1][0] != dp[j].index(min(dp[j])):
        total.append([dp[j].index(min(dp[j])), total[j-1][1] + min(dp[j])])
    else:
        sorts = sorted(dp[j])
        presorts = sorted(dp[j-1])
        if total[j-2][0] != dp[j-1].index(presorts[1]):
            prevalue = total[j-2][1] + presorts[1]
        else:
            prevalue = total[j - 2][1] + presorts[2]

        if j>= 3:
            prepresorts = sorted(dp[j-2])
            if total[j-3][0] != dp[j-2].index(prepresorts[1]):
                preprevalue = total[j-3][0] + prepresorts[1]
            else:
                preprevalue = total[j - 3][0] + prepresorts[2]
            if (total[j - 1][1] + sorts[1]) < (prevalue + min(dp[j])):
                if (total[j - 1][1] + sorts[1]) > preprevalue + min(dp[j]):
                    total.append([dp[j].index(min(dp[j])), preprevalue + min(dp[j])])
                    continue
                total.append([dp[j].index(sorts[1]), total[j - 1][1] + sorts[1]])
            else:
                if (prevalue + min(dp[j])) > preprevalue + min(dp[j]):
                    total.append([dp[j].index(min(dp[j])), preprevalue + min(dp[j])])
                    continue
                total.append([dp[j].index(min(dp[j])), prevalue + min(dp[j])])
                continue

        if (total[j-1][1] + sorts[1]) < (prevalue + min(dp[j])):
            total.append([dp[j].index(sorts[1]), total[j-1][1] + sorts[1]])
        else:
            total.append([dp[j].index(min(dp[j])), prevalue + min(dp[j])])

print(total[-1][1])