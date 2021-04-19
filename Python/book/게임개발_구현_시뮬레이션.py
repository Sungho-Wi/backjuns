n, m = map(int, input().split(' '))
# d = [[0] * m for _ in range(n)]
# print(d)
y, x, d = map(int, input().split(' '))

see = [(0, -1), (-1, 0), (0, 1), (1, 0)]

world = []

for i in range(n):
    world.append(list(map(lambda v: [int(v), False], input().split(' '))))

count = 1

world[y][x][1] = True  # 시작은 들름


for i in world:
    print(i)

while True:
    for k in range(4):
        if 0 <= (y + see[d][0]) <= n and 0 <= (x + see[d][1]) <= m:
            next = world[y + see[d][0]][x + see[d][1]]

            if next[0] == 0 and next[1] is False:
                y = y + see[d][0]
                x = x + see[d][1]
                world[y][x][1] = True
                d = (d + 3) % 4
                count += 1
                break
            else:
                d = (d + 3) % 4

            if k == 3:
                y = see[(d + 3) % 4][0]
                x = see[(d + 3) % 4][1]

                if not (0 <= y <= n and 0 <= x <= m  and world[y][x][0] == 1):
                    print(count)
                    for i in world:
                        print(i)
                    exit()
                else:
                    world[y][x][1] = True
                    count += 1
