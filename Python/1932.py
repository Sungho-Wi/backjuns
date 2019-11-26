size = int(input())

n = [0]
for i in range(size):
    n.append(list(map(int, input().split())))


for k in range(len(n[-1]) -1, 0, -1):
    for x in range(k):
        n[k][x] += max(n[k+1][x], n[k+1][x+1])

print(n[1][0])
