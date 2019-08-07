size = int(input())

red = [0]
green = [0]
blue = [0]

for i in range(size):
    r, g, b = map(int, input().split())
    red.append(r)
    green.append(g)
    blue.append(b)

DP = [[0, 0, 0]]

for j in range(1, size + 1):
    R = min(DP[j-1][1], DP[j-1][2]) + red[j]
    G = min(DP[j - 1][0], DP[j - 1][2]) + green[j]
    B = min(DP[j - 1][0], DP[j - 1][1]) + blue[j]
    DP.append([R, G, B])

print(min(DP[-1][0], DP[-1][1], DP[-1][2]))