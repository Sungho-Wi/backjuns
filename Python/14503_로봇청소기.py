N, M = map(int, input().split())

MOVE = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cur_y, cur_x, direction = map(int, input().split())

map_ = []

result = 1

for i in range(N):
    map_.append(list(map(int, input().split())))

while True:
    map_[cur_y][cur_x] = 2

    copy_direction = direction

    going = False

    for i in range(4):
        copy_direction = copy_direction - 1 if copy_direction - 1 >= 0 else 3

        move_y = cur_y + MOVE[copy_direction][0]
        move_x = cur_x + MOVE[copy_direction][1]

        if 0 <= move_y < N and 0 <= move_x < M and map_[move_y][move_x] == 0:
            direction = copy_direction
            cur_y = move_y
            cur_x = move_x

            going = True
            result += 1
            break

    if not going:
        back_direction = (direction + 2) % 4
        cur_y += MOVE[back_direction][0]
        cur_x += MOVE[back_direction][1]

        if 0 <= cur_y < N and 0 <= cur_x < M and map_[cur_y][cur_x] == 1:
            break

print(result)
