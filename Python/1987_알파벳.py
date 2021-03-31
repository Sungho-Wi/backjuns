dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def bfs(r, c):
    global matrix
    maximum_result = 0
    queue = set([(0, 0, matrix[0][0])])

    while queue:
        y_, x_, visited = queue.pop()
        maximum_result = max(maximum_result, len(visited))

        for i in range(4):
            move_y = y_ + dy[i]
            move_x = x_ + dx[i]

            if 0 <= move_y < r and 0 <= move_x < c and matrix[move_y][move_x] not in visited:
                queue.add((move_y, move_x, visited + matrix[move_y][move_x]))

    return maximum_result


R, C = map(int, input().split())

matrix = []

for _ in range(R):
    matrix.append(list(input()))

print(bfs(R, C))
