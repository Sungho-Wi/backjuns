N = int(input())
players = sorted(list(map(int, input().split())))

count = 0
groups = 0

for p in players:
    count += 1
    if count >= p:
        count = 0
        groups += 1

print(groups)