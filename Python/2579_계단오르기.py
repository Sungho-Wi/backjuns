N = int(input())

floor_list = []

for _ in range(N):
    floor_list.append(int(input()))

if N < 3:
    if N == 0:
        print(0)
    elif N == 1:
        print(floor_list[0])
    elif N == 2:
        print(floor_list[0] + floor_list[1])

    exit()


dp = []

dp.append(floor_list[0])
dp.append(max(floor_list[0] + floor_list[1], floor_list[1]))
dp.append(max(floor_list[0] + floor_list[2], floor_list[1] + floor_list[2]))

for i in range(3, N):
    dp.append(max(dp[i - 2] + floor_list[i], dp[i - 3] + floor_list[i - 1] + floor_list[i]))

print(dp.pop())
