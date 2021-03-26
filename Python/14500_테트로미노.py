N, M = map(int, input().split())

map_ = []

for i in range(N):
    map_.append(list(map(int, input().split())))

items = [
    [(0, 1), (0, 2), (0, 3)],
    [(0, 1), (1, 0), (1, 1)],
    [(1, 0), (2, 0), (2, 1)],
    [(1, 0), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (1, 1)],
]

condition = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

maximum_value = 0


def get_total_value(item, y, x):
    max_value = 0
    for i in range(8):
        total_value = map_[y][x]

        con_y, con_x = condition[i % 4]
        for y_, x_ in item:
            y_ *= con_y
            x_ *= con_x

            if i > 3:
                x_, y_ = y_, x_

            if not (0 <= y + y_ < N and 0 <= x + x_ < M):
                total_value = -1
                break
            total_value += map_[y + y_][x + x_]

        max_value = max(max_value, total_value)

    return max_value


for y in range(N):
    for x in range(M):
        for item in items:
            maximum_value = max(maximum_value, get_total_value(item, y, x))

print(maximum_value)