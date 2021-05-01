from collections import deque

N = int(input())
K = int(input())
board = [[0] * (N + 1) for _ in range(N + 1)]
board[1][1] = 1

move_queue = deque([])

for _ in range(K):
    y, x = map(int, input().split())
    board[y][x] = 2

L = int(input())

for _ in range(L):
    move_queue.append(list(map(lambda x: int(x) if x.isdigit() else x, input().split())))

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_direction = 0
location = (1, 1)
current_time = 0
snake = deque([(1, 1)])

while True:
    current_time += 1

    dy, dx = direction[current_direction]

    location = (location[0] + dy, location[1] + dx)

    if (not (0 < location[0] <= N and 0 < location[1] <= N)) or board[location[0]][location[1]] == 1:
        break

    snake.append((location[0], location[1]))

    if board[location[0]][location[1]] != 2:
        remove_y, remove_x = snake.popleft()
        board[remove_y][remove_x] = 0

    if len(move_queue) > 0 and move_queue[0][0] == current_time:
        move = move_queue.popleft()
        if move[1] == 'D':
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction - 1) % 4

    board[location[0]][location[1]] = 1

print(current_time)
