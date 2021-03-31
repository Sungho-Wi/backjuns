from copy import deepcopy
from collections import deque


def set_virus(matrix, y, x, n, m):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    queue = deque([(y, x)])

    while queue:
        y_, x_ = queue.popleft()

        for i in range(4):
            moved_y = y_ + dy[i]
            moved_x = x_ + dx[i]

            if 0 <= moved_y < n and 0 <= moved_x < m and matrix[moved_y][moved_x] == 0:
                queue.append((moved_y, moved_x))
                matrix[moved_y][moved_x] = 1

    return matrix


def get_area(matrix, n, m):
    for y in range(n):
        for x in range(m):
            if matrix[y][x] == 2:
                matrix = set_virus(matrix, y, x, n, m)

    safe_room_count = 0

    for y in range(n):
        for x in range(m):
            if matrix[y][x] == 0:
                safe_room_count += 1

    return safe_room_count


N, M = map(int, input().split())

MATRIX = []

for _ in range(N):
    MATRIX.append(list(map(int, input().split())))

result = 0

for first_index in range(N * M):
    if MATRIX[first_index // M][first_index % M] != 0:
        continue
    for second_index in range(first_index + 1, N * M):
        if MATRIX[second_index // M][second_index % M] != 0:
            continue
        for third_index in range(second_index + 1, N * M):
            if MATRIX[third_index // M][third_index % M] != 0:
                continue

            new_matrix = deepcopy(MATRIX)
            new_matrix[first_index // M][first_index % M] = 1
            new_matrix[second_index // M][second_index % M] = 1
            new_matrix[third_index // M][third_index % M] = 1
            result = max(result, get_area(new_matrix, N, M))

print(result)
